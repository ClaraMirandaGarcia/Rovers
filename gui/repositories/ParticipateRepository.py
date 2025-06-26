from database_manager.database_manager_sqlite import DataBaseManager
from gui.repositories.DBError import DBError

create_table_sql_query = "CREATE TABLE ROVERS_SIMULATIONS (" \
                         "id INTEGER PRIMARY KEY AUTOINCREMENT," \
                         "rover_id INTEGER," \
                         "simulation_id INTEGER," \
                         "FOREIGN KEY(rover_id) REFERENCES rover(rover_id)," \
                         "FOREIGN KEY(simulation_id) REFERENCES simulation(simulation_id));"

insert_rovers_simulations_sql = "INSERT INTO rovers_simulations VALUES (NULL, ?, ?);"
get_rovers_simulations_query = "SELECT * FROM rovers_simulations;"
get_rovers_simulations_byid_sql = "SELECT * FROM rovers_simulations WHERE id=?;"
get_rovers_simulations_by_rover_id_sql = "SELECT * FROM rovers_simulations WHERE rover_id=?;"
get_rovers_simulations_by_sim_id_sql = "SELECT * FROM rovers_simulations WHERE simulation_id=?;"
delete_rovers_simulations_by_id = "DELETE FROM rovers_simulations WHERE id=?;"
delete_rovers_simulations_by_rover_id_sql = "DELETE FROM rovers_simulations WHERE rover_id=?;"
delete_rovers_simulations_by_sim_id_sql = "DELETE FROM rovers_simulations WHERE simulation_id=?;"
update_rovers_simulations_query = "UPDATE rovers_simulations SET rover_id=?, " \
                                  "simulation_id=?, " \
                                  " WHERE (id=?);"

truncate_query = "DELETE FROM rovers_simulations"


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
        query = cnn.exec(create_table_sql_query)
    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def get_insert_rovers_simulations_sql(rover_id, sim_id):
    tuple = (rover_id, sim_id)
    val = False
    try:
        cnn = DataBaseManager()
        cnn.connect()
        val = cnn.exec2(insert_rovers_simulations_sql, tuple)
    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()
        return val


def update_rovers_simulations_sql(rovers_simulations_id, name_rovers_simulations, battery_rovers_simulations,
                                  translate_speed, translate_battery, exp_speed, exp_battery,
                                  charging_time):
    tuple = (
        name_rovers_simulations, battery_rovers_simulations, translate_speed, translate_battery, exp_speed, exp_battery,
        charging_time, rovers_simulations_id)
    val = False
    try:
        cnn = DataBaseManager()
        cnn.connect()
        val = cnn.exec2(update_rovers_simulations_query, tuple)
    except Exception as e:
        raise DBError("DB", e)
    finally:
        return val
        cnn.close()


def get_all_rovers_simulations():
    try:
        cnn = DataBaseManager()
        cnn.connect()
        rovers_simulationss = cnn.exec(get_rovers_simulations_query)
        return rovers_simulationss

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def get_rovers_simulations_by_rover_id(rovers_id):
    try:
        cnn = DataBaseManager()
        cnn.connect()
        tuple = (rovers_id,)
        cnn.exec2(get_rovers_simulations_by_rover_id_sql, tuple)
        rovers_simulationss = cnn.cursor.fetchall()
        return rovers_simulationss

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def get_rovers_simulations_by_sim_id(sim_id):
    try:
        cnn = DataBaseManager()
        cnn.connect()
        tuple = (sim_id,)
        cnn.exec2(get_rovers_simulations_by_sim_id_sql, tuple)
        rovers_simulationss = cnn.cursor.fetchall()
        return rovers_simulationss

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def delete_rovers_simulations(rovers_simulations_id):
    val = False
    try:
        cnn = DataBaseManager()
        cnn.connect()
        tuple = (rovers_simulations_id,)
        val = cnn.exec2(delete_rovers_simulations_by_id, tuple)
        return val

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def delete_rovers_simulations_by_rover_id(rover_id):
    val = False
    try:
        cnn = DataBaseManager()
        cnn.connect()
        tuple = (rover_id,)
        val = cnn.exec2(delete_rovers_simulations_by_rover_id_sql, tuple)
        return val

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def delete_rovers_simulations_by_sim_id(simulation_id):
    val = False
    try:
        cnn = DataBaseManager()
        cnn.connect()
        tuple = (simulation_id,)
        val = cnn.exec2(delete_rovers_simulations_by_sim_id_sql, tuple)
        return val

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()
