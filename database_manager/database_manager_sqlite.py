import sqlite3


class DataBaseManager(object):
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.error = None

    def connect(self):
        try:
            self.connection = sqlite3.connect('rovers_system.db')
            self.cursor = self.connection.cursor()
            return True

        except sqlite3.Error as error_connection:
            self.error = "Error while connecting to sqlite" + error_connection
            return False

    def exec3(self, sql_qry):
        try:
            self.cursor.execute(sql_qry)
            self.connection.commit()
            return True

        except Exception as error:
            return False

    def exec2(self, sql_qry, parameters):
        try:
            self.cursor.execute(sql_qry, parameters)
            self.connection.commit()
            return True
        except Exception as error:
            return False

    def exec(self, strsql, retrs=True):
        self.error = ""
        try:

            self.cursor.execute(strsql)
            self.connection.commit()

            if retrs:
                result = []
                data = self.cursor.fetchone()
                while (data != None):
                    result.append(data)
                    data = self.cursor.fetchone()
                # el resultado es una lista(result) de tuplas(data)
                return True, result
            return True, None
        except Exception as e:
            self.error = "Error: %s" % (e)
        return False, None

    def close(self):
        try:
            self.cursor.close()
        except Exception as e:
            self.error = "Error: %s" % (e)
