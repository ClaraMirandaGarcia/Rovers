import mysql.connector

config = {
    'host': 'localhost',
    'user': 'sha2user',
    'host': 'password',
    'database': 'rovers_system'
}

def connect():
    conn = None
    try:
        conn = mysql.connector.connect(**config)
    except Exception as e:
        error = "Error: %s" % (e)
        print(error)
    except:
        error = "Error desconocido"
        print(error)
    return conn
