import numpy as np
from spacy.tokens import Token
from typing import Iterable
import random

ACCEPTED_TAGS = ("NOUN", "VERB", "ADJ", "ADV", "NUM")


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