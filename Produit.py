class Produit:

    def __init__(self, conn) -> None:
        self.conn = conn
        self.cursor = conn.cursor()
# CA MARCHE PAS A CAUSE DE CA 
    # def create_produit(self, nom, description, prix, quantite, id_categorie):
    #     sql = """INSERT INTO produit (nom, description, prix, quantite, id_categorie) 
    #         SELECT %s, %s, %s, %s, %s
    #         WHERE NOT EXISTS (
    #         SELECT * FROM produit WHERE nom = %s AND description = %s)
    #         """
    #     val = (nom, description, prix, quantite, id_categorie)
    #     self.cursor.execute(sql, val)
    #     self.conn.commit()
    #     return self.cursor.lastrowid


    def read_produit(self):
        self.cursor.execute("SELECT * FROM produit")
        result = self.cursor.fetchall()
        for row in result:
            print(row)

    def update_produit(self, nom=None, description=None, prix=None, quantite=None, id_categorie=None):
        sql = "UPDATE produit SET "
        val = ()
        if nom is not None:
            sql += "nom = %s, "
            val += (nom,)
        if description is not None:
            sql += "description = %s, "
            val += (description,)
        if prix is not None:
            sql += "prix = %s, "
            val += (prix,)
        if quantite is not None:
            sql += "quantite = %s, "
            val += (quantite,)
        if id_categorie is not None:
            sql += "id_categorie = %s, "
            val += (id_categorie,)
        # Retirer la virgule et l'espace finales
        sql = sql[:-2]
        # Ajouter la condition WHERE pour le produit spécifié
        sql += " WHERE id = %s"
        val += (id,)
        self.cursor.execute(sql, val)
        self.conn.commit()
        return True

    def delete_produit(self, id):
        sql = "DELETE FROM produit WHERE id = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        self.conn.commit()
        return self.cursor.rowcount  