import json
import requests
import re

def reformat(entry: bytes) -> json:
    entry = re.sub(b'\n', b'', entry)
    entry = re.sub(b'\r', b'', entry)
    entry = json.loads(entry.decode("utf-8"))
    return entry

def get_response(url: str) -> json:
    response = reformat(requests.get(url, timeout=None).content)
    return response

def recreate_dict(entry: list) -> list:
    new_list = []
    for dico in entry:
        new_dict = {"id_Bloc": 0,
            "Parcours": 0,
            "Type_de_periode": 0,
            "Libelle_entite": 0,
            "Parcours_suivi": 0,
            "Type_de_parcours": 0,
            "Nombre_de_semestres": 0,
            "Nombre_de_places": 0,
            "Pays": 0,
            "Ville_etrangere": 0,
            "Procedure_d_affectation": 0,
            "Theme": 0,
            "Rang_minimum_2B": 0}
        i = 0
        for value in dico.values():
            new_dict[list(new_dict.keys())[i]] = value
            i += 1
        new_list.append(new_dict)
    return new_list

def get_formations_list() -> list:
    url_mod_list = ["2B_2223", "1A_2324", "2A_2324"]
    url_base = "https://amway.ensam.eu/json"
    for url_mod in url_mod_list:
        url_addon = f"/recherche/109%2C415%2C501%2C416%2C401%2C216%2C419%2C237%2C134%2C404%2C100%2C112%2C223%2C127%2C217%2C227%2C350%2C405%2C103%2C502%2C413%2C122%2C116%2C114%2C132%2C104%2C351%2C208/GI%2CENERG%2CMAT%2CAUTRE%2CELEC%2CENV%2CIA%2CINFO%2CGES_MGMT%2CAERO%2CGM%2CMECATRO%2CCIVIL%2CSANTE%2CCONCEP/3A%2C1_SEM%2CMASTER%2CUEE%2CDOUBLE_DIPLOME%2CUEE_CP%2CMASTER_OF_SCIENCE%2CDOUBLE_MASTER/INGENIEUR_6MOIS%2CS7_RI%2CS8_RI%2CRECHERCHE_10SEMAINES/{url_mod}/19%2C10%2C22%2C7%2C26%2C27%2C123%2C14"
        formation_list = get_response(url_base + url_addon)
    formation_list = recreate_dict(formation_list)
    return formation_list

def get_formations_details(formations_id: list) -> list:
    responses = []
    for id in formations_id:
        responses += get_response(f"https://amway.ensam.eu/json/details/{id}/undefined")
    new_list = []
    for dico in responses:
        new_dict = {"Procedure_d_affectation": 0,
            "Campus_2A": 0,
            "Type_de_parcours": 0,
            "Type_de_parcours_suivi": 0,
            "Theme": 0,
            "Etablissement": 0,
            "Pays": 0,
            "Ville": 0,
            "Nombre_de_semestres": 0,
            "Description_Parcours": 0,
            "Composant_parcours_2": 0,
            "Composant_parcours_3": 0,
            "Composant_parcours_4": 0,
            "Composant_parcours_5": 0,
            "Composant_parcours_6": 0,
            "Description_programme": 0,
            "Langues_d_enseignement": 0,
            "Autre_langue": 0,
            "Tests_de_langue_necessaire": 0,
            "Debut_du_sejour_d_etudes": 0,
            "Details_des_frais_de_scolarite": 0,
            "Frais_de_scolarite_chez_partenaire": 0,
            "Status_erasmus": 0,
            "Autres_possibilites_de_financement": 0,
            "Commentaire_inscription": 0,
            "Inscription_principale_avec_paiement": 0,
            "Inscription_secondaire_sans_paiement": 0,
            "Procedure_de_selection": 0,
            "Particularites": 0,
            "Diplomes_obtenus_supplement_au_diplome": 0,
            "Responsable_parcours": 0,
            "Responsables_admin": 0,
            "Places_disponible_a_l_etape_2B": 0,
            "Site_web_etablissement_partenaire": 0,
            "Site_web_du_parcours": 0,
            "Lien_presentations": 0}
        
        i = 0
        for value in dico.values():
            new_dict[list(new_dict.keys())[i]] = value
            i += 1
        new_list.append(new_dict)

    return new_list