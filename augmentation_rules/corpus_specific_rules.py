from typing import Iterable
from spacy.tokens import Token


def convert_date(sentence: Iterable[Token]) -> Iterable[Token] | list[str]:
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
    "dilluns , 19 de novembre de 2007"
    "després dilluns dia 19 mes novembre any 2007"

    if len(sentence) != 7:
        return sentence

    # Check if it is a date
    week_day = sentence[0].text
    year = sentence[6].text
    month = sentence[4].text
    day = sentence[2].text

    if week_day in week_days and month in months:
        gloss_sentence = f"després {week_day} dia {day} mes {month} any {year}"
        return gloss_sentence.split()

    return sentence


def prepirineu_rule(sentence: list[str]) -> list[str]:
    """Converts the word prepirineus into per-sota pirineus

    Args:
        sentence (Iterable[Token]): the sentence we apply the rule to

    Returns:
        Iterable[Token]: the sentence with the converted token
    """

    sentence_list = []
    for tok in sentence:
        if tok == "prepirineu":
            sentence_list.extend(["per-sota", "pirineus"])
        else:
            sentence_list.append(tok)

    return sentence_list


def marejol_rule(sentence: list[str]) -> list[str]:
    """Converts the word marejol into mar onades

    Args:
        sentence (Iterable[Token]): the sentence we apply the rule to

    Returns:
        Iterable[Token]: the sentence with the converted token
    """

    sentence_list = []
    for tok in sentence:
        if tok == "marejol":
            sentence_list.extend(["mar", "onades"])
        else:
            sentence_list.append(tok)

    return sentence_list


def directions_rule(sentence: list[str]) -> list[str]:
    directions_mapping = {"oriental": "est", "occidental": "oest"}

    sentence_list = []
    for tok in sentence:
        if tok in directions_mapping:
            sentence_list.append(directions_mapping[tok])
        else:
            sentence_list.append(tok)

    return sentence_list


def wind_names_rule(sentence: list[str]) -> list[str]:
    wind_names_mapping = {
        "tramuntana": ["vent", "nord"],
        "gregal": ["vent", "nord", "est"],
        "llevant": ["vent", "est"],
        "xaloc": ["vent", "sud", "est"],
        "migjorn": ["vent", "sud"],
        "llebeig": ["vent", "sud", "oest"],
        "ponent": ["vent", "oest"],
        "mestral": ["vent", "nord", "oest"],
    }

    sentence_list = []
    for tok in sentence:
        if tok in wind_names_mapping:
            sentence_list.extend(wind_names_mapping[tok])
        else:
            sentence_list.append(tok)

    return sentence_list
