import json
import sys
import os
from datetime import datetime, timezone
import nltk
from nltk.tokenize import word_tokenize


def parse_date(time_string):
    # Define the Catalan names for days of the week and months
    week_days = [
        "dilluns",
        "dimarts",
        "dimecres",
        "dijous",
        "divendres",
        "dissabte",
        "diumenge",
    ]
    months = [
        "gener",
        "febrer",
        "març",
        "abril",
        "maig",
        "juny",
        "juliol",
        "agost",
        "setembre",
        "octubre",
        "novembre",
        "desembre",
    ]

    # Parse the input time string into a datetime object
    parsed_time = datetime.strptime(time_string, "%Y%m%dZ").replace(tzinfo=timezone.utc)

    # Get the day of the week, day of the month, month, and year
    day_of_week = week_days[parsed_time.weekday()]
    day = parsed_time.day
    month = months[parsed_time.month - 1]
    year = parsed_time.year

    # Format the date in the desired Catalan format
    formatted_date = f"{day_of_week} , {day} de {month} de {year}\n"

    return formatted_date


def format_prediction(pred_obj: dict[str, str]) -> str:
    """{
      "estatDelCel": "Circularan n\u00favols alts i mitjans que deixaran el cel mig ennuvolat, sobretot fins a primeres hores del mat\u00ed i a partir de mitja tarda. Durant el centre de la jornada hi haur\u00e0 estones de cel poc ennuvolat.\nA l'extrem nord del Pirineu creixeran alguns n\u00favols d'evoluci\u00f3 di\u00fcrna.",
      "precipitacions": "\u00c9s possible algun ruixat feble i minso al Pirineu occidental.",
      "temperatures": "La temperatura m\u00ednima pujar\u00e0 lleugerament en general, amb alguns valors superiors als 20\u00baC a punts del Pla de Lleida i a trams del litoral central i sud.\nLa temperatura m\u00e0xima ser\u00e0 lleugerament m\u00e9s alta, si b\u00e9 ser\u00e0 lleugerament m\u00e9s baixa a l'extrem nord-est, on localment baixar\u00e0 moderadament. Els valors m\u00e9s alts de temperatura m\u00e0xima superaran els 36 \u00baC a Ponent.",
      "visibilitat": "La visibilitat ser\u00e0 bona o excel\u00b7lent, tot i algun banc de boirina al litoral sud i nord fins a primera hora del mat\u00ed. Al llarg del dia empitjorar\u00e0 en zones elevades de l'oest del pa\u00eds per l'arribada de pols en suspensi\u00f3.",
      "vent": "El vent bufar\u00e0 fluix i de direcci\u00f3 variable de matinada i al final del dia. Durant les hores centrals del dia s'imposar\u00e0 progressivament el vent de component est al litoral i el component sud i est a l'interior. Bufar\u00e0 entre fluix i moderat, m\u00e9s refor\u00e7at al ter\u00e7 sud i a Ponent on hi haur\u00e0 cops forts a la tarda i vespre."
    }"""
    lines = []

    for key, value in pred_obj.items():
        if key == "estatDelCel":
            lines.append("estat de el cel :\n")
        else:
            lines.append(key + " :\n")

        lines.extend(
            [
                " ".join(word_tokenize(sentence.strip())).lower() + " .\n"
                for sentence in value.split(".")
                if len(sentence.strip()) > 0
            ]
        )

    return "".join(lines)


def parse_prediction(input_path: str, output_path: str) -> None:
    if os.path.isdir(input_path):
        files = [
            os.path.join(input_path, file)
            for file in os.listdir(input_path)
            if os.path.isfile(os.path.join(input_path, file)) and file.endswith(".json")
        ]
    else:
        files = [input_path]

    print(files)
    with open(output_path, "w+") as output_fp:
        for file in files:
            with open(file, "r") as fp:
                parsed_file = json.load(fp)
                # Check if there are multiple days in a file
                if isinstance(parsed_file, list):
                    for pred in parsed_file:
                        output_fp.write(parse_date(pred["diaPredit"]))
                        output_fp.write(format_prediction(pred["versio"]["variables"]))
                else:
                    output_fp.write(parse_date(parsed_file["diaPredit"]))
                    output_fp.write(
                        format_prediction(parsed_file["versio"]["variables"])
                    )


if __name__ == "__main__":

    nltk.download("punkt")
    if len(sys.argv) < 3:
        print("Missing arguments")
        sys.exit()

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    parse_prediction(input_path, output_path)
