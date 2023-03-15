#! -*- coding:utf-8 -*-
import json
import os

from flask_cors import cross_origin,CORS

from flask import render_template, redirect, flash,url_for, request,Flask,send_from_directory,jsonify
from pathlib import Path
from werkzeug.utils import secure_filename




from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,IntegerField
from wtforms.validators import DataRequired, Length,ValidationError

from datetime import datetime
from flask import flash, redirect, url_for, render_template
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
import pymysql
app = Flask(__name__)

app.config["SECRET_KEY"] = "sss"
app.config.from_object(__name__)
app.config["JSON_AS_ASCII"] = False
UPLOAD_FOLDER = './templates'



app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.jinja_env.trim_blocks = True
app.config["jinja_env.trim_blocks"] = True
app.config["jinja_env.lstrip_blocks"] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost/appbox"
db = SQLAlchemy(app)
# bootstrap = Bootstrap(app)
moment = Moment(app)







class Model():
    def __init__(self):
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='appbox',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

        self.cursor = self.connection.cursor()

    def select_all(self,tablename): # ok
        sql_cmd = " select * from {0} where delete_flg='0';".format(tablename)
        self.cursor.execute(sql_cmd)

        ret = self.cursor.fetchall()
        self.commit()

        return  ret


    def select(self,tablename,param):
        sql_cmd = " select * from {0} where delete_flg='0';".format(tablename)
        self.cursor.execute(sql_cmd)
        ret = self.cursor.fetchall()
        self.commit()

    def insert(self,tablename,param):

        content =param[0]["app_name"],param[0]["app_type"],param[0]["domain"],param[0]["stack"],param[0]["fontport"],param[0]["backendport"]

        sql_cmd = 'insert into {0} (app_name,app_type,domain,stack,fontport,backendport) values (%s,%s,%s,%s,%s,%s)'.format(tablename)
        self.cursor.execute(sql_cmd,content)
        self.commit()

    def update(self,tablename,param):
        pass
    def delete(self,tablename,param):
        # content = (param[0]["id"])
        sql_cmd = 'update  {0} set delete_flg="1" where id={1};'.format(tablename,param)
        self.cursor.execute(sql_cmd)
        self.commit()





    def commit(self):
            self.connection.commit()


    def close(self):

            self.connection.close()




# 因为vue和render_template的模板都是用{{  }}，所以会冲突，将flask的修改为[[  ]]


# 以下代码会影响pygal的加载？ app.jinja_env.variable_start_string = '[['
# 所以得专门把svg作图单独提出来

# yao要用jinja2以下配置不能有
app.jinja_env.variable_start_string = '{['
app.jinja_env.variable_end_string = ']}'



@app.route("/")
@cross_origin()
def top_homepage():
    return render_template("appbox_hp.html")



@app.route("/appbox/api",methods=["GET"])
@cross_origin()
def all_app_info():
    ret = model_instance.select_all("app_info")

    response = jsonify(ret)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


@app.route("/appbox/api",methods=["POST"])
@cross_origin()
def add_app_info():
    # bytes---> str
    request_param = str(request.data,"utf-8")
    response = dict(json.loads(request_param))

    model_instance.insert("app_info", [response])
    return "插入DB success"


@app.route("/appbox/api/<remove_id>", methods=["DELETE"]) #OK
@cross_origin()
def delete_app_info(remove_id):
    model_instance.delete("app_info", str(remove_id))
    return "删除成功"



# # ### 路由管理
if __name__ == '__main__':
    model_instance  = Model()
    app.run(debug=True,port=8003)




#
# -- db:appbox--
# create table app_info (id int not null primary key auto_increment,
# app_name  varchar(255),
# app_type varchar(255),
# domain varchar(255),
# stack  varchar(100),
# fontport  varchar(20),
# backendport  varchar(20),
# delete_flg varchar(1) NOT NULL DEFAULT '0',
# others  varchar(255) not null DEFAULT ''
# ) engine=InnoDB  default charset=utf8;
#
# INSERT INTO app_info (app_name,app_type,domain,stack,fontport,backendport) values("gin-vue-admin","后台管理","gin.vue.admin.itbenyou.com","gin vue","8080","8080");
# INSERT INTO app_info  (app_name,app_type,domain,stack,fontport,backendport) values("go-gin-api","代码生成","go.itbenyou.com","gin vue","8080","8080");
#
#
