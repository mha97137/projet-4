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
players = cursor.fetchall()

for player in players:
    print("Nom         :", player[1])
    print("Prenom      :", player[2])
    print("Age         :", player[3])
    print("Nationalite :", player[4])
    print("Classement  :", player[5])
    print("\n")    

# fermer conexion
conexion.close()

