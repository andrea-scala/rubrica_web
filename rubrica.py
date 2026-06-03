import pymysql.cursors
from db import DB
from models import Persona

class Rubrica:
    def __init__(self, config):
        self.db = DB(config)

    def get_all(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lista_contatti ORDER BY cognome, nome")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [Persona(**row) for row in rows]

    def get_by_id(self, id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lista_contatti WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return Persona(**row) if row else None

    def insert(self, persona):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO lista_contatti (nome, cognome, indirizzo, telefono, eta) VALUES (%s, %s, %s, %s, %s)",
            (persona.nome, persona.cognome, persona.indirizzo, persona.telefono, persona.eta)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def update(self, persona):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE lista_contatti SET nome=%s, cognome=%s, indirizzo=%s, telefono=%s, eta=%s WHERE id=%s",
            (persona.nome, persona.cognome, persona.indirizzo, persona.telefono, persona.eta, persona.id)
        )
        conn.commit()
        cursor.close()
        conn.close()

    def delete(self, id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM lista_contatti WHERE id = %s", (id,))
        conn.commit()
        cursor.close()
        conn.close()
        
    def get_utente_by_username(self, username):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM utenti WHERE username = %s", (username,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
if __name__ == "__main__":
    from rubrica import Rubrica
    from models import Persona

    r = Rubrica({})  # config vuoto → DB legge dal .env

    # test get_all
    contatti = r.get_all()
    print("get_all:", contatti)

    # test insert
    persona = Persona(nome='Mario', cognome='Rossi', indirizzo='Via Roma 1', telefono='123456', eta=30)
    r.insert(persona)
    print("insert ok")

    # test get_all dopo insert
    contatti = r.get_all()
    print("get_all dopo insert:", contatti)

    # test get_by_id
    p = r.get_by_id(contatti[0].id)
    print("get_by_id:", p)

    # test update
    p.nome = 'Luigi'
    r.update(p)
    print("update ok")

    # test delete
    r.delete(p.id)
    print("delete ok")

    # verifica finale
    contatti = r.get_all()
    print("get_all finale:", contatti)
        