from typing import Optional
import duckdb

def query_parquet_file(file_path_or_url:str, selectquery:str = "*", where:Optional[str] = None):
    query = f"""
        FROM read_parquet('{file_path_or_url}')
        SELECT {selectquery}
        """
    if where != None:
        query += f"WHERE {where}"
    res = duckdb.sql(query)
    return res

def recuperation_donnees_sirene():
    url_data_sirene = "https://www.data.gouv.fr/api/1/datasets/r/a29c1297-1f92-4e2a-8f6b-8c902ce96c5f"
    parcours_donnees = query_parquet_file(file_path_or_url=url_data_sirene)
    print("PREMIERE REQUETE")
    print(parcours_donnees.columns)
    parcours_donnees.show()
    print("Regardons maintenant les activités principales")
    valeurs_distinctes_naf2025 = query_parquet_file(file_path_or_url=url_data_sirene, selectquery="DISTINCT nomenclatureActivitePrincipaleEtablissement")
    print(valeurs_distinctes_naf2025.show())


 

if __name__ == "__main__":
    recuperation_donnees_sirene()
