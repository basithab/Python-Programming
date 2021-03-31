'''
NAME         Abdul Baasit
ID           0945195
LAB          3
DATE         13th October 2020 
DESCRIPTION  Formatting,Dates,Datetime module,String formatting,files 
-------------------------------------------------------------------------'''
#builtin-functions------------------------------------------------------
import datetime
import subprocess
#-----------------------------------------------------------------------

#Variables--------------------------------------------------------------
line = '_'*50#to format output
currentDateTime = datetime.datetime.now()# set up for current date
intyear = int(input('Enter year of birth:')) 
intmonth = int(input('Enter month of birth:'))
intdate = int(input('Enter date of birth:'))
intdOB = datetime.datetime(intyear,intmonth,intdate)
# set up for age calculation------------------------------
intdiffer = (str(currentDateTime - intdOB)).split(" ")#subtracting dates and splitting the string by space(" ") to retreive number of days
intage = int(intdiffer[0])/365#converting string to int and dividing it by 365 to convert days into years
#set up pinging website------------------------------------------------------------------------------
strWebsite ="www.google.ca"
intPingCount = input('Number of Pings:')


#Output---------------------------------------------------------------------
print(line)
print("Age:{:.2f}years".format(intage))
print(line)
print("Date:{0}".format(currentDateTime.strftime("%B %d,%Y")))
print(line)
print("Start Time: {0}:{1}:{2}".format(currentDateTime.hour,currentDateTime.minute,currentDateTime.second))
print(line)
subprocess.run(['ping','-n',intPingCount,strWebsite])#pings the website by taking input from the user and displays the output
print(line)
subprocess.run(['netstat'])#executes the netstat command and displays the output
print(line)
#-set up for script execution time-----------------------------------------------------------------------
scriptTime =datetime.datetime.now()#storing the datetime when script has finished executing
print("Time taken for the script to execute:{:.5f}seconds".format((int(scriptTime.strftime("%S%f"))-int(currentDateTime.strftime("%S%f")))/10**6))
print(line)
#----------------------------------------------------------------------------------------
#end of code