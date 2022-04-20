#!/usr/bin/env python3
# sql.py>
import sys, sqlite3
from configparser import *

# Define configuration
def config():
    try:
        config = ConfigParser()
        config.read("config.ini")
        var1 = config["SQL"]["database"]
        var2 = config["SQL"]["table"]
        var3 = config["SQL"]["layout"]
        return var1, var2, var3
    except Exception as e:
        print("[+] SQL ERROR,", e)
        return -1

# Define SQL connection
def sql_conn(var):
    try:
        connection = sqlite3.connect(var)
        return connection
    except Exception as e:
        print("[+] SQL ERROR,", e)
        return -1

# Define SQL command
def sql_command(mysql, var):
    try:
        cursor = mysql.cursor()
        cursor.execute(var)
        mysql.commit()
        return cursor.fetchall()
    except Exception as e:
        print("[+] SQL ERROR,", e)
        return -1

# Define SQL table exists
def sql_exists(mysql, table, layout):
    try:
        y = sql_command(mysql, f'SELECT name FROM sqlite_master')
        if y == -1:
            sys.exit()
        x = 0
        if y != []:
            for i in y:    
                if i[0] == table:
                    x = 1
                    break
        if x == 0:
            if sql_command(mysql, f'CREATE TABLE {table} {layout};') == -1:
                sys.exit()
            x = 2
        return x
    except Exception as e:
        print("[+] SQL ERROR,", e)
        return -1

# Define SQL insert
def sql_insert(mysql, table, var1, var2, var3, var4, var5, var6, var7, var8, var9):
    try:
        y = sql_command(mysql, f'SELECT id FROM {table}')
        if y == -1:
            sys.exit()
        if y != []:
            id = max(y)[0]+1
        else:
            id = 1
        if sql_command(mysql, f'INSERT INTO {table} VALUES ({id}, "{var1}", "{var2}", "{var3}","{var4}", \
                    	    "{var5}", "{var6}", "{var7}", "{var8}", "{var9}")')== -1:
            sys.exit()
    except Exception as e:
        print("[+] SQL ERROR,", e)
        return -1

def main(var1, var2, var3, var4, var5, var6, var7, var8, var9):
    # Read configuration
    db = config()[0]
    table = config()[1]
    layout = config()[2]
    if db == -1 or table == -1 or layout == -1:
        sys.exit()

    # Setup connection and connect
    mysql = sql_conn(db)
    if mysql == -1:
        sys.exit()
    print("[+] SQL INFO, Connected to Database", db)

    # Check if table exists, if not, create one
    ck = sql_exists(mysql, table, layout)
    if ck == -1:
        sys.exit()
    try:
        if ck == 1:
            print("[+] SQL INFO, Database tabel", table, "exists")
        if ck == 2:
            print("[+] SQL INFO, Database tabel", table, "created")
    except Exception as e:
        print("[+] SQL ERROR,", e)
        return -1

    # Insert values into table
    while ck != 0:
        if sql_insert(mysql, table, var1, var2, var3, var4, var5, var6, var7, var8, var9) == -1:
            sys.exit()
        print("[+] SQL INFO, Table Values Injected")
        break

    # Close connection
    mysql.close()