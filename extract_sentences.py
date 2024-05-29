import os
from argparse import ArgumentParser


def main(input_dir: str, field: int, ignore_topic_marks: bool) -> None:

    if not os.path.isdir(input_dir):
        print(f"Path {input_dir} is not a valid directory")
        return

    for file in os.listdir(input_dir):

        file_path = os.path.join(input_dir, file)
        output_dir = input_dir + " extracted"
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        output_path = os.path.join(output_dir, file)

        with open(file_path, "r") as fp:
            lines = fp.readlines()
            with open(output_path, "w") as output_fp:

                for line in lines:
                    tokens = line.split()
                    words = [token.split("|")[field] for token in tokens]
                    if ignore_topic_marks:
                        words = [word for word in words if word not in ["?!", "!", "?"]]
                    output_fp.write(" ".join(words) + "\n")


if __name__ == "__main__":

    parser = ArgumentParser()
    parser.add_argument(
        "input_directory",
        help="path to the directory where the corpus files are located",
    )
    parser.add_argument("field", type=int)
    parser.add_argument("--ignore_topic_marks", action="store_true")
    args = parser.parse_args()
    main(args.input_directory, args.field, args.ignore_topic_marks)
