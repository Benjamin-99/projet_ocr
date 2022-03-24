import mysql.connector

##  connexion à la base de données
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ocr_data"
)


# initialisation du manager de db
cursor = db.cursor()




# Enregistrer le permis passé en parametre
def save_permis(p):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="ocr_data"
    )
    cursor = db.cursor()

    print("Start ! ")
    print(p.categorie)
    query = """INSERT INTO permis (nom, prenom, date_naissance, lieu_naissance, date_creation, date_expiration, lieu_creation, categorie, bande_mrz, numero_permis) VALUES(%s, %s, %s, %s, %s, %s, %s,  %s, %s, %s)"""
    reference = (p.nom,p.prenom,p.date_naissance,p.lieu_naissance,p.date_creation,p.date_expiration,p.lieu_creation,p.categorie,p.bande_mrz,p.numero_permis)
    ex = cursor.execute(query,reference)
    db.commit()
    print("Fini ! ")
    print(reference)
    print(ex)
    db.close()

def save_carte_grise(c):
    reference= (c.num_immatriculation, c.date_immatriculation,c.nom, c.prenom, c.adresse, c.marque, c.version, c.code_identification, c.categorie, c.genre_national, c.carrosserie, c.cylindre, c.puissance, c.type_carburant, c.date_visite_technique)
    cursor.execute("""INSERT INTO carte_grise (num_immatriculation, date_immatriculation, nom, prenom, adresse, marque, version, code_identification, categorie, genre_national, carrosserie, cylindre, puissance, type_carburant, date_visite_technique) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s)""",reference)
    db.commit()
    db.close()

db.close()