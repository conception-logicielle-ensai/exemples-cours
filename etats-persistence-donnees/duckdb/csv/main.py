from typing import Optional
import duckdb

def query_csv_file(file_path_or_url:str, selectquery:str = "*", where:Optional[str] = None):
    query = f"""
        FROM read_csv('{file_path_or_url}')
        SELECT {selectquery}
        """
    if where != None:
        query += f"WHERE {where}"
    query = f"""
        FROM read_csv('fichier.csv')
        SELECT *
        """
    res = duckdb.sql(query)
    return res

def lecture_csv_pop_par_commune():
    file_path = "./ensemble/donnees_communes.csv"
    parcours_donnees = query_csv_file(file_path_or_url=file_path)
    print("PREMIERE REQUETE")
    print(parcours_donnees.columns)
    parcours_donnees.show()
    donnees_du_35 = query_csv_file(file_path_or_url=file_path, where="DEP='35'")
    print(donnees_du_35.show())


 

if __name__ == "__main__":
    lecture_csv_pop_par_commune()
