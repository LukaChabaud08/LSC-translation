from typing import Callable, Iterable
import pandas as pd
import spacy
from spacy.tokens import Token
from spacy.language import Language
from augmentation_rules.moryossef_general_rules import moryossef_general_rules
from tqdm import tqdm

# ! DATA_PATH = "data/Tatoeba Corpus/ca-es.txt/Tatoeba.ca-es.ca"
DATA_PATH = "test.txt"
OUTPUT_FILE_NAME = "augmented"

Augmentation_rule_t = Callable[[Iterable[Token]], str]


def generate_synthetic_glosses(
    nlp: Language,
    sent: str,
    augmentation_rules: Augmentation_rule_t,
    iterations: int = 1,
) -> list[str]:
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
    original_sentences: list[str], synthetic_data: list[list[str]]
):
    """given some sentences and all their generated synthetic glosses, write them in parallel in 2 different files

    Args:
        original_sentences (list[str]): the original sentences
        synthetic_data (list[list[str]]): all the synthetic translations
    """
    with open(OUTPUT_FILE_NAME + ".gl", "w") as fp_gl:
        with open(OUTPUT_FILE_NAME + ".ca", "w") as fp_ca:
            for i, generated_glosses in enumerate(synthetic_data):
                for line in generated_glosses:
                    fp_ca.write(original_sentences[i] + "\n")
                    fp_gl.write(line + "\n")


def main() -> None:
    # Load the spacy model
    print("Loading SpaCy model...")
    nlp = spacy.load("ca_core_news_trf")

    # Read the sentences into a dataframe and eliminate duplicates
    print(f"Reading input file at: {DATA_PATH}")
    with open(DATA_PATH, "r") as fp:
        lines = fp.readlines()
        sentences = [line.strip() for line in lines]
        df = pd.DataFrame(sentences, columns=["sentences"]).drop_duplicates()

    # * Create the synthetic gloss translation applying some rules
    synthetic_data = []
    for sent in tqdm(df["sentences"], desc="Processing sentences", unit="sentence"):
        synthetic_data.append(
            generate_synthetic_glosses(nlp, sent, moryossef_general_rules)
        )

    # Write the parallel results
    print(f"Writing output at: {OUTPUT_FILE_NAME}.ca and {OUTPUT_FILE_NAME}.gl")
    write_parallel_sentences(df["sentences"].to_list(), synthetic_data)


if __name__ == "__main__":
    main()
