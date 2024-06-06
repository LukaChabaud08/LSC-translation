from typing import Callable, Iterable
import pandas as pd
import spacy
from spacy.tokens import Token
from spacy.language import Language
from augmentation_rules.moryossef_general_rules import moryossef_general_rules
from augmentation_rules.catalan_specific_rules import LSC_specific_rules
from tqdm import tqdm
import os
from typing import List

# ! DATA_PATH = "data/Tatoeba Corpus/ca-es.txt/Tatoeba.ca-es.ca"
# DATA_PATH = "data/Tatoeba Corpus/ca/Tatoeba.ca-es.ca"
DATA_PATH = "data/tatoeba/ca/Tatoeba.ca-es.ca"
OUTPUT_FILE_NAME = "data/augmented_general_tatoeba/augmented_general_tatoeba"

Augmentation_rule_t = Callable[[Iterable[Token]], str]


def split(txt, seps):
    default_sep = seps[0]

    # we skip seps[0] because that's the default separator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]


def generate_synthetic_glosses(
    nlp: Language,
    sent: str,
    augmentation_rules: Augmentation_rule_t,
    iterations: int = 1,
) -> List[str]:
    """generate a synthetic gloss representation of the given string

    Args:
        nlp (Language): the spacy Language model to use for POS and lemmatizing
        sent (str): the sentence to translate into glosses

    Returns:
        str: the synthetic glosses created from the given sentence
    """
    sentence = nlp(sent)

    return [augmentation_rules(sentence) for _ in range(iterations)]


def write_parallel_sentences(
    original_sentences: List[str], synthetic_data: List[List[str]]
):
    """given some sentences and all their generated synthetic glosses, write them in parallel in 2 different files

    Args:
        original_sentences (list[str]): the original sentences
        synthetic_data (list[list[str]]): all the synthetic translations
    """
    with open(OUTPUT_FILE_NAME + ".lsc", "w+") as fp_gl:
        with open(OUTPUT_FILE_NAME + ".cat", "w+") as fp_ca:
            for i, generated_glosses in enumerate(synthetic_data):
                for line in generated_glosses:
                    if line:
                        fp_ca.write(original_sentences[i] + "\n")
                        fp_gl.write(line + "\n")


def main() -> None:
    # Load the spacy model
    print("Loading SpaCy model...")
    nlp = spacy.load("ca_core_news_sm")

    # Read the sentences into a dataframe and eliminate duplicates
    print(f"Reading input at: {DATA_PATH}")

    if os.path.isdir(DATA_PATH):
        for file in os.listdir(DATA_PATH):
            lines = []
            with open(os.path.join(DATA_PATH, file), "r") as fp:
                lines.extend(fp.readlines())
    else:
        with open(DATA_PATH, "r") as fp:
            lines = fp.readlines()
    sentences = [line.strip() for line in lines]
    df = pd.DataFrame(sentences, columns=["sentences"]).drop_duplicates()

    # * Create the synthetic gloss translation applying some rules
    kept_sentences = []
    synthetic_data = []
    count = 0
    for sent in df["sentences"]:
        # Get rid of sentences that are too long
        if len(split(sent, "., ")) >= 40:
            continue

        count += 1
        kept_sentences.append(sent)
        try:
            synthetic_data.append(
                generate_synthetic_glosses(nlp, sent, moryossef_general_rules)
            )
        except:
            continue

    # Write the parallel results
    print(f"Writing output at: {OUTPUT_FILE_NAME}.ca and {OUTPUT_FILE_NAME}.gl")
    write_parallel_sentences(kept_sentences, synthetic_data)


if __name__ == "__main__":
    main()
