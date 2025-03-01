import mysql.connector as MC

hostname = "127.0.0.1"
username = "root"
password = "123456"
dbname = "cfavanya"


# CREATION DE LA BAS DE DONNEES
def connect_db():
    conn = MC.connect(host=hostname, user=username, passwd=password, database=dbname)
    cur = conn.cursor(buffered=True)

    # Table des adhérants
    cur.execute(
        """CREATE TABLE IF NOT EXISTS adherants (
              id int NOT NULL AUTO_INCREMENT,
              matricule varchar(25) DEFAULT NULL,
              nom varchar(255) DEFAULT NULL,
              dob varchar(10) DEFAULT NULL,
              pob varchar(45) DEFAULT NULL,
              cni varchar(45) DEFAULT NULL,
              date_cni varchar(10) DEFAULT NULL,
              lieu_cni varchar(10) DEFAULT NULL,
              adresse varchar(255) DEFAULT NULL,
              ville varchar(45) DEFAULT NULL,
              telephone varchar(15) DEFAULT NULL,
              autre_telephone varchar(15) DEFAULT NULL,
              email varchar(45) DEFAULT NULL,
              ref_person varchar(255) DEFAULT NULL,
              ref_number varchar(45) DEFAULT NULL,
              registration_date varchar(10) DEFAULT NULL,
              PRIMARY KEY (id)
          )
        """
    )

    # Table des versements
    cur.execute(
        """CREATE TABLE IF NOT EXISTS versements (
            id int NOT NULL AUTO_INCREMENT,
            numero_operation varchar(45) DEFAULT NULL,
            date_operation varchar(10) DEFAULT NULL,
            matricule varchar(45) DEFAULT NULL,
            montant float DEFAULT NULL,
            methode varchar(45) DEFAULT NULL,
            type varchar(45) DEFAULT NULL,
            numero_piece varchar(45) DEFAULT NULL,
            PRIMARY KEY (id)
            )
        """
    )

    # Table des prêts
    cur.execute(
        """CREATE TABLE IF NOT EXISTS prets (
            id int NOT NULL AUTO_INCREMENT,
            numero_operation varchar(45) DEFAULT NULL,
            date_operation varchar(10) DEFAULT NULL,
            matricule varchar(45) DEFAULT NULL,
            montant float DEFAULT NULL,
            echeance varchar(10) DEFAULT NULL,
            taux float DEFAULT NULL,
            total_rembourser float DEFAULT NULL,
            garant  varchar(3) DEFAULT NULL,
            PRIMARY KEY (id)
            )
        """
    )

    # Table rembousements
    cur.execute(
        """CREATE TABLE IF NOT EXISTS remboursements (
            id int NOT NULL AUTO_INCREMENT,
            numero_operation varchar(45) DEFAULT NULL,
            date_operation varchar(10) DEFAULT NULL,
            matricule varchar(45) DEFAULT NULL,
            montant float DEFAULT NULL,
            methode varchar(45) DEFAULT NULL,
            PRIMARY KEY (id)
            )
        """
    )

    # Table avalistes
    cur.execute(
        """CREATE TABLE IF NOT EXISTS avalistes (
            numero_operation varchar(45) DEFAULT NULL,
            matricule varchar(45) DEFAULT NULL,
            montant float DEFAULT NULL
            )
        """
    )

    # Table des methodes de paiements
    cur.execute(
        """CREATE TABLE IF NOT EXISTS methodes (
            id int NOT NULL AUTO_INCREMENT,
            nom_methode varchar(45) DEFAULT NULL,
            PRIMARY KEY (id)
            )
        """
    )

    # Table des types de versement
    cur.execute(
        """CREATE TABLE IF NOT EXISTS types (
            id int NOT NULL AUTO_INCREMENT,
            nom_type varchar(45) DEFAULT NULL,
            PRIMARY KEY (id)
            )
        """
    )

    conn.commit()
    conn.close()
    conn.close()


connect_db()


