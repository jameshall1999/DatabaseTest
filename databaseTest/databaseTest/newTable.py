from flask import request, jsonify, render_template, flash, url_for, redirect, abort, Response
import sqlite3, json, flask, uuid

connectionString = sqlite3.connect('testtable')
conn= sqlite3.connect('testtable')

#----------------------------CREATES A TABLE CALLED STUDENT, REMEMBER IF YOU HAVE ALREADY CREATED IT, TO DEL IT FIRST OR MAKE A NEW TABLE NAME---------------------

sqlStr2 = """CREATE TABLE Student(
    StudentID TEXT,
    FirstName TEXT,
    Surname   TEXT,
    Course TEXT,
    City TEXT)"""

conn= sqlite3.connect('testtable')
cur = conn.cursor() 
cur.execute(sqlStr2)
conn.commit()
conn.close()

#--------------------------------CHECK IF TABLE EXISTS----------------------------------------

# sqlStr="""

# IF EXISTS(
#     SELECT TABLE_NAME,TABLE_SCHEMA 
#     FROM INFORMATION_SCHEMA.TABLES
#     WHERE TABLE_NAME ='Student'
#     AND TABLE_SCHEMA ='dbo')
# BEGIN
#     DROPTABLE Student 
# END"""