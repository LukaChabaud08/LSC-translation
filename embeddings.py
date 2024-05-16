from gensim.models import Word2Vec
from typing import List
from argparse import ArgumentParser


def is_alphabetic_word(word: str) -> bool:
    return all(c.isalpha() for c in word)


def get_vocabulary(datapath: str) -> List[str]:
    with open(datapath, "r") as fp:
        lines = fp.readlines()
        words = []

        for line in lines:
            words.extend(line.split())

        return list(filter(is_alphabetic_word, set(words)))


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "corpus_file",
        help="the path to the corpus which will be used to train the embeddings",
    )
    parser.add_argument("output_file", help="the path to the output file")
    args = parser.parse_args()

    model = Word2Vec(corpus_file=args.corpus_file)
    for index, word in enumerate(model.wv.index_to_key):
        print(f"word #{index+1}/{len(model.wv.index_to_key)} is {word}")
    model.wv.save_word2vec_format(args.output_file, binary=False, write_header=False)
