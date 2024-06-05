from database.DB_connect import DBConnect
from model.Aereoporti import Aereoporto
from model.Connessioni import Connessione


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def _getAereoporti():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """select *
            FROM airports a"""
        cursor.execute(query)
        for row in cursor:
            result.append(Aereoporto(f"{row["ID"]}", row["AIRPORT"]))
        cursor.close()
        conn.close()
        return result
    @staticmethod
    def _getLinea():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select *
                    FROM flights f"""
        cursor.execute(query)
        for row in cursor:
            result.append(Connessione(row["ID"], row["ORIGIN_AIRPORT_ID"], row["DESTINATION_AIRPORT_ID"], row["DISTANCE"]))
        cursor.close()
        conn.close()
        return result
