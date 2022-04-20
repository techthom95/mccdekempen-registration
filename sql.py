#!/usr/bin/env python3
# sql.py>
import sqlite3

# Define SQL connection
def sql_conn(var):
    try:
        connection = sqlite3.connect(var)
        return connection
    except Exception as e:
        print("[+] SQL ERROR,", e)

# Define SQL command
def sql_command(mysql, var):
    try:
        cursor = mysql.cursor()
        cursor.execute(var)
        mysql.commit()
        return cursor.fetchall()
    except Exception as e:
        print("[+] SQL ERROR,", e)

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
        print("[+] SQL ERROR,", e)

# Define SQL insert
def sql_insert(mysql, table, var1, var2, var3, var4, var5, var6, var7, var8, var9):
    try:
        y = sql_command(mysql, f'SELECT id FROM {table}')
        if y != []:
            id = max(y)[0]+1
        else:
            id = 1
        sql_command(mysql, f'INSERT INTO {table} VALUES ({id}, "{var1}", "{var2}", "{var3}","{var4}", \
                    	    "{var5}", "{var6}", "{var7}", "{var8}", "{var9}")')
    except Exception as e:
        print("[+] SQL ERROR,", e)

def main(var1, var2, var3, var4, var5, var6, var7, var8, var9):
    # Variables
    db = "mysql.db"
    table = "members"
    layout = "(id INTEGER PRIMARY KEY, Lastname VARCHAR(255), Insertion VARCHAR(255), Firstname VARCHAR(255), Address VARCHAR(255), \
             Zip Code VARCHAR(255), Place VARCHAR(255), Nationality VARCHAR(255), E-Mail VARCHAR(255), Date of Birth VARCHAR(255))"

    # Setup connection and connect
    mysql = sql_conn(db)
    print("[+] SQL INFO, Connected to Database", db)

    # Check if table exists, if not, create one
    ck = sql_exists(mysql, table, layout)
    try:
        if ck == 1:
            print("[+] SQL INFO, Database tabel", table, "exists")
        if ck == 2:
            print("[+] SQL INFO, Database tabel", table, "created")
    except Exception as e:
        print("[+] SQL ERROR,", e)

    # Insert values into table
    while ck != 0:
        sql_insert(mysql, table, var1, var2, var3, var4, var5, var6, var7, var8, var9)
        print("[+] SQL INFO, Table Values Injected")
        break

    # Close connection
    mysql.close()