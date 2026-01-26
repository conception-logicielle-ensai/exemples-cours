import duckdb

def setup(postgresql_database_url:str):
    con = duckdb.connect()

    # Extensions
    con.execute("INSTALL postgres;")
    con.execute("LOAD postgres;")

    # Connexion Postgres
    con.execute(f"""
        ATTACH '{postgresql_database_url}'
        AS pg (TYPE postgres);
    """)

    return con


def main():
    con = setup(postgresql_database_url="postgresql://demo:demo@localhost:5432/demo_db")

    # Exemple de requête
    result = con.execute("""
        SELECT country, COUNT(*) AS cnt, AVG(age) avg_age
        FROM pg.demo.users
        GROUP BY country
        ORDER BY cnt DESC
    """).fetchall()

    for row in result:
        print(row)


if __name__ == "__main__":
    main()