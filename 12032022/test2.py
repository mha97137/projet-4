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

# insert data
cursor.execute("INSERT INTO players VALUES (null, 'Ricciardo', 'Daniel', 31, 'Australie', 5)")
conexion.commit()

# list data
cursor.execute("SELECT * FROM players;")
# print(cursor)   # is ok, one objet
players = cursor.fetchall()
print(players)

# fermer conexion
conexion.close()

