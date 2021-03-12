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

# insert many data
playerss = [
    ("Ricciardo", "Daniel", 31, "Australie", 5),
    ("Norris", "Lando", 21, "Royaume-Uny", 9),
    ("Vettel", "Sebastian", 33, "Allemagne", 13),
    ("Latifi", "Nicholas", 25, "Canada", 21),
    ("Raikkonen", "Kimi", 41, "Finlande", 16),
    ("Gasly", "Pierre", 25, "France", 10),
    ("Perez", "Sergio", 31, "Mexique", 4),
]

cursor.executemany("INSERT INTO players VALUES (null, ?,?,?,?,?)", playerss) 
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

