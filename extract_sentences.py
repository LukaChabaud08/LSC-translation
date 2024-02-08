import sys
import os


def main(input_dir: str) -> None:

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
                    words = [token.split("|")[0] for token in tokens]
                    output_fp.write(" ".join(words) + "\n")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Need to input the directory")
        sys.exit()

    main(sys.argv[1])
