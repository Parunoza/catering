import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="catering",
        user="postgres",
        password="dein_passwort",
        host="localhost",
        port="5432"
    )
