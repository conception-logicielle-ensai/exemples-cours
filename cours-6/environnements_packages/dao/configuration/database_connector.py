from typing import Literal, Optional

import psycopg2

from utils.singleton import Singleton


class DatabaseConnector(metaclass=Singleton):
    _connection = None

    def __init__(
        self,
        db_type: Literal["postgres"] = "postgres",
        db_name: str = "defaultdb",
        user: str = "postgres",
        password: str = "password",
        host: str = "localhost",
        port: int = 5432,
    ):
        self.db_type = db_type
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connect()

    def _connect_postgres(self):
        try:
            DatabaseConnector._connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )
        except psycopg2.Error as e:
            print(f"Erreur de connexion PostgreSQL : {e}")

    def connect(self):
        if DatabaseConnector._connection is not None:
            raise RuntimeError("Base de données déjà connectée!")

        if self.db_type == "postgres":
            self._connect_postgres()
        else:
            raise ValueError("Type de base de données inconnu. Choisissez 'postgres'.")

    def init_db(self):
        connexion = self.get_connection()
        cursor = connexion.cursor()

        # Suppression des tables si elles existent
        cursor.execute("DROP TABLE IF EXISTS roles_user;")
        cursor.execute("DROP TABLE IF EXISTS users;")

        # Création des tables
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username TEXT NOT NULL UNIQUE
            );
            """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS roles_user (
                user_id INTEGER NOT NULL,
                role TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            );
            """
        )
        connexion.commit()

        # Insertion d'un utilisateur 'admin'
        cursor.execute(
            "INSERT INTO users (username) VALUES (%s) RETURNING id;", ("adm",)
        )
        user_id = cursor.fetchone()[0]
        cursor.execute(
            "INSERT INTO roles_user (user_id, role) VALUES (%s, %s)", (user_id, "admin")
        )
        cursor.execute(
            "INSERT INTO roles_user (user_id, role) VALUES (%s, %s)", (user_id, "dev")
        )

        cursor.execute(
            "INSERT INTO users (username) VALUES (%s) RETURNING id;", ("pasadm",)
        )
        user_id = cursor.fetchone()[0]
        cursor.execute(
            "INSERT INTO roles_user (user_id, role) VALUES (%s, %s)", (user_id, "dev")
        )

        connexion.commit()
        self.close_connection()

    def get_connection(self):
        if DatabaseConnector._connection is None:
            self.connect()
        return DatabaseConnector._connection

    def close_connection(self):
        """Ferme la connexion à la base de données si elle est ouverte."""
        if DatabaseConnector._connection is not None:
            DatabaseConnector._connection.close()
            DatabaseConnector._connection = None
