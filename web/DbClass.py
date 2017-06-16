# class DbClass:
#     def __init__(self):
#         import mysql.connector as connector
#
#         self.__dsn = {
#             "host": "localhost",
#             "user": "lyvain",
#             "passwd": "mentos",
#             "db": "rAid_DB"
#         }
#
#         self.__connection = connector.connect(**self.__dsn)
#         self.__cursor = self.__connection.cursor()
#
#     def getDataFromDatabase(self):
#         # Query zonder parameters
#         sqlQuery = "SELECT * FROM tablename"
#
#         self.__cursor.execute(sqlQuery)
#         result = self.__cursor.fetchall()
#         self.__cursor.close()
#         return result
#
#     def getDataFromDatabaseMetVoorwaarde(self, voorwaarde):
#         # Query met parameters
#         sqlQuery = "SELECT * FROM tablename WHERE columnname = '{param1}'"
#         # Combineren van de query en parameter
#         sqlCommand = sqlQuery.format(param1=voorwaarde)
#
#         self.__cursor.execute(sqlCommand)
#         result = self.__cursor.fetchall()
#         self.__cursor.close()
#         return result
#
#     def setDataToDatabaseBoekCursus(self, value1, value2):
#         # Query met parameters
#         sqlQuery = "INSERT INTO boekCursus (startdatum, einddatum) VALUES ('{param1}','{param2}')"
#         # Combineren van de query en parameter
#         sqlCommand = sqlQuery.format(param1=value1, param2=value2)
#
#         self.__cursor.execute(sqlCommand)
#         self.__connection.commit()
#
#     def setDataToDatabaseTitel(self, value1):
#         # Query met parameters
#         sqlQuery = "INSERT INTO titel (titelNaam) VALUES ('{param1}')"
#         # Combineren van de query en parameter
#         sqlCommand = sqlQuery.format(param1=value1)
#
#         self.__cursor.execute(sqlCommand)
#         self.__connection.commit()



class DbClass:
    def __init__(self, database):
        import mysql.connector as connector
        self.__dsn = {
            "host": "localgost",
            "user": "lyvain",
            "passwd": "mentos",
            "db": database,
        }
        self.__connection = connector.connect(**self.__dsn)


    # voor lezen (SELECT)
    # met query(..., return_dict=True) krijg je een dictionary terug,
    # dat vermindert de kans op fouten (zeker bij SELECT * FROM..)
    def query(self, query: str, data: dict = None, dictionary=False):
        try:
            cursor = self.__connection.cursor(dictionary=dictionary)
        except TypeError:
            print("De optie 'dictionary vereist mysql-connector v2.x.x, kan je installeren met: \n "
                  "sudo pip3 install mysql-connector==2.1.4")
            cursor = self.__connection.cursor()
        cursor.execute(query, data)
        result = cursor.fetchall()
        cursor.close()
        return result

    # voor schrijven (INSERT, UPDATE, ...)
    def execute(self, query: str, data: dict = None):
        cursor = self.__connection.cursor()
        cursor.execute(query, data)
        result = cursor.lastrowid
        self.__connection.commit()
        cursor.close()
        return result
