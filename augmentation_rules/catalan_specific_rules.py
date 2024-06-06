from typing import Iterable
from spacy.tokens import Token
import spacy
from augmentation_rules.corpus_specific_rules import (
    convert_date,
    prepirineu_rule,
    marejol_rule,
    wind_names_rule,
    directions_rule,
)
from augmentation_rules.positional_rules import reorder_sentence
from augmentation_rules.util import get_lemmas, filter_tokens_by_tag


def LSC_specific_rules(sent: Iterable[Token]) -> str:
    """
    Used General Rules (Moryossef et al., 2021)
        1. Remove Determinants
        2. Remove Prepositions
        3. Lemmatize words
    Specific ordering of the glosses, based on LSC Grammar (Quer & Barberà, 2020)
        4. Adjectives are signed after the noun they modify
        5. Adverbials are signed after the verb they modify
        6. Basic order of a sentence is subject-object-verb
        7. Quantifiers can go before and after the noun*
        8. Temporal adverbials at start of sentence*
        9. Frequency adverbials can go anywhere, except negative ones, which go to the end of the sentence*
    Corpus Observed Rules
        10. dilluns , 19 de novembre de 2007 → després dilluns dia 19 mes novembre any 2007
        11. prepirineus → per-sota pirineus
        12. oriental → est, occidental → oest
        13. Substitute wind names by vent [direction]
        14. Marejol → mar onades

    Args:
        sent (Iterable[Token]): the tokenized sentence we want to apply the rules to

    Returns:
        str: the sentence after applying LSC specific rules
    """
    sentence = convert_date(sent)

    if isinstance(sentence, list):
        return " ".join(sentence)

    sentence = reorder_sentence(sentence)

    sentence = filter_tokens_by_tag(sentence)
    sentence = get_lemmas(sentence)

    sentence = prepirineu_rule(sentence)
    sentence = marejol_rule(sentence)
    sentence = directions_rule(sentence)
    sentence = wind_names_rule(sentence)

    return " ".join(sentence)


if __name__ == "__main__":
    nlp = spacy.load("ca_core_news_sm")
    print("Spacy model loaded!")
    example_sentence = (
        "la temperatura màxima pujarà entre lleugerament i moderadament ."
    )

    print(LSC_specific_rules(nlp(example_sentence)))
