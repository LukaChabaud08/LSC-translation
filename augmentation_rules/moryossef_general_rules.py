from typing import Iterable
from spacy.tokens import Token
from util import filter_tokens_by_tag, discard_random_tokens, permute_with_max_distance, get_lemmas

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