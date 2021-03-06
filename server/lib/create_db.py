#!/usr/bin/python3

import sqlite3


def create_db(DB_FILE, TABLE):
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute(
            f"""CREATE TABLE IF NOT EXISTS {TABLE} (
                time text,
                mcc integer,
                mnc integer,
                lac integer,
                cell_id integer,
                rxl integer,
                arfcn text,
                bsic text,
                lat float,
                lon float,
                satellites integer,
                GPS_quality text,
                altitude float,
                altitude_units text,
                PRIMARY KEY (time, mcc, mnc, lac, cell_id)
            );""")
        c.execute(
            """CREATE TABLE IF NOT EXISTS towers (
                id PRIMARY KEY,
                est_lat float,
                est_lon float
                in_db boolean,
                lat float,
                lon float,
                delta float,
                range integer,
                radio_type integer
            );""")
        conn.commit()
        conn.close()
    except Exception as e:
        log.error(f'failed to connect to db: {e}')