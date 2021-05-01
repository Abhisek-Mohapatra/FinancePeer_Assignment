# Finacepeer Coding Assignment

          Name :  Abhisek Mohapatra
          Roll Number : 2020201020
          PG1 M.Tech CSE

Coding Assignment Github Link :
https://github.com/Abhisek-Mohapatra/FinancePeer_Assignment

Video Link :
https://iiitaphyd-my.sharepoint.com/:v:/g/personal/abhisek_mohapatra_students_iiit_ac_in/EX7It2336SZBpxrHFGXi9OgBncapVJnJo-2JhU4_XMjNjw?e=7yMmaB

`NOTE` : If the video cannot be played on sharepoint, kindly download it using download button.
                

# Database used :  
`MySql`
# Back End Files:
`flask_app.py`  : Flask API end-point used for facilitating communication between http requests and database

# Front End Files :
### 6 html files are used (present inside templates folder): 
`index.html`
`insertData.html`
`login.html`
`newuser.html`
`success.html`
`userPage.html` 

These html files contain forms to capture user registration and login information and provide facilities to upload an external json file and are used to display final result in tabular form after data is retrieved from the database.

### 1 css file is used (present inside static/css folder):
`style.css` : It is used for styling the HTML elements like background,buttons,forms etc in a web page.
### 1 javascript file (present inside static/js folder): 
`check.js` : It is used for validation of whether the password and confirm password are same or not while registering a user. If not, an alert box pops up displaying message to enter correct password.

### Dependencies Required: 

a) python3 needs to be installed on the system .

b) Directory structure similar to the code base as present in Github link needs to be maintained.

c) Additional json files needs to be added to the directory where currently marks.json file is present in the code base

d) `MySql` needs to be downloaded from official website.

e)`Flask` needs to be downloaded. On Ubuntu Machines, this can be done by using : `pip3 install -U Flask` in the terminal

f) After Flask is downloaded, we need to install mysql extension. This can be done by using : `pip3 install flask-mysql`. It serves as mysql extension through which mysql database can be accessed using Flask endpoint.

g) In the `flask_app.py`, valid credentials like database name,database password, database username etc need to be replaced with that of the user currently using the mysql database instance . 

In other words,

The following details need to be updated (it is present in `flask_app.py` at the top)

```
app.config['MYSQL_DATABASE_USER'] 
app.config['MYSQL_DATABASE_PASSWORD'] 
app.config['MYSQL_DATABASE_DB'] 
app.config['MYSQL_DATABASE_HOST'] 
```

### Compilation / Execution Formats:

1)  For executing flask_app.py file, open the terminal where flask_app.py file is present:
```
python3 flask_app.py  
```

Then open the link : http://127.0.0.1:5000/ as present on the terminal screen.





























