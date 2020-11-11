from flask import request, jsonify, render_template, flash, url_for, redirect, abort, Response
import sqlite3, json, flask, uuid

connectionString = sqlite3.connect('testtable')
conn= sqlite3.connect('testtable')
cur = conn.cursor()
result = cur.execute('SELECT * FROM company;').fetchall()


#-------------------------------------Inserting--------------------------------
query = """INSERT INTO company
(company_no,company_name,tel,county,post_code)
VALUES (5000,'QA','0207 888555','TEST!!!!','SE8 5ER')"""
conn= sqlite3.connect('testtable')
cur = conn.cursor() 
cur.execute(query)

conn.commit()
conn.close()

#-------------------------------------------------------------------------------

