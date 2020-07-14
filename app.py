import os
basedir = os.path.abspath(os.path.dirname(__file__))

import sys
sys.path.append('/usr/lib/python2.7/dist-packages')

import pymysql as mysql
import json
from flask import Flask, request, render_template

'''
run sql to create table

CREATE TABLE `stat` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `host` varchar(256) DEFAULT NULL,
  `mem_free` int(11) DEFAULT NULL,
  `mem_usage` int(11) DEFAULT NULL,
  `mem_total` int(11) DEFAULT NULL,
  `load_avg` varchar(128) DEFAULT NULL,
  `time` bigint(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `host` (`host`(255))
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

'''



app = Flask(__name__)

db = mysql.connect(user="root", passwd="password", db="twitterdb", charset="utf8")
db.autocommit(True)
c = db.cursor()

@app.route("/", methods=["GET", "POST"])
def hello():
    sql = ""
    if request.method == "POST":
        data = request.json
        try:
            sql = "INSERT INTO `stat` (`host`,`mem_free`,`mem_usage`,`mem_total`,`load_avg`,`time`) VALUES('%s', '%d', '%d', '%d', '%s', '%d')" % (data['Host'], data['MemFree'], data['MemUsage'], data['MemTotal'], data['LoadAvg'], int(data['Time']))
            ret = c.execute(sql)
        except mysql.IntegrityError:
            pass
        return "OK"
    else:
        return render_template("mon.html")

@app.route("/data", methods=["GET"])
def getdata():
    c.execute("SELECT `time`,`mem_usage` FROM `stat`")
    ones = [[i[0]*1000, i[1]] for i in c.fetchall()]
    return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))

if __name__ == "__main__":
    app.run(host="localhost", port=8888, debug=True)