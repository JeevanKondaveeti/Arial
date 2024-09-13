from flask import Flask,render_template,redirect,request,url_for,flash,session,jsonify
from flask_session import Session
import os
from dbdata import util,util_creation,data_save,admin_Login
dbcreation = util_creation()
dbinfo = util()
##print(dbinfo)
grp_info = dbinfo[0]
admin_user = dbinfo[1]
#print(admin_user)
#print(grp_info)

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
app.secret_key = "E11CD7B8D64CAA25611DD4EE22393"

@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/1',methods=["GET","POST"])
def reg_admin():
    if request.method == 'POST':
        data = dict(request.form)
        email = data['email']
        grp_name = data['Groupname']
        dbinfo = util()
        grp_info = dbinfo[0]
        admin_user = dbinfo[1]
        #print(data)
        for i in admin_user:
            if email == i[2]:
                flash("admin already exist")
                return render_template('adminRegisteration.html')
        for i in  grp_info:
            if grp_name == i[1]:
                flash("grp already exist")
                return render_template('adminRegisteration.html')
        info = ["admin",data]
        #print(data)
        response=data_save(info)
        flash("Admin and Group Registered successfully")
        return redirect(url_for('admin_login'))
    return render_template('adminRegisteration.html')
@app.route('/2',methods=["GET","POST"])
def admin_login():
    if request.method == "POST":
        session.pop('user',None)
        user_data = dict(request.form)
        username = user_data['username']
        passkey = user_data['Password']
        email=admin_Login(username,passkey)
        print(email)
        if email==1:
            session['username']=username
            if not session.get(username):
                session[username]={}
                return redirect(url_for('admin_panel'))
        else:
            flash("Invalid credentials")
            
    return render_template('admin_login.html')

@app.route('/4',methods=['POST','GET'])
def admin_panel():
    if not session.get('username'):
        return redirect(url_for(admin_login))
    else:
        if request.method == 'POST':
            form = request.get_json()
            print(form)
            return jsonify("Love you")
    return render_template('create_form.html')
@app.route('/3', methods=['POST','GET'])
def receive_data():
    if request.method == "POST":
        data = dict(request.form)
        print(data)
# Process the received data
        return jsonify("ok")
    return jsonify(grp_info)


app.run(debug=True,host='localhost',port=1601)