# import mysql.connector as mc
# from mysql.connector import Error
#
# HOSTNAME = "viaduct.proxy.rlwy.net"
# USERNAME = "root"
# PASSWORD = "gdBIIliGMPHtlmSUzpqoFALsgmIwCqBK"
# DBNAME = "railway"
# PORT = "37425"
#
#
# def connexion():
#     conn = mc.connect(host=HOSTNAME, user=USERNAME, passwd=PASSWORD, database=DBNAME, port=PORT)
#     cur = conn.cursor()
#     try:
#         cur.execute("""CREATE TABLE IF NOT EXISTS devis (
#                             id              INTEGER PRIMARY KEY AUTO_INCREMENT,
#                             numero          TEXT,
#                             date            DATE,
#                             client          INTEGER,
#                             montant         NUMERIC,
#                             objet           TEXT,
#                             remise          INTEGER,
#                             montant_lettres TEXT,
#                             statut          TEXT,
#                             note_bene       TEXT,
#                             delai           TEXT,
#                             point_liv       TEXT,
#                             validite        INTEGER,
#                             paiement        TEXT,
#                             cree_par        TEXT,
#                             last_modif      TEXT)""")
#         conn.commit()
#         conn.close()
#         print("table crée")
#
#     except Exception as e:
#         print(f"Erreur : {e}")
#
#
# connexion()