# Tables Methodes _____________________________________________________
def ajouter_methode(name):
    conn = MC.connect(host=hostname, user=username, passwd=password, database=dbname)
    cur = conn.cursor(buffered=True)
    cur.execute("""INSERT INTO methodes values (%s, %s)""",  (cur.lastrowid, name))
    conn.commit()
    conn.close()


def all_methodes():
    conn = MC.connect(host=hostname, user=username, passwd=password, database=dbname)
    cur = conn.cursor(buffered=True)
    cur.execute("""SELECT nom_methode FROM methodes""")
    result = cur.fetchall()
    final = [row[0] for row in result]
    conn.commit()
    conn.close()
    return final


# Table des types de versements____________________________________________
def ajouter_type(name):
    conn = MC.connect(host=hostname, user=username, passwd=password, database=dbname)
    cur = conn.cursor(buffered=True)
    cur.execute("""INSERT INTO types values (%s, %s)""",  (cur.lastrowid, name))
    conn.commit()
    conn.close()


def all_types():
    conn = MC.connect(host=hostname, user=username, passwd=password, database=dbname)
    cur = conn.cursor(buffered=True)
    cur.execute("""SELECT nom_type FROM types""")
    result = cur.fetchall()
    final = [row[0] for row in result]
    conn.commit()
    conn.close()
    return final


# Table des versements _______________________________________________________
def numero_du_versement():
    conn = MC.connect(host=hostname, user=username, passwd=password, database=dbname)
    cur = conn.cursor(buffered=True)
    cur.execute("""SELECT id FROM versements ORDER BY id DESC""")
    result = cur.fetchone()

    if result is None:
        numero = "OP/VS/001"

    else:
        if 1 <= result[0] < 10:
            numero = f"OP/VS/00{result[0] + 1}"
        elif 10 <= result[0] < 100:
            numero = f"OP/VS/0{result[0] + 1}"
        else:
            numero = f"OP/VS/{result[0] + 1}"

    conn.commit()
    conn.close()
    return numero


def ajouter_versement(num, date, mat, montant, methode, typp, num_piece):
    conn = MC.connect(host=hostname, user=username, passwd=password, database=dbname)
    cur = conn.cursor(buffered=True)
    cur.execute("""INSERT INTO versements VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (cur.lastrowid, num, date, mat, montant, methode, typp, num_piece))
    conn.commit()
    conn.close()


# ajouter_versement(num="", date="", mat="", montant="", methode="", typp="", num_piece="")


# Table des adhérants _________________________________________
def ajouter_adherant(
        mat, nom, dob, pob, cni, date_cni, lieu_cni, adresse,
        ville, tel1, tel2, email, ref_person, ref_number, regis_date
    ):
    conn = MC.connect(host=hostname, user=username, passwd=password, database=dbname)
    cur = conn.cursor(buffered=True)
    cur.execute(
        """INSERT INTO adherants values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
        (cur.lastrowid, mat, nom, dob, pob, cni, date_cni, lieu_cni,
         adresse, ville, tel1, tel2, email, ref_person, ref_number, regis_date)
    )
    conn.commit()
    conn.close()


def nom_et_matricules_adherants():
    conn = MC.connect(host=hostname, user=username, passwd=password, database=dbname)
    cur = conn.cursor(buffered=True)
    cur.execute('SELECT matricule, nom FROM adherants')
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result


def numero_matricule_nouveau():
    conn = MC.connect(host=hostname, user=username, passwd=password, database=dbname)
    cur = conn.cursor(buffered=True)
    cur.execute("""SELECT count(id) FROM adherants""")
    res = cur.fetchone()

    if res is None:
        mat = "EP001"

    else:
        if 1 <= res[0] + 1 < 10:
            mat = f"EP00{res[0] + 1}"
        elif 10 <= res[0] + 1 < 100:
            mat = f"EP0{res[0] + 1}"
        else:
            mat = f"EP{res[0] + 1}"

    conn.commit()
    conn.close()




    return mat


# ajouter_versement(
#     num=numero_du_versement(),
#     date="2024-07-27", mat="EP034",
#     montant=10000, methode="ESPECES",
#     typp="FONDS", num_piece="146/2024"
# )


