import psycopg2 as psycopg
from os import getenv
from dotenv import load_dotenv

load_dotenv("/home/thais_carvalho/Documents/github/simple-api-flask/.env")


def connect():
    conn = psycopg.connect(
        database=getenv("DB_DATABASE"),
        user=getenv("DB_USER"),
        password=getenv("DB_PASSWORD"),
        host=getenv("DB_HOST"),
        port=getenv("DB_PORT"),
    )

    return conn


def select():
    # Execulta a query
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios")
    records = cursor.fetchall()
    cursor.close()
    conn.close()
    for row in records:
        print(f"id:{row[0]}")
        print(f"Nome:{row[1]}")
        print(f"Sobrenome:{row[2]}")
        print(f"Nascimento:{row[3]}")
        print(f"Altura:{row[4]}")


def insert(values):
    query = f"""
        INSERT INTO usuarios(
            nome,
            sobrenome,
            data_nasc,
            altura
        )
        VALUES(
            '{values[0]}',
            '{values[1]}',
            '{values[2]}',
             {values[3]}
        )
        """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


data = ["gabriela", "cunha", "2000-01-01", 1.58]

# insert(values=data)


def update(nome):
    query = f"""
        UPDATE
            usuarios
        SET
            nome = '{nome}'
        WHERE id = 2;  
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


nome = "Rian"
# update(nome)


def delete(id):
    query = f"""
        DELETE
        FROM usuarios
        Where id = {id}  
    """
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


id = 11

delete(id)
