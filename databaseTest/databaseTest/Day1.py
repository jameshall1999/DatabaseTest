from flask import request, jsonify, render_template, flash, url_for, redirect, abort, Response
import sqlite3, json, flask, uuid

connectionString = sqlite3.connect('testtable')
conn= sqlite3.connect('testtable')
cur = conn.cursor()
result = cur.execute('SELECT * FROM company;').fetchall()


#------- Some Commands (UN- COMMENT THEM TO USE THEM)----------------------------------------------------------


sqlStr= """SELECT* FROM company WHERE county='London'ORDER BY company_no"""
conn= sqlite3.connect('testtable')
cur = conn.cursor() 
result = cur.execute(sqlStr).fetchall()
conn.close()
for row in result: 
    print(row)


#-------------------------------------------------------------------------------

# def getData(sqlquery):
#     conn= sqlite3.connect('testtable')
#     cur = conn.cursor()
#     result = cur.execute(sqlquery).fetchall()
#     conn.close()
#     return result

# query = """select *
#     from company"""

# query_result=getData(query)
# for q in query_result:
#     print(q)

# query1='select * from sale'
# query1_result=getData(query1)
# for q in query1_result:
#     print(q)

#---------------------------------------------------------------------------------


# def readData(sql):
#     conn= sqlite3.connect('testtable')
#     cur = conn.cursor() 
#     result = cur.execute(sql).fetchall()
#     conn.close()
#     return result

# res =  readData("SELECT * FROM company WHERE county ='Devon' ")  
# for row in res:        
#     print(row)


#---------------------------------------------------------------------------------