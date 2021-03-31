'''
NAME         Abdul Baasit
DATE         10th November 2020 
DESCRIPTION  Modules,Databases 
-------------------------------------------------------------------------'''
import connect_DB
import re
#------------------------------------------------------------------------
"""---------------------------------------------------------------------------------------------------
Function: create_DB
date : 10th November 2020 
Input arguement: none
output: database(.db file)
Description : creates a database
---------------------------------------------------------------------------------------------------"""

def create_DB():
    return Connect_DB.create()
#--------------------------------------------------------------------------------------------------
"""---------------------------------------------------------------------------------------------------
Function: __IsPasswordValid
date : 10th November 2020 
Input arguement: string
output: list
Description : validates the password has one upper case, one lower case, numer value and atleast 8 characters of length
---------------------------------------------------------------------------------------------------"""

def __IsPasswordValid(password):# method not seen in modules that import them. But, developer knows about function could call it
    passwordFlag = True
    if len(password) < 8:
        message ="Password is Too Short" 
        passwordFlag = False
        send = [message,passwordFlag]
        return send        
    elif not re.search("[a-z]",password):
        message ="Password must have atleast one lower case letter" 
        passwordFlag = False
        send = [message,passwordFlag]
        return send
    elif not re.search("[A-Z]",password):
        message ="Password must have atleast one upper case letter" 
        passwordFlag = False 
        send = [message,password]
        return send
    elif not re.search("[0-9]",password):
        message ="Password must have atleast one numeric value" 
        passwordFlag = False 
        send = [message,passwordFlag]
        return send  
    else:
        message ="Password is Valid"
        send =[message,passwordFlag]
        return send
    
#---------------------------------------------------------------------------------
"""---------------------------------------------------------------------------------------------------
Function: Check_user
date : 10th November 2020 
Input arguement: strings
output: list
Description : checks whether username exits in database or not
---------------------------------------------------------------------------------------------------"""
def Check_user(user, password):
    db_result = connect_DB.check_for_user(user)
    
    if db_result == None:
        return [False] # return a list with one element 
    else:
        if db_result[1] != password:
            return [False] # return a list with one element 
    return [True, db_result[2]] # # return a list with two element, True and role 
#----------------------------------------------------------------------------------------------------
"""---------------------------------------------------------------------------------------------------
Function: add_user
date : 10th November 2020 
Input arguement: strings(3)
output: list
Description : adds the user if already doesn't exit and not an admin
---------------------------------------------------------------------------------------------------"""
def add_user(name, password, role):
    checkFlag = connect_DB.check_for_user(name)
    passwordResult = __IsPasswordValid(password)
    if checkFlag or not name:
        message="Username UnAvailable"
        send = [True,message]
        return send        
    if not passwordResult[1]:
        message = passwordResult[0]
        send = [True,message]
        return send
    if role == "Admin" or not role :
        message ="Invalid Role"
        send = [True,message]
        return send
    if (not checkFlag) and (passwordResult[1]) and (role != "Admin"):
        print("Valid Username\n",passwordResult[0],"\nValid Role\n")
        connect_DB.update_users(name,password,role)
        message="{0},{1},{2} has been added".format(name,password,role)
        send = [True, message]
        return send
#--------------------------------------------------------------------------------------
"""---------------------------------------------------------------------------------------------------
Function: get_user_table
date : 10th November 2020 
Input arguement: none
output: prints 
Description : prints all the user in the database
---------------------------------------------------------------------------------------------------"""
def get_user_table():
    users = str(connect_DB.read_all_users())
    yo = connect_DB.read_all_users()
    print(yo)
    #to print in username, password and role format 
    temp=""
    for i in range(len(users)):
        if users[i] == "'" :
            i=i+1
            while users[i] != "'":
                temp += users[i]
                i=i+1
        if i == 21:
            break
    
    li = list(temp.split(","))
    for i in range(len(li)):
        print("username:{},password:{},role:{}\n".format(li[i],li[i],li[i]))
#--------------------------end--of--Code--------------------------------------------------------------------------
                
                
            
    


