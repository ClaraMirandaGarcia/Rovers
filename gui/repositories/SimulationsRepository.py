from database_manager.database_manager_sqlite import DataBaseManager
from gui.repositories.DBError import DBError

create_table_sql_query = "CREATE TABLE IF NOT EXISTS SIMULATION (SIMULATION_ID INTEGER PRIMARY KEY," \
                         "NAME TEXT NOT NULL," \
                         "TOTAL_TIME REAL," \
                         "TOTAL_SPACE REAL," \
                         "NUM_ROVERS INT," \
                         "LOG_FILE_NAME TEXT);"

insert_simulation_sql = "INSERT INTO simulation VALUES (NULL, ?, ?, ?, ?, ?);"
get_simulations_table_query = "SELECT SIMULATION_ID, NAME, TOTAL_TIME, TOTAL_SPACE, NUM_ROVERS, LOG_FILE_NAME FROM " \
                              "simulation; "
get_simulations_name_query = "SELECT NAME FROM simulation;"
get_simulations_query = "SELECT * FROM simulation;"
get_simulation_byid_sql = "SELECT * FROM simulationS WHERE simulation_id=?;"
get_simulation_by_name_sql = "SELECT SIMULATION_ID, NAME, TOTAL_TIME, TOTAL_SPACE, NUM_ROVERS, LOG_FILE_NAME FROM " \
                             "simulation " \
                             "WHERE name LIKE ?;"
get_simulation_starting_name_sql = "SELECT SIMULATION_ID, NAME, TOTAL_TIME, TOTAL_SPACE, NUM_ROVERS, LOG_FILE_NAME " \
                                   "FROM " \
                                   "simulation WHERE name LIKE ?; "
get_full_simulation_by_name_sql = "SELECT * FROM simulation WHERE name LIKE ?;"
delete_simulation_by_id = "DELETE FROM simulation WHERE simulation_id=?;"
update_simulation_query = "UPDATE simulation SET NAME=?, " \
                          "TOTAL_TIME=?, " \
                          "TOTAL_SPACE=?, " \
                          "NUM_ROVERS =?," \
                          "LOG_FILE_NAME=?" \
                          " WHERE (simulation_ID=?);"

truncate_query = "DELETE FROM simulation"


def truncate_table_sql():
    try:
        cnn = DataBaseManager()
        cnn.connect()
        cnn.exec3(truncate_query)
    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def get_create_table_sql():
    try:
        cnn = DataBaseManager()
        cnn.connect()
        cnn.exec(create_table_sql_query)
    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def get_insert_simulation_sql(name, total_time, total_space, num_rovers, name_file):
    tuple_var = (
        name, total_time, total_space, num_rovers, name_file)
    val = False
    try:
        cnn = DataBaseManager()
        cnn.connect()
        val = cnn.exec2(insert_simulation_sql, tuple_var)
    except Exception as e:
        return DBError("DB", e)
    finally:
        cnn.close()
        return val


def get_all_simulations_table():
    try:
        cnn = DataBaseManager()
        cnn.connect()
        result = cnn.exec(get_simulations_table_query)
        simulations = result[1]
        return simulations

    except Exception as e:
        return DBError("DB", e)
    finally:
        cnn.close()


def get_simulation_by_name(simulation_name):
    try:
        cnn = DataBaseManager()
        cnn.connect()
        tuple_var = (simulation_name,)
        cnn.exec2(get_simulation_by_name_sql, tuple_var)
        simulations = cnn.cursor.fetchall()
        return simulations

    except Exception as e:
        return DBError("DB", e)
    finally:
        cnn.close()


def get_simulation_starting_name(simulation_name):
    try:
        cnn = DataBaseManager()
        cnn.connect()
        tuple_var = (simulation_name,)
        cnn.exec2(get_simulation_starting_name_sql, tuple_var)
        simulations = cnn.cursor.fetchall()
        return simulations

    except Exception as e:
        return DBError("DB", e)
    finally:
        cnn.close()


def delete_simulation(simulation_id):
    val = False
    try:
        cnn = DataBaseManager()
        cnn.connect()
        tuple_var = (simulation_id,)
        val = cnn.exec2(delete_simulation_by_id, tuple_var)
        return val

    except Exception as e:
        return DBError("DB", e)
    finally:
        cnn.close()
