from typing import Iterable
from spacy.tokens import Token
import numpy as np
import spacy


def find_adjectives(sentence: list[Token]) -> dict[int, int]:
    """Finds the adjectives, returning a dict that maps them to the noun they modify

    Args:
        sentence (list[tuple[int, Token]]): the sentence to analyze

    Returns:
        dict[int, int]: a mapping of the adjectives to the noun they modify
    """

    # Dictionary to hold adjective index -> noun index mapping
    adj_noun_dict = {}

    # Iterate over each token in the sentence
    for token in sentence:
        # Check if the token is an adjective
        if token.pos_ == "ADJ":
            # Look for nouns that the adjective modifies
            if token.dep_ == "amod" and token.head.pos_ == "NOUN":
                adj_noun_dict[token.i] = token.head.i
            # Look for adjectival complements (e.g., "is happy")
            elif token.dep_ == "acomp":
                for child in token.children:
                    if child.dep_ == "attr" and child.pos_ == "NOUN":
                        adj_noun_dict[token.i] = child.i

    return adj_noun_dict


def find_adverbials(sentence: list[Token]) -> dict[int, int]:
    # Dictionary to hold adverbial index -> verb index mapping
    adv_verb_dict = {}

    # Iterate over each token in the sentence
    for token in sentence:
        # Check if the token is an adverb
        if token.pos_ == "ADV":
            # Look for verbs that the adverb modifies
            if token.dep_ in ("advmod", "amod") and token.head.pos_ == "VERB":
                adv_verb_dict[token.i] = token.head.i

    return adv_verb_dict


def find_subject_object_verb(sentence: list[Token]) -> dict[str, list[int]]:
    # Initialize dictionaries to store token indices
    components = {"noun_phrase": [], "object": [], "verbal_phrase": []}

    # Get the root of the sentence
    root = next(token for token in sentence if token.dep_ == "ROOT")

    components["verbal_phrase"].append(root.i)

    stack = [("root", child) for child in root.children]

    while len(stack) > 0:
        tag, token = stack.pop()

        if token.dep_ == "nsubj" or tag == "subject":
            stack.extend([("subject", child) for child in token.children])
            components["noun_phrase"].append(token.i)

        elif token.dep_ == "obj" or tag == "object":
            stack.extend([("object", child) for child in token.children])
            components["object"].append(token.i)
        else:
            stack.extend([("root", child) for child in token.children])
            components["verbal_phrase"].append(token.i)

    return components


def reorder_sentence(sentence: Iterable[Token]) -> Iterable[Token]:
    # Find the adjectives, adverbials and the important syntactical components
    adjectives = find_adjectives(sentence)
    adverbials = find_adverbials(sentence)
    subject_object_verb = find_subject_object_verb(sentence)

    order = [i for values in subject_object_verb.values() for i in values]

    # Put adjectives after the noun
    for adj, noun in adjectives.items():
        order.remove(adj)
        noun_pos = order.index(noun)
        order.insert(noun_pos + 1, adj)

    # Put adverbials after the verb
    for adv, verb in adverbials.items():
        order.remove(adv)
        verb_pos = order.index(verb)
        order.insert(verb_pos + 1, adv)

    reordered_sentence = np.array(sentence)[order]
    return list(reordered_sentence)


if __name__ == "__main__":
    nlp = spacy.load("ca_core_news_sm")
    print("Spacy model loaded!")
    example_sentence = '" Si no fan les vacances abans de ser substituïts per personal que ha tret la plaça en propietat , perden el dret a cobrar -les , i ara mateix no poden sortir els assumptes del jutjat " , ha dit .'
    print("Sentence: ", example_sentence)
    print(reorder_sentence(nlp(example_sentence)))
