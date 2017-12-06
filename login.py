import MySQLdb
from flask import Flask, render_template,request,redirect,make_response

application = Flask(__name__)

@application.route('/')


#ログイン画面を表示する
@application.route('/login')
def show_new():

    #ログイン画面を表示する
    return render_template('login.html')

#ログイン処理
@application.route('/login', methods = ['POST'])
def login():

    #�܂���form�̒l�����A�{�����擾����
    scr_id = request.form['userid']
    scr_pw = request.form['password']

    #mysql�ɐڑ�����
    db = MySQLdb.connect( user='root', passwd='ym71125326', host='localhost', db='myapp', charset='utf8')
    con = db.cursor()

    #�擾�����^�X�N�̓��e��todo�e�[�u���ɒǉ�����
    sql = 'select login_pw from users where login_id = %s'
    con.execute(sql,[scr_id])
    #�l��2�����z���Ŏ擾�B
    result = con.fetchone()

    #DB�̐ؒf
    db.close()
    con.close()

    if result == None:
        result_flg ='1'
        msg = 'IDが登録されていません。'
        print ("------")
        print (result_flg)
    else:
        db_pw = result[0]
        if db_pw == scr_pw:
            result_flg ='0'
            print ("------")
            print (result_flg)
        else:
            result_flg ='1'
            msg = 'パスワードが違います。'
            print ("------")
            print (result_flg)


    print ("------")
    print (scr_id)
    print ("------")
    print (scr_pw)
    print ("------")
    print (result)
    print ("------")
    print (db_pw)
    print ("------")


    if result_flg == '0':
        #ブラウザにcookie保存
        html = redirect('http://localhost:8080/index')
        resp = make_response(html)
        resp.set_cookie('login_id', scr_id)

        return resp
    else:
        html = render_template('login.html', err_msg=msg)
        return html
