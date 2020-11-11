from flask import request, jsonify, render_template, flash, url_for, redirect, abort, Response
import sqlite3, json, flask, uuid

connectionString = sqlite3.connect('testtable')
conn= sqlite3.connect('testtable')
cur = conn.cursor()
result = cur.execute('SELECT * FROM company;').fetchall()

###creating a method####
def getData(sqlquery):
    conn= sqlite3.connect('testtable')
    cur = conn.cursor()
    result = cur.execute(sqlquery).fetchall()
    conn.close()
    print(result)
    return result

###end of the method####
query="""select *
    from company"""

query_result=getData(query)
for q in query_result:
    print(q)