from typing import Callable, Iterable
import pandas as pd
import spacy
from spacy.tokens import Token
from spacy.language import Language
import random
import numpy as np
from tqdm import tqdm

# TODO: DATA_PATH = "data/Tatoeba Corpus/ca-es.txt/Tatoeba.ca-es.ca"
DATA_PATH = "test.txt"
OUTPUT_PATH = "synthetic_glosses.txt"
ACCEPTED_TAGS = ("NOUN", "VERB", "ADJ", "ADV", "NUM")

Augmentation_rule_t = Callable[[Iterable[Token]], str]


def get_lemmas(sent: list[Token]) -> list[str]:
    """get the lemmas from the tokens, and return them all uppercase

    Args:
        sent (list[Token]): the tokens we want to take the lemmas from

    Returns:
        list[str]: the list of lemmas in the same order
    """

    return [token.lemma_.upper() for token in sent]


def filter_tokens_by_tag(sent: Iterable[Token]) -> list[Token]:
    """returns the tokenized sentence without all the tokens with unaccepted POS tags

    Args:
        sent (list[Token]): the sentence to filter

    Returns:
        list[Token]: the filtered sentence
    """
    return [token for token in sent if token.pos_ in ACCEPTED_TAGS]


def discard_random_tokens(sent: Iterable[Token], p: float = 0.2) -> list[Token]:
    """randomly discard the tokens of the given sentence with probability p

    Args:
        sent (list[Token]): the sentence that is going to go through the discards
        p (float, optional): probability of a token being discarded. Defaults to 0.2.

    Returns:
        list[Token]: the new sentence
    """
    # ? Are we sure we want to discard ANY tag?
    return [token for token in sent if random.random() >= p]


def permute_with_max_distance(
    sent: Iterable[Token], max_distance: int = 4
) -> list[Token]:
    """Apply a random permutation σ to S verifying ∀i ∈ {1, n}, |σ(i) − i| ≤ max_distance, where n is the number of tokens

    Args:
        sent (list[Token]): sentence to apply the permutation to
        max_distance (int, optional): maximum distance betweent the original position of the permutation and the new one. Defaults to 4.

    Returns:
        list[Token]: the permutated sentence
    """
    sent = list(sent)
    n = len((sent))

    # Keep trying permutations if they don't comply with the rules
    while True:
        perm = np.random.permutation(n)

        # Check if the current permutation complies
        if all(abs(sigma_i - i) <= max_distance for i, sigma_i in enumerate(perm)):
            # Apply the valid permutation to the sentence
            permuted_sent = [sent[sigma_i] for sigma_i in perm]

            return permuted_sent

def moryossef_general_rules(sent: Iterable[Token]) -> str:
    """
    1. Discard all tokens t ∈ S if POS(t) not in {noun, verb, adjective, adverb, numeral}
    2. Discard remaining tokens t ∈ S with probability p = 0.2
    3. Lemmatize all tokens t ∈ S
    4. Apply a random permutation σ to S verifying ∀i ∈ {1, n}, |σ(i) − i| ≤ 4

    Args:
        sent (Iterable[Token]): the tokenized sentence we want to apply the rules to

    Returns:
        str: the sentence after applying Moryossef general rules
    """
    sentence = filter_tokens_by_tag(sent)
    sentence = discard_random_tokens(sentence)
    sentence = permute_with_max_distance(sentence)
    sentence = get_lemmas(sentence)

    # ? The output format might need to be changed, so that it is the same as in the LSC Corpus
    return " ".join(sentence)

def generate_synthetic_glosses(nlp: Language, sent: str, augmentation_rules: Augmentation_rule_t, iterations: int=1) -> list[str]:
    """generate a synthetic gloss representation of the given string

    Args:
        nlp (Language): the spacy Language model to use for POS and lemmatizing
        sent (str): the sentence to translate into glosses

    Returns:
        str: the synthetic glosses created from the given sentence
    """
    sentence = nlp(sent)
    
    return [augmentation_rules(sentence) for _ in range(iterations)]


def main() -> None:
    #Load the spacy model
    print("Loading SpaCy model...")
    nlp = spacy.load("ca_core_news_trf")
    
    
    #Read the sentences into a dataframe and eliminate duplicates
    print(f"Reading input file at: {DATA_PATH}")
    with open(DATA_PATH, "r") as fp:
        lines = fp.readlines()
        sentences = [line.strip() for line in lines]
        df = pd.DataFrame(sentences, columns=["sentences"]).drop_duplicates()
        
        
    # * Create the synthetic gloss translation applying some rules
    synthetic_data = []
    for sent in tqdm(df["sentences"], desc="Processing sentences", unit="sentence"):
        synthetic_data.extend(generate_synthetic_glosses(nlp, sent, moryossef_general_rules))
    
    
    #Drop duplicates and empty values
    synthetic_df = pd.DataFrame(synthetic_data, columns=["sentences"]).drop_duplicates()
    synthetic_df = synthetic_df[synthetic_df["sentences"].str.strip() != ""]
    
    
    print(f"Writing output at: {OUTPUT_PATH}")
    #Write the results into a new file
    with open(OUTPUT_PATH, "w") as fp:
        for line in synthetic_df["sentences"]:
            fp.write(line + "\n")


if __name__ == "__main__":
    main()
