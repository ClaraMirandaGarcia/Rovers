from database_manager.database_manager_sqlite import DataBaseManager
from gui.repositories.DBError import DBError

create_table_sql_query = "CREATE TABLE IF NOT EXISTS ROVER (ROVER_ID INTEGER PRIMARY KEY," \
                         "NAME TEXT NOT NULL," \
                         "BATTERY REAL," \
                         "TRANSLATE_SPEED REAL," \
                         "TRANSLATE_BATTERY REAL," \
                         "EXP_SPEED REAL," \
                         "EXP_BATTERY REAL," \
                         "CHARGING_TIME REAL);"

insert_rover_sql = "INSERT INTO ROVER VALUES (NULL, ?, ?, ?, ?, ?, ?, ?);"
get_rovers_table_query = "SELECT ROVER_ID, NAME, BATTERY, CHARGING_TIME FROM ROVER;"
get_rovers_name_query = "SELECT NAME FROM ROVER;"
get_rovers_query = "SELECT * FROM ROVER;"
get_rover_byid_sql = "SELECT * FROM ROVER WHERE rover_id=?;"
get_rover_by_name_sql = "SELECT ROVER_ID, NAME, BATTERY, CHARGING_TIME FROM ROVER WHERE name LIKE ?;"
get_rover_starting_name_sql = "SELECT ROVER_ID, NAME, BATTERY, CHARGING_TIME FROM ROVER WHERE name LIKE ?;"
get_full_rover_by_name_sql = "SELECT * FROM ROVER WHERE name LIKE ?;"
delete_rover_by_id = "DELETE FROM ROVER WHERE rover_id=?;"
update_rover_query = "UPDATE ROVER SET NAME=?, " \
                     "BATTERY=?, " \
                     "TRANSLATE_SPEED =?," \
                     "TRANSLATE_BATTERY=?, " \
                     "EXP_SPEED=?, " \
                     "EXP_BATTERY=?, " \
                     "CHARGING_TIME=? " \
                     " WHERE (ROVER_ID=?);"
truncate_query = "DELETE FROM ROVER"


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


def get_insert_rover_sql(name_rover, battery_rover, translate_speed, translate_battery, exp_speed,
                         exp_battery,
                         charging_time):
    tuple = (name_rover, battery_rover, translate_speed, translate_battery, exp_speed, exp_battery, charging_time)
    val = False
    try:
        cnn = DataBaseManager()
        cnn.connect()
        val = cnn.exec2(insert_rover_sql, tuple)
    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()
        return val


def update_rover_sql(rover_id, name_rover, battery_rover, translate_speed, translate_battery, exp_speed, exp_battery,
                     charging_time):
    tuple = (
        name_rover, battery_rover, translate_speed, translate_battery, exp_speed, exp_battery, charging_time, rover_id)
    val = False
    try:
        cnn = DataBaseManager()
        cnn.connect()
        val = cnn.exec2(update_rover_query, tuple)
    except Exception as e:
        raise DBError("DB", e)
    finally:
        return val
        cnn.close()


def get_all_rovers():
    try:
        cnn = DataBaseManager()
        cnn.connect()
        rovers = cnn.exec(get_rovers_query)

        return rovers

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def get_rovers_names():
    try:
        cnn = DataBaseManager()
        cnn.connect()
        query_result = cnn.exec(get_rovers_name_query)
        rovers = query_result[1]
        return rovers

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def get_all_rovers_table():
    try:
        cnn = DataBaseManager()
        cnn.connect()
        result = cnn.exec(get_rovers_table_query)
        rovers = result[1]
        return rovers

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def get_rover_by_name(rover_name):
    try:
        cnn = DataBaseManager()
        cnn.connect()
        tuple = (rover_name,)
        cnn.exec2(get_rover_by_name_sql, tuple)
        rovers = cnn.cursor.fetchall()
        return rovers

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def get_rover_starting_name(rover_name):
    try:
        cnn = DataBaseManager()
        cnn.connect()
        tuple = (rover_name,)
        cnn.exec2(get_rover_starting_name_sql, tuple)
        rovers = cnn.cursor.fetchall()
        return rovers

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def get_full_rover_by_name(rover_name):
    try:
        cnn = DataBaseManager()
        cnn.connect()
        tuple = (rover_name,)
        cnn.exec2(get_full_rover_by_name_sql, tuple)
        rovers = cnn.cursor.fetchall()
        return rovers

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def get_rover_by_id(rover_id):
    try:
        cnn = DataBaseManager()
        cnn.connect()
        tuple = (rover_id,)
        cnn.exec2(get_rover_byid_sql, tuple)
        rovers = cnn.cursor.fetchall()
        return rovers

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()


def delete_rover(rover_id):
    val = False
    try:
        cnn = DataBaseManager()
        cnn.connect()
        tuple = (rover_id,)
        val = cnn.exec2(delete_rover_by_id, tuple)
        return val

    except Exception as e:
        raise DBError("DB", e)
    finally:
        cnn.close()
