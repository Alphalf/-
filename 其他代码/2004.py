#coding = UTF-8
import json
import sqlite3
import datetime
from flask import Flask, render_template, request
DATABASE = 'data/data.db'
app = Flask(__name__)
@app.route("/")
def hello():
    db = sqlite3.connect(DATABASE)
    cur = db.sursor()
    cur.execute("SELECT * FORM sensorlog WHERE sensorid=1")
    data = cur.fetchall()
    cur.close()
    db.close()
    temp1 = data[-1]
    temp = temp1[2]
    return render_template('vews.html', data=data, temp=temp)
#Adding data
@app.route("/input",methods=['POST','GET'])
def add_data():
    if request.method == 'POST':
        jsonval = json.loads(request.data)
        sensorid = jsonval['id']
        sensorvalue = jsonval['val']
    else:
        sensorid = int(request.args.get('id'))
        sensorvalue = float(request.args.get('val'))
    nowtime = datetime.datetime.now()
    nowtime = nowtime.strftime('%Y-%m-%d %H:%M:%S')
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    
