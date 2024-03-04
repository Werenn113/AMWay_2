import sqlite3
import get_data

### Create Database
conn = sqlite3.connect("formations.db")

### Create Formations table
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Formations")
cur.execute("""CREATE TABLE Formations (
            id_Bloc INTEGER,
            Parcours TEXT,
            Type_de_periode TEXT,
            Libelle_entite TEXT,
            Parcours_suivi TEXT,
            Type_de_parcours TEXT,
            Nombre_de_semestres INTEGER,
            Nombre_de_places INTEGER,
            Pays TEXT,
            Ville_etrangere BOOLEEN,
            Procedure_d_affectation TEXT,
            Theme TEXT,
            Rang_minimum_2B INTEGER
            )""")


### Put data in Formations table
formations_list = get_data.get_formations_list()
cur.executemany("""INSERT INTO Formations (
                    id_Bloc,
                    Parcours,
                    Type_de_periode,
                    Libelle_entite,
                    Parcours_suivi,
                    Type_de_parcours,
                    Nombre_de_semestres,
                    Nombre_de_places,
                    Pays,
                    Ville_etrangere,
                    Procedure_d_affectation,
                    Theme,
                    Rang_minimum_2B) 
                Values (
                    :id_Bloc,
                    :Parcours,
                    :Type_de_periode,
                    :Libelle_entite,
                    :Parcours_suivi,
                    :Type_de_parcours,
                    :Nombre_de_semestres,
                    :Nombre_de_places,
                    :Pays,
                    :Ville_etrangere,
                    :Procedure_d_affectation,
                    :Theme,
                    :Rang_minimum_2B
                )""", formations_list)
conn.commit()


### Create Formations_details table
cur.execute("DROP TABLE IF EXISTS Formations_details")
cur.execute("""CREATE TABLE Formations_details (
            Procedure_d_affectation TEXT,
            Campus_2A TEXT,
            Type_de_parcours TEXT,
            Type_de_parcours_suivi TEXT,
            Theme TEXT,
            Etablissement TEXT,
            Pays TEXT,
            Ville TEXT,
            Nombre_de_semestres INTEGER,
            Description_Parcours TEXT ,
            Composant_parcours_2 TEXT,
            Composant_parcours_3 TEXT,
            Composant_parcours_4 TEXT,
            Composant_parcours_5 TEXT,
            Composant_parcours_6 TEXT,
            Description_programme TEXT,
            Langues_d_enseignement TEXT,
            Autre_langue TEXT,
            Tests_de_langue_necessaire TEXT,
            Debut_du_sejour_d_etudes TEXT,
            Details_des_frais_de_scolarite TEXT,
            Frais_de_scolarite_chez_partenaire TEXT,
            Status_erasmus TEXT,
            Autres_possibilites_de_financement TEXT,
            Commentaire_inscription TEXT,
            Inscription_principale_avec_paiement TEXT,
            Inscription_secondaire_sans_paiement TEXT,
            Procedure_de_selection TEXT,
            Particularites TEXT,
            Diplomes_obtenus_supplement_au_diplome TEXT,
            Responsable_parcours TEXT,
            Responsables_admin TEXT,
            Places_disponible_a_l_etape_2B INTEGER,
            Site_web_etablissement_partenaire TEXT,
            Site_web_du_parcours TEXT,
            Lien_presentations TEXT
            )""")

# faire en sorte d'avoir l'id de la formation dans cette table
### Put data in Formations_details table
formations_id = [i["id_Bloc"] for i in formations_list]
formations_details = get_data.get_formations_details(formations_id)
cur.executemany("""INSERT INTO Formations_details (
                    Procedure_d_affectation,
                    Campus_2A,
                    Type_de_parcours,
                    Type_de_parcours_suivi,
                    Theme,
                    Etablissement,
                    Pays,
                    Ville,
                    Nombre_de_semestres,
                    Description_Parcours,
                    Composant_parcours_2,
                    Composant_parcours_3,
                    Composant_parcours_4,
                    Composant_parcours_5,
                    Composant_parcours_6,
                    Description_programme,
                    Langues_d_enseignement,
                    Autre_langue,
                    Tests_de_langue_necessaire,
                    Debut_du_sejour_d_etudes,
                    Details_des_frais_de_scolarite,
                    Frais_de_scolarite_chez_partenaire,
                    Status_erasmus,
                    Autres_possibilites_de_financement,
                    Commentaire_inscription,
                    Inscription_principale_avec_paiement,
                    Inscription_secondaire_sans_paiement,
                    Procedure_de_selection,
                    Particularites,
                    Diplomes_obtenus_supplement_au_diplome,
                    Responsable_parcours,
                    Responsables_admin,
                    Places_disponible_a_l_etape_2B,
                    Site_web_etablissement_partenaire,
                    Site_web_du_parcours,
                    Lien_presentations)
                Values (
                    :Procedure_d_affectation,
                    :Campus_2A,
                    :Type_de_parcours,
                    :Type_de_parcours_suivi,
                    :Theme,
                    :Etablissement,
                    :Pays,
                    :Ville,
                    :Nombre_de_semestres,
                    :Description_Parcours,
                    :Composant_parcours_2,
                    :Composant_parcours_3,
                    :Composant_parcours_4,
                    :Composant_parcours_5,
                    :Composant_parcours_6,
                    :Description_programme,
                    :Langues_d_enseignement,
                    :Autre_langue,
                    :Tests_de_langue_necessaire,
                    :Debut_du_sejour_d_etudes,
                    :Details_des_frais_de_scolarite,
                    :Frais_de_scolarite_chez_partenaire,
                    :Status_erasmus,
                    :Autres_possibilites_de_financement,
                    :Commentaire_inscription,
                    :Inscription_principale_avec_paiement,
                    :Inscription_secondaire_sans_paiement,
                    :Procedure_de_selection,
                    :Particularites,
                    :Diplomes_obtenus_supplement_au_diplome,
                    :Responsable_parcours,
                    :Responsables_admin,
                    :Places_disponible_a_l_etape_2B,
                    :Site_web_etablissement_partenaire,
                    :Site_web_du_parcours,
                    :Lien_presentations
                )""", formations_details)
conn.commit()

conn.close()