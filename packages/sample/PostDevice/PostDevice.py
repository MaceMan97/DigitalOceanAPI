from decimal import Decimal
from datetime import datetime, date, timedelta

import mysql.connector

def main(args):
    ip = args.get("ip")

    db = mysql.connector.connect(host="db-mysql-nyc1-26755-do-user-12703804-0.b.db.ondigitalocean.com",    # your host, usually localhost
                        user="doadmin",         # your username
                        passwd="AVNS_g4jCamCIzl2BLw9goTB",  # your password
                        db="defaultdb")        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT * FROM Devices")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print(row[0])

    db.close()

    return {"ip": ip}