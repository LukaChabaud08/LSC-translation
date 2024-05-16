from gensim.models.fasttext import load_facebook_vectors
from argparse import ArgumentParser


def fasttext_to_word2vec(input_file: str, output_file: str) -> None:
    model = load_facebook_vectors(input_file)
    model.save_word2vec_format(output_file, binary=False, write_header=False)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("input_file", help="path to the fasttext embeddings")
    parser.add_argument("output_file", help="path to the output file")
    args = parser.parse_args()
    fasttext_to_word2vec(args.input_file, args.output_file)
