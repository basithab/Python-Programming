
#               This file (Module) deals with database.
#   DATE        FEB 2020
#   ------------------------------------
''' 
If you need to write code, functions, or methods that updates, 
retrives, creates, or delete imformation or tables, 
this is the files to do it.
If need write sql spasific lines this is also the place to write it.
The methods here act as a go between database and rest of the application. 
If need to change database, it could be done here without changing the 
rest of the application or script. 

'''
import sqlite3 #importing module that allows us to connect to general database.

def create():
    '''
    ****Use only if database has been deleted**** 
    Creats a file named logins.db that contains table called users.
    Module also adds a user 'Admin' with password 'Admin'.
    This user will serve as default admin user. 
    '''

    conn = sqlite3.connect('logins.db')
    c = conn.cursor() #creates an instance of the connection to datafile

    #checks to see if there is a table named 'iusers' 
    # returns 1 if there is and 0 if there are no table named 'users'
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users' ''')
    
    #if there is no table users then create it. if there is don't create
    if c.fetchone()[0]==0 :
        c.execute('''CREATE TABLE users (username, password,role)''') # Create table
        # Insert a user for Admin user, in real world use differant name and a harder password 
        c.execute("INSERT INTO users VALUES ('Admin','Admin','admin')")
        
        message = "Table has been created"
    else:
        message = "Table exists already!!!"
    
    # Save (commit) the changes
    conn.commit()
    
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    
    conn.close()
    
    return message
    
#adding users to database
def update_users(e_user,e_password, e_role):
    conn = sqlite3.connect('logins.db')
    c = conn.cursor() #creates an instance of the connection to datafile
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='users' ''')
    
    
    #if there is no table ipaddress then create it. if there is don't creat 
    if c.fetchone()[0]==1 :
        # Insert a row of data
        c.execute("INSERT INTO users VALUES(?,?,?) ",(e_user,e_password,e_role))
        # Save (commit) the changes
        conn.commit()
        #close connection
        conn.close()


'''
function that returns a list of all users with their password and role
''' 
def read_all_users():
    conn = sqlite3.connect('logins.db')
    c = conn.cursor() 
    
    c.execute('SELECT * FROM users')
    
    users = c.fetchall()
    
    conn.close()
    
    return users # returns a list filled with the table information
    
'''
function that reads all the database and prints it to screan
''' 
def check_for_user(user):
    conn = sqlite3.connect('logins.db') #connect to database
    c = conn.cursor() #creats instant 
    t = (user,) # user variable to send to database
    c.execute('SELECT * FROM users WHERE username=?', t) # sql command to get specific user
    
    db_user = c.fetchone() #output of c.execute will be held in user variable, will recieve 'NoneType' if there is no username or 'tuple Type' if finds a user
    
    conn.close()
    
    return db_user #returns either None Type or a tuple Type
