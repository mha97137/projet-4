import sqlite3


# conexion
conexion = sqlite3.connect('tests.db')

# create cursor
cursor = conexion.cursor()

# create table
cursor.execute("CREATE TABLE IF NOT EXISTS players("+
"id INTEGER PRIMARY KEY AUTOINCREMENT,"+
"nom varchar(50), "+
"prenom varchar(50), "+
"naissance int(99), "+
"sexe varchar(50), "+
"classement int(99)"+
")")

# enregistrer modifications
conexion.commit()

# fermer conexion
conexion.close()
