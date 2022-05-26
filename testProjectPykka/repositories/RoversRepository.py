from database_manager import database_manager
from PySide6.QtSql import QSqlQuery

from database_manager.database_manager import DataBaseManager

create_table_sql_query = "CREATE TABLE IF NOT EXISTS ROVERS (ROVER_ID INT AUTO_INCREMENT PRIMARY KEY," \
                         "NAME CHAR(20) NOT NULL," \
                         "BATTERY FLOAT(22)," \
                         "TRANSLATE_SPEED FLOAT(22)," \
                         "TRANSLATE_BATTERY FLOAT(22)," \
                         "EXP_SPEED FLOAT(22)," \
                         "EXP_BATTERY FLOAT(22)," \
                         "CHARGING_TIME FLOAT(22));"

insert_rover_sql = "INSERT INTO rovers VALUES (NULL, %s, %s, %s, %s, %s, %s, %s);"
get_rovers_query = "SELECT * FROM ROVERS;"
get_rover_byid_sql = "SELECT * FROM ROVERS WHERE rover_id=%s;"
get_rover_byname_sql = "SELECT * FROM ROVERS WHERE name=%s;"
delete_rover_by_id = "DELETE FROM ROVERS WHERE rover_id=%s;"
update_rover_query = "UPDATE rovers SET NAME=%s, " \
                   "BATTERY=%s, " \
                   "TRANSLATE_SPEED =%s," \
                   "TRANSLATE_BATTERY=%s, " \
                   "EXP_SPEED=%s, " \
                   "EXP_BATTERY=%s, " \
                   "CHARGING_TIME=%s " \
                   " WHERE (ROVER_ID=%s);"


def get_create_table_sql(dbm: DataBaseManager):
    try:
        cnn = DataBaseManager()
        cnn.connect(3306)
        query = cnn.exec(create_table_sql_query)
    except Exception as e:
        print(e)
    finally:
        cnn.close()


def get_insert_rover_sql(dbm: DataBaseManager, name_rover, battery_rover, translate_speed, translate_battery, exp_speed, exp_battery,
                         charging_time):
    tuple = (name_rover, battery_rover, translate_speed, translate_battery, exp_speed, exp_battery, charging_time)
    val = False
    try:
        cnn = DataBaseManager()
        cnn.connect(3306)
        val = cnn.exec2(insert_rover_sql, tuple)
    except Exception as e:
        print(e)
    finally:
        print(val)
        cnn.close()


def update_rover_sql(rover_id, name_rover, battery_rover, translate_speed, translate_battery, exp_speed, exp_battery,
                         charging_time):
    tuple = (name_rover, battery_rover, translate_speed, translate_battery, exp_speed, exp_battery, charging_time, rover_id)
    val = False
    try:
        cnn = DataBaseManager()
        cnn.connect(3306)
        val = cnn.exec2(update_rover_query, tuple)
    except Exception as e:
        print(e)
    finally:
        print(val)
        cnn.close()


def get_all_rovers(dbm: DataBaseManager):
    try:
        cnn = DataBaseManager()
        cnn.connect(3306)
        cnn.exec(get_rovers_query)
        rovers = cnn.rs.fetchall()
        return rovers

    except Exception as e:
        print(e)
    finally:
        print(':)')
        cnn.close()


def get_rover_by_id(rover_id):
    try:
        cnn = DataBaseManager()
        cnn.connect(3306)
        tuple = (rover_id,)
        cnn.exec2(get_rover_byid_sql, tuple)
        rovers = cnn.rs.fetchall()
        return rovers

    except Exception as e:
        print(e)
    finally:
        cnn.close()

def delete_rover(rover_id):
    val = False
    try:
        cnn = DataBaseManager()
        cnn.connect(3306)
        tuple = (rover_id,)
        val = cnn.exec2(delete_rover_by_id, tuple)
        return val

    except Exception as e:
        print(e)
    finally:
        cnn.close()
