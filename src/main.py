#! /usr/bin/env python3


__author__ = 'foxtrot_charlie'
__version__ = '0.0.1a'

# This is a vulnerable pastebin implementation for XSS training
# Prepared for Devskiller Sp. z.o.o.
# The vulnerability is marked by the comment so please do NOT report it
# Sessions and data are stored in the memory to simplify the application.
# THIS IS NOT MEANT TO BE USED ON ANY PRODUCTION ENVIRONMENT !!!EVER!!!


from flask import Flask, render_template, request, redirect, \
    url_for, flash, make_response, session, abort
import functools
import os
import base64
import uuid
import sqlite3
from faker import Faker

app = Flask(__name__, template_folder='templates')


_DB_NAME_ = 'db.sqlite3'
_FLAG_ = r'DevSkill{SqL1_1s_5t1ll_4_th1ng_s4dly_1337}'
fake = Faker()


def db_init():
    print("== Building DB ==")
    if os.path.isfile(_DB_NAME_):
        os.remove(_DB_NAME_)

    con = sqlite3.connect(_DB_NAME_)
    cur = con.cursor()

    print("== CREATING TABLES ==")

    cur.execute("CREATE TABLE IF NOT EXISTS people (person_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, address TEXT NOT NULL);")
    cur.execute("CREATE TABLE IF NOT EXISTS data (flag_id INTEGER PRIMARY KEY AUTOINCREMENT, val TEXT NOT NULL);")

    print("== GENERATING DATA ==")

    for i in range(100):
        fname = fake.name()
        faddr = fake.address()

        cur.execute("INSERT INTO people (name, address) VALUES (?, ?);", (fname, faddr))

    cur.execute("INSERT INTO data (val) VALUES (?)", (_FLAG_,))


    print("== DB GENERATED ==")
    con.commit()
    con.close()



@app.route('/')
def main():
    query = request.args.get("q", None)
    try:
        if query is None:
            return render_template('index.html')

        else:
            con = sqlite3.connect(_DB_NAME_)
            cur = con.cursor()

            sql_query = "SELECT * from people WHERE name LIKE UPPER('%" + query + "%');"  # ;)
            print(sql_query)

            cur.execute(sql_query)

            rows = cur.fetchall()

            return render_template('index.html', result=rows)
    except Exception:
        return render_template('error.html')





if __name__ == '__main__':
    db_init()
    app.secret_key = base64.b64encode(os.urandom(40)).decode('utf-8')  # again this app is not secure at all
    app.run(host="0.0.0.0", port=5000)
