class Categorie:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def create_categorie(self, nom):
        sql = "INSERT INTO categorie (nom) VALUES (%s)"
        val = (nom,)
        self.cursor.execute(sql, val)
        self.conn.commit()
        return self.cursor.lastrowid

    def read_categorie(self):
        self.cursor.execute("SELECT * FROM categorie")
        result = self.cursor.fetchall()
        for row in result:
            print(row)

    def update_categorie(self, id, nom):
        sql = "UPDATE categorie SET nom = %s WHERE id = %s"
        val = (nom, id)
        self.cursor.execute(sql, val)
        self.conn.commit()
        return True

    def delete_categorie(self, id):
        sql = "DELETE FROM categorie WHERE id = %s"
        val = (id,)
        self.cursor.execute(sql, val)
        self.conn.commit()
        return self.cursor.rowcount  