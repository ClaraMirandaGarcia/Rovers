import MySQLdb
import mysql.connector
from mysql.connector import Error
from PySide6.QtSql import QSqlDatabase, QSqlQuery


class DataBaseManager(object):
    def __init__(self):
        self.strhost = "localhost"
        self.struser = "sha2user"
        self.strpasswd = "password"
        self.strdb = "rovers_system"
        self.db = None

    def connect2(self):
        print(QSqlDatabase.drivers())
        self.db = QSqlDatabase().addDatabase("QMYSQL")
        print('Last error', self.db.lastError())
        self.db.setHostName(self.strhost)
        self.db.setDatabaseName(self.strdb)
        self.db.setUserName(self.struser)
        self.db.setPassword(self.strpasswd)

        if not self.db.open():
            print("Unable to connect.")
            print('Last error', self.db.lastError())
        else:
            print("Connection to the database successful")

    def connect(self, nport=3306):
        try:

            self.db = mysql.connector.connect(
                host=self.strhost,
                user=self.struser,
                password=self.strpasswd,
                database=self.strdb
            )

            self.rs = self.db.cursor()
            self.status = 1
            return True, self.db
        except Exception as e:
            self.error = "Error: %s" % (e)
            print(self.error)
        except:
            self.error = "Error desconocido"
            print(self.error)
        return False

    def exec2(self, sql_qry,  parameters):
        try:
            self.rs.prepared = True
            self.rs.execute(sql_qry, parameters)
            self.db.commit()
            print("Data inserted successfully")
            return True

        except mysql.connector.Error as error:
            print("parameterized query failed {}".format(error))
            return False

    def exec(self, strsql, retrs=True):
        if self.status == 1:
            self.error = ""
            try:
                print(strsql)
                self.rs.execute(strsql)
                self.db.commit()
                if retrs:
                    result = []
                    data = self.rs.fetchone()
                    while (data != None):
                        result.append(data)
                        data = self.rs.fetchone()
                    # el resultado es una lista(result) de tuplas(data)
                    return True, result
                return True, None
            except Exception as e:
                self.error = "Error: %s" % (e)
                print(self.error)
        return False, None

    def close(self):
        self.status = 0
        try:
            self.rs.close()
        except:
            pass
        try:
            self.cnx.close()
        except:
            pass

    def get_state(self):
        return self.status

    def get_error(self):
        return self.error

    def get_count(self):
        if self.status:
            return self.rs.rowcount
        else:
            return -1
