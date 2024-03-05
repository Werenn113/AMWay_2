import requests
import re
import json
import unidecode
import time

def reformat(entry: bytes) -> json:
    entry = re.sub(b'\n', b'', entry)
    entry = re.sub(b'\r', b'', entry)
    entry = json.loads(entry.decode("utf-8"))
    return entry

def get_response(url: str) -> json:
    response = reformat(requests.get(url, timeout=None).content)
    return response


def get_formation_id(url_base: str) -> list:
    url_mod_list = ["2B_2223", "1A_2324", "2A_2324"]
    formation_list = []
    for url_mod in url_mod_list:
        url_addon = f"/recherche/109%2C415%2C501%2C416%2C401%2C216%2C419%2C237%2C134%2C404%2C100%2C112%2C223%2C127%2C217%2C227%2C350%2C405%2C103%2C502%2C413%2C122%2C116%2C114%2C132%2C104%2C351%2C208/GI%2CENERG%2CMAT%2CAUTRE%2CELEC%2CENV%2CIA%2CINFO%2CGES_MGMT%2CAERO%2CGM%2CMECATRO%2CCIVIL%2CSANTE%2CCONCEP/3A%2C1_SEM%2CMASTER%2CUEE%2CDOUBLE_DIPLOME%2CUEE_CP%2CMASTER_OF_SCIENCE%2CDOUBLE_MASTER/INGENIEUR_6MOIS%2CS7_RI%2CS8_RI%2CRECHERCHE_10SEMAINES/{url_mod}/19%2C10%2C22%2C7%2C26%2C27%2C123%2C14"
        formation_list += get_response(url_base + url_addon)
    return formation_list


def find_word(formation_id: int, word: str) -> bool:
    url_addon = f"/details/{formation_id}/undefined"
    result = get_response(url_base + url_addon)
    if unidecode.unidecode(word).casefold() in unidecode.unidecode(str(result)).casefold():
        return True
    else:
        return False


if __name__ == "__main__":
    url_base = "https://amway.ensam.eu/json"

    formation_list = get_formation_id(url_base)

    good_formation = []
    compteur = 1
    compteur_max = len(formation_list)
    for formation in formation_list:
        print(f"{compteur}/{compteur_max} -- {compteur/compteur_max*100}")
        if find_word(formation["id.Bloc"], "cyber"):
            good_formation.append(formation)
        compteur += 1
    

    print(good_formation)
    