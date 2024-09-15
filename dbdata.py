import mysql.connector
import json
def util():
    with open('dbfile.json') as f:
        data = json.load(f)
    user = data['user']
    password = data['password']
    db = data['db']
    host = data['host']
    mydb = mysql.connector.connect(user=user,password=password,db=db,host=host)
    if mydb.is_connected:
        cursor = mydb.cursor(buffered=True)
        cursor.execute('select * from admin_user')
        admin_user = cursor.fetchall()
        cursor.execute('select * from admin_group')
        grpinfo = cursor.fetchall()
    #print(users[1])
    #print(screens)
        #print("connected")
    else:
        print("Database not connected")
    
    return [grpinfo,admin_user]

def util_creation():
    with open('dbfile.json') as f:
        data = json.load(f)
    user = data['user']
    password = data['password']
    db = data['db']
    host = data['host']
    mydb = mysql.connector.connect(user=user,password=password,db=db,host=host)
    if mydb.is_connected:
        cursor = mydb.cursor(buffered=True)
        cursor.execute('CREATE TABLE IF NOT EXISTS admin_user (a_id INT AUTO_INCREMENT PRIMARY KEY,admin_name VARCHAR(100) UNIQUE,admin_mail VARCHAR(255) UNIQUE,password varbinary(20) not null,created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);')
        mydb.commit()
        print("Admin user table created")
        cursor.execute('CREATE TABLE IF NOT EXISTS admin_group (g_id INT AUTO_INCREMENT PRIMARY KEY,group_name VARCHAR(100) UNIQUE,a_id INT,FOREIGN KEY (a_id) REFERENCES admin_user(a_id));')
        mydb.commit()
        print("Admin_group table created")
        cursor.execute('Create table IF NOT EXISTS grp_user (u_id INT AUTO_INCREMENT PRIMARY KEY,user_name VARCHAR(50),dob DATE,phone_number varchar(10),g_id int,a_id int,FOREIGN KEY(g_id) REFERENCES admin_group(g_id),FOREIGN KEY(a_id) REFERENCES admin_user(a_id));')
        mydb.commit()
        print("Group users table created")
        cursor.execute('CREATE TABLE IF NOT EXISTS screens (s_id int auto_increment primary key,screen_name varchar(50) unique,screen_path varchar(500));')
        mydb.commit()
        print("Screens table created")
        cursor.execute('CREATE table if not exists grp_screen(g_id int,s_id int,Foreign key(g_id) references admin_group(g_id),Foreign key(s_id) references screens(s_id));')
        mydb.commit()
        print("grp_screens created")

def data_save(info): 
    with open('dbfile.json') as f:
        data = json.load(f)
    user = data['user']
    password = data['password']
    db = data['db']
    host = data['host']
    mydb = mysql.connector.connect(user=user,password=password,db=db,host=host)
    cursor = mydb.cursor(buffered=True)
    #admin_user(admin_name,admin_mail,password,),admin_group(group_name)
    registration = info[0]
    match registration:
        case "admin":
            data = info[1]
            print(data)
            admin_name = data['username']
            email = data['email']
            grp_name = data['Groupname']
            pword = data['Password']
            admin_reg=cursor.execute(
                    'insert into admin_user (admin_name,admin_mail,password) values (%s,%s,%s)',
                    [admin_name,email,pword]
                    )
            #print(admin_reg)
            mydb.commit()
            cursor.execute('select a_id from admin_user where admin_mail=%s',[email])
            aid = cursor.fetchone()[0]
            admingroup=cursor.execute(
                    'insert into admin_group (group_name,a_id) values (%s,%s)',
                    [grp_name,aid]
                    )
            #print(admingroup)
            mydb.commit()
            print("registering admin and adding group")
            return 1
        case "grp_user":
            print("Registering user to group")
        case "grp_screen":
            print("adding screens to group")
def admin_Login(username,passkey):
    with open('dbfile.json') as f:
        data = json.load(f)
    user = data['user']
    password = data['password']
    db = data['db']
    host = data['host']
    mydb = mysql.connector.connect(user=user,password=password,db=db,host=host)
    cursor = mydb.cursor(buffered=True)
    if mydb.is_connected:
        cursor = mydb.cursor(buffered=True)
        cursor.execute('select admin_mail,admin_name,password from admin_user where admin_name=%s',[username])
        admin_mail,user,pass_word = cursor.fetchone()
        pass_word = pass_word.decode('utf-8')
        if username == user and passkey == pass_word:
            return 1
        else:
            return 0
        
   
def screen(screen,filepath):
    with open('dbfile.json') as f:
        data=json.load(f)
    user = data['user']
    password = data['password']
    db = data['db']
    host = data['host']
    mydb = mysql.connector.connect(user=user,password = password,db=db,host=host)
    if mydb.is_connected:
        cursor = mydb.cursor(buffered=True)   
        cursor.execute('select * from screens') 
        screensinfo = cursor.fetchall()
        print(len(screensinfo))
        if len(screensinfo) == 0:
            cursor.execute('insert into screens (screen_name,screen_path) values (%s,%s)',[screen,filepath])
            mydb.commit()

        
        
    
