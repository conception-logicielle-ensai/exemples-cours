import psycopg2

try:
    # il faut executer le script rollback-initdb.sql pour tester
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost")
    cursor = conn.cursor()
    cursor.execute("BEGIN")
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Alice", 25))
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("Bob", 35))
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Erreur :", e)
finally:
    cursor.close()
    conn.close()