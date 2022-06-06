from Classes import PermisClass
import database_connection as dbc
p = PermisClass("NANDA","Choupo","1997-10-12","Banga","2020-10-15","2025-10-15","Limoges", "B", "9876543210")

dbc.save_permis(p)
