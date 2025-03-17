from flask import Flask
import mysql.connector
import os
import time

app = Flask(__name__)

db_config = {
    "host": os.getenv("DB_HOST", "mysql"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "IvoLuis023rd"),
    "database": os.getenv("DB_NAME", "testdb"),
}

def initialize_database():
    """ Verifica si la base de datos existe; si no, la crea. """
    try:
        conn = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["root"],
            password=db_config["IvoLuis023rd"]
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config['database']};")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error al conectar a MySQL: {e}")
        time.sleep(5)
        initialize_database()

initialize_database()

@app.route("/")
def hello_world():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT 'Conexión a MySQL exitosa' AS mensaje;")
        result = cursor.fetchone()
        conn.close()
        return f"Hola Mundo! - {result[0]}"
    except Exception as e:
        return f"Error conectando a la BD: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
