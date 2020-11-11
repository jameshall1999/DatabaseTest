from flask import request, jsonify, render_template, flash, url_for, redirect, abort, Response
import sqlite3, json, flask, uuid

connectionString = sqlite3.connect('testtable')
conn= sqlite3.connect('testtable')
cur = conn.cursor()
result = cur.execute('SELECT * FROM company;').fetchall()