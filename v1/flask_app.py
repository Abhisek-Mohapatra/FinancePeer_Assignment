from flask import Flask,render_template,request
from flaskext.mysql import MySQL
import secrets
import json


secret_key = secrets.token_hex(16)


mysql = MySQL()
app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = "Baba@1234"
app.config['MYSQL_DATABASE_DB'] = 'usersDb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)



@app.route('/',methods=['GET','POST'])
def index():
   if request.method=='POST':
      name=request.form['uname']
      username=request.form['userName']
      passw=request.form['userPassword']

      conn=mysql.connect()
      cur=conn.cursor()

      cur.execute('INSERT INTO USERS VALUES(%s,%s,%s)',(name,username,passw))
     

      conn.commit()

      cur.close()

     
      return render_template('index.html')

   return render_template('index.html')

@app.route('/newuser.html',methods=['GET','POST'])
def newuser():
   return render_template('newuser.html')

@app.route('/login.html',methods=['GET','POST'])
def login():

   return render_template('login.html')


@app.route('/success.html',methods=['GET','POST'])
def success():

   if request.method=='POST':

      username=request.form['userName']
      passw=request.form['userPassword']

      conn=mysql.connect()
      cur=conn.cursor()

      cur.execute("SELECT * FROM USERS where Username='"+username+"' and Password='"+passw+"'")  # For Selection
      r=cur.fetchall()
      count=cur.rowcount
      cur.close()

      if count==0:
         error = "No such login credentials exist..."
         return error
      elif count==1:
         return render_template('success.html',username=username)
      else:
         return "More than 1 credentials present..."


   return render_template('success.html')



@app.route('/insertData.html', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['upfile']

      fin=open(f.filename,'r')
      content_lst=json.loads(fin.read())

      conn=mysql.connect()
      cur=conn.cursor()

      for dc in content_lst:  # list of dictionaries

         userId=str(dc["userId"])
         uid=str(dc["id"])
         title=dc["title"]
         body=dc["body"]

         cur.execute('INSERT INTO USER_DATA VALUES(%s,%s,%s,%s)',(userId,uid,title,body))
     
         conn.commit()

      cur.close()
      msg='Data successfully inserted into database from json file...'

      return render_template('insertData.html',msg=msg)


@app.route('/userPage.html', methods = ['GET', 'POST'])
def getData():
   if request.method == 'POST':

      conn=mysql.connect()
      cur=conn.cursor()

      users=cur.execute("SELECT * FROM USER_DATA")  # For Selection

      if users>0:

         userData=cur.fetchall()
         cur.close()
         return render_template('userPage.html',userData=userData)
      
      



      










      # f.save(secure_filename(f.filename))
      # return 'file uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug=True)

