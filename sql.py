#!/usr/bin/env python3
# sql.py>
import sqlite3

# Define SQL connection
def sql_conn(var):
    try:
        connection = sqlite3.connect(var)
        return connection
    except Exception as e:
        print("ERROR,", e)

# Define SQL command
def sql_command(mysql, var):
    try:
        cursor = mysql.cursor()
        cursor.execute(var)
        mysql.commit()
        return cursor.fetchall()
    except Exception as e:
        print("ERROR,", e)

# Define SQL table exists
def sql_exists(mysql, table, layout):
    try:
        y = sql_command(mysql, f'SELECT name FROM sqlite_master')
        x = 0
        if y != []:
            for i in y:    
                if i[0] == table:
                    x = 1
                    break
        if x == 0:
            sql_command(mysql, f'CREATE TABLE {table} {layout};')
            x = 2
        return x
    except Exception as e:
        print("ERROR,", e)

# Define SQL insert
def sql_insert(mysql, table, var1, var2, var3):
    try:
        y = sql_command(mysql, f'SELECT id FROM {table}')
        if y != []:
            id = max(y)[0]+1
        else:
            id = 1
        sql_command(mysql, f'INSERT INTO {table} VALUES ({id}, "{var1}", "{var2}", "{var3}")')
    except Exception as e:
        print("ERROR,", e)

def main(first, last, pin):
    db = "mysql.db"
    table = "register"
    layout = "(id INTEGER PRIMARY KEY, first VARCHAR(255), last VARCHAR(255), pin INTEGER)"

    mysql = sql_conn(db)
    print("Connected to Database", db)

    ck = sql_exists(mysql, table, layout)
    try:
        if ck == 1:
            print("Database tabel", table, "exists")
        if ck == 2:
            print("Database tabel", table, "created")
    except Exception as e:
        print("ERROR,", e)

    while ck != 0:
        sql_insert(mysql, table, first, last, pin)
        print("Table Values Injected")
        break

    mysql.close()