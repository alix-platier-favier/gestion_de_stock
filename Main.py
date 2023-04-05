from Connexion import conn
from Categorie import Categorie
from Produit import Produit

conn = conn()
cursor = conn.cursor()
cursor.execute("create database if not exists boutique")
cursor.execute("use boutique")
cursor.execute("""create table if not exists categorie
            (
               id INT PRIMARY KEY AUTO_INCREMENT,
               nom varchar(255)
               )""")


cursor.execute("create database if not exists boutique")
cursor.execute("use boutique")
cursor.execute("""create table if not exists produit
            (
               id INT PRIMARY KEY AUTO_INCREMENT,
               nom varchar(255),
               description text,
               prix int,
               quantite int,
               id_categorie int
               )""")


Categorie = Categorie(conn)
Produit = Produit(conn)
Categorie.create_categorie("Informatique")
Categorie.create_categorie("Mode")
Categorie.create_categorie("Jouets")

Produit.create_produit("Ordinateur portable", "Ordinateur portable HP", 799, 10, 1)
Produit.create_produit("T-shirt", "T-shirt en coton rouge", 25, 20, 2)
Produit.create_produit("Lego", "Boîte de 100 pièces pour un vaisseau spatial", 59, 5, 3)
Produit.create_produit("Souris sans fil", "Souris sans fil Logitech", 29, 15, 1)
Produit.create_produit("Robe", "Robe de soirée de couleur noire", 99, 7, 2)


Produit.create_produit("Pull", "Pull en laine blanc", 35, 10, 2)

print(Produit.read_produit())

Produit.delete_produit(11)

print(Produit.read_produit())

conn.close()