from tkinter import *
import sqlite3
from Connexion import conn

root = Tk()
root.title("Gestion de stock")
root.geometry("400x600")

conn = sqlite3.connect("boutique.sqlite3")
c = conn.cursor()

# Create TABLE 
# c.execute("""create table produit (
#         nom varchar(255),
#         description TEXT,
#         prix INTEGER,
#         quantite INTEGER,
#         id_categorie INTEGER
#         )
#         """)

def save():
    conn = sqlite3.connect("boutique.sqlite3")
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("""UPDATE produit SET
        nom = :nom,
        description = :description,
        prix = :prix,
        quantite = :quantite,
        id_categorie = :id_categorie
    
        WHERE oid = :oid""",
        {
        "nom": nom_edit.get(),
        "description": description_edit.get(),
        "prix": prix_edit.get(),
        "quantite": quantite_edit.get(),
        "id_categorie": id_categorie_edit.get(),
        "oid": record_id
        })

    conn.commit()
    conn.close()
    editor.destroy()


def update():
    global editor
    editor = Tk()
    editor.title("Editer la gestion de stock")
    editor.geometry("300x300")

    conn = sqlite3.connect("boutique.sqlite3")
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM produit WHERE oid= " + record_id)
    records = c.fetchall()

    global nom_edit
    global description_edit
    global prix_edit
    global quantite_edit
    global id_categorie_edit

    # Text boxes
    nom_edit = Entry(editor, width=30)
    nom_edit.grid(row=0, column=2, padx=20, pady= (10, 0))
    description_edit = Entry(editor, width=30)
    description_edit.grid(row=1, column=2)
    prix_edit = Entry(editor, width=30)
    prix_edit.grid(row=2, column=2)
    quantite_edit = Entry(editor, width=30)
    quantite_edit.grid(row=3, column=2)
    id_categorie_edit = Entry(editor, width=30)
    id_categorie_edit.grid(row=4, column=2)

    # Text boxes label
    nom_lbl = Label(editor, text="Nom")
    nom_lbl.grid(row=0, column=0, pady= (10, 0))
    description_lbl = Label(editor, text="Description")
    description_lbl.grid(row=1, column=0)
    prix_lbl = Label(editor, text="Prix (Euros)")
    prix_lbl.grid(row=2, column=0)
    quantite_lbl = Label(editor, text="Quantité")
    quantite_lbl.grid(row=3, column=0)
    id_categorie_lbl = Label(editor, text="ID Catégorie")
    id_categorie_lbl.grid(row=4, column=0)

    for record in records:
            nom_edit.insert(0, record[0])
            description_edit.insert(0, record[1])
            prix_edit.insert(0, record[2])
            quantite_edit.insert(0, record[3])
            id_categorie_edit.insert(0, record[4])

    update_btn = Button(editor, text="Sauvegarder", command=save)
    update_btn.grid(row=5, column=0, columnspan=3, pady=10, padx=10, ipadx=100)

def delete():
    conn = sqlite3.connect("boutique.sqlite3")
    c = conn.cursor()

    c.execute("DELETE FROM produit WHERE oid= " + delete_box.get())
    delete_box.delete(0, END)

    conn.commit()
    conn.close()

def create():
    conn = sqlite3.connect("boutique.sqlite3")
    c = conn.cursor()
    c.execute("INSERT INTO produit VALUES (:nom, :description, :prix, :quantite, :id_categorie)",
              {
                'nom': nom.get(),
                'description': description.get(),
                'prix': prix.get(),
                'quantite': quantite.get(),
                'id_categorie': id_categorie.get()
              })

    conn.commit()
    conn.close()

    nom.delete(0, END)
    description.delete(0, END)
    prix.delete(0, END)
    quantite.delete(0, END)
    id_categorie.delete(0, END)


def read():
    conn = sqlite3.connect("boutique.sqlite3")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM produit")
    records = c.fetchall()

    print_records = ""
    for record in records:
        # Utiliser un seul espace entre le record 5 et le record 1
        print_records += "{:<15} {:<10}\n".format(record[5], record[1])

    read_lbl = Label(root, text=print_records, justify=LEFT)
    read_lbl.grid(row=11, column=0, columnspan=2)

    conn.commit()
    conn.close()

# Text boxes
nom = Entry(root, width=30)
nom.grid(row=0, column=1, padx=20, pady= (10, 0))
description = Entry(root, width=30)
description.grid(row=1, column=1)
prix = Entry(root, width=30)
prix.grid(row=2, column=1)
quantite = Entry(root, width=30)
quantite.grid(row=3, column=1)
id_categorie = Entry(root, width=30)
id_categorie.grid(row=4, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1, pady=5)

# Text boxes label
nom_lbl = Label(root, text="Nom")
nom_lbl.grid(row=0, column=0, pady= (10, 0))
description_lbl = Label(root, text="Description")
description_lbl.grid(row=1, column=0)
prix_lbl = Label(root, text="Prix (Euros)")
prix_lbl.grid(row=2, column=0)
quantite_lbl = Label(root, text="Quantité")
quantite_lbl.grid(row=3, column=0)
id_categorie_lbl = Label(root, text="ID Catégorie")
id_categorie_lbl.grid(row=4, column=0)
delete_box_lbl= Label(root, text= "Choix de l'ID")
delete_box_lbl.grid(row=8, column=0, pady=5)

create_btn = Button(root, text="Ajouter à la base de données", command=create)
create_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
read_btn = Button(root, text="Afficher la table", command=read)
read_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=134)
delete_btn = Button(root, text="Supprimer de la table", command=delete)
delete_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=119)
update_btn = Button(root, text="Editer la table", command=update)
update_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=139)


#commit changes
conn.commit()

#close connection
conn.close()

root.mainloop()