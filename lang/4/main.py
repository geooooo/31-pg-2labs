from prettyprinter import (
    cpprint as cprint,
)
import pymorphy2


def get_case(morph_result):
    """
        Определение падежа
    """
    case = str(morph_result.tag.case).lower()
    if case == "nomn" or case == "voct":
        return "именительный"
    elif case.startswith("gen"):
        return "родительный"
    elif case == "datv":
        return "дательный"
    elif case.startswith("acc"):
        return "винительный"
    elif case == "ablt":
        return "творительный"
    elif case.startswith("loc"):
        return "предложный"
    else:
        return "неизвестно"


def get_gender(morph_result):
    """
        Определение рода
    """
    gender = str(morph_result.tag.gender).lower()
    if gender == "masc":
        return "мужской"
    elif gender == "femn":
        return "женский"
    elif gender == "neut" or gender == "ms-f":
        return "средний"
    else:
        return "неизвестно"


def get_number(morph_result):
    """
        Определение числа
    """
    number = str(morph_result.tag.number).lower()
    if number == "sing":
        return "единственное"
    elif number == "plur":
        return "множественное"
    else:
        return "неизвестно"


def get_pos(morph_result):
    """
        Определение части речи
    """
    pos = str(morph_result.tag.POS).lower()
    if pos == "noun" or pos == "npro":
        return "существительное"
    elif pos.startswith("adj"):
        return "прилагательное"
    elif pos == "verb" or pos == "infn":
        return "глагол"
    elif pos.startswith("prt"):
        return "причастие"
    elif pos == "grnd":
        return "деепричастие"
    elif pos == "comp":
        return "компаратив"
    elif pos == "numb":
        return "числительное"
    elif pos == "advb":
        return "наречие"
    elif pos == "pred":
        return "предикатив"
    elif pos == "prep":
        return "предлог"
    elif pos == "conj":
        return "союз"
    elif pos == "prcl" or pos == "intj":
        return "междометие"
    else:
        return "неизвестно"


def get_normal_form(morph_result):
    return str(morph_result.normal_form).lower()


def lemma(word):
    morph = pymorphy2.MorphAnalyzer()
    morph_result = morph.parse(word)[0]
    cprint(f"Слово:          {word}")
    cprint(f"Исходная форма: {get_normal_form(morph_result)}")
    cprint(f"Род:            {get_gender(morph_result)}")
    cprint(f"Число:          {get_number(morph_result)}")
    cprint(f"Часть речи:     {get_pos(morph_result)}")
    cprint(f"Падеж:          {get_case(morph_result)}")


for number, word in enumerate(open("dict.txt", "rt").readlines()):
    cprint(f"{'#' * 10} {number + 1} {'#' * 10}")
    lemma(word.strip().lower())
    cprint("")


