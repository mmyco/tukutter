import MySQLdb
from flask import Flask, render_template,request,redirect,make_response

application = Flask(__name__)

@application.route('/')


#インデックス画面を表示する
@application.route('/index')
def show_new():
    user_id = request.cookies.get('id',None)
    print ('---------')
    print (user_id)
    print ('---------')
    
    #インデックス画面を表示する
    return render_template('index.html')

#インデックス処理
