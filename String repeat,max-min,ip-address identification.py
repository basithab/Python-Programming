# fill your information here
stud_id = "95"
stud_name = "Abdul Baasit" 
    


def repeat_string(word:str, num:int):
    """
    Method should recive a string and an integert. 
    the method returns a string that has the enterd string repeated the 
    number entered. Put a space between the repeated string. See examples below:
    
    >>>repeat_string("London", 3)
    London London London  
    
    >>>repeat_string("Hello", 5)
    Hello Hello Hello Hello Hello
    
    Notice the space between the words
    
    """
    word = word + ' '#adding space    
    return word*num
    



def number_of_cents(change:float): # if entered an integer, ex 20, it will be converted to float, ex 20.00
    """
    Takes in a dollar value including cents and returns the cents in the value entered 
    
    >>> number_of_cents(1.25)
    25
    >>> number_of_cents(20)
    0
    >>> number_of_cents(134.02)
    2
    """
    return int((change - int(change))*100)#subtract and get the decimal part first, then multiply with 100(100cents = 1dollar), then typecast it to integer

        


def max_of_min(num1, num2, num3, num4):
    
    '''
    Method recives 4 numbers. Takes the firsts two(2) and returns minimum. 
    Takes the second two(2) and returns their minimum. takes both minimum numbers and returns maximimum.
    could use min() and max() functions 
    
    Examples:
    
    >>>max_of_min(35, 5.1, 7, 6)
    6
    
    >>>max_of_min(35, 5.1, 5, 6)
    5.1
    '''
    num1 = min(num1,num2)#finding minmum number from group1 and storing it in num1    
    num3 = min(num3,num4)#finding minmum number from group2 and storing it in num3
    return max(num1,num3)#returning max number out of two min numbers
    





def ip_class(ip:str):
    '''
    Function takes in a ip address in string format. 
    Returns which class the IP address belongs too. 
    IP address 8.8.8.8 is Class A
    
    print which class the IP address belongs to
    First Octet:
    class A: 1 to 126
    loopback:127
    clsss B: 128 to 191
    class C: 192 to 223
    
    
    Think how you can split a string. 
    '''
    value = ip.split(".")#splitting the string by "."
    value = int(value[0])#storing the first value into a variable
    if value >= 1 and value <= 126:#checking condtions as per requirement and returning appropriate class
        return "ClASS A"
    elif value == 127:
        return "Loopback"
    elif value >=128 and value <=191:
        return "CLASS B"
    else:
        return "CLASS C"
        
        
    
        
        



def private_IP_address(ip):
    """
    Function takes in a ip address in string format. 
    Returns Private or Public for IP address given. 
    
    private IP address are  
    Private class A is in range 10.0.0.0 through 10.255.255.255
    Private class B is in range 172.16.0.0 through 172.31.255.255
    Private class C is in range 192.168.0.0 through 192.168.255.255
    all other IP Address are public
    
    Think how you can split a string. 
    
    """
    
    value = ip.split(".")#splitting the string by "."
    value0 = int(value[0])#storing the first value into a variable
    value1 = int(value[1])#storing the second value into a variable
    value2 = int(value[2])#storing the third value into a variable
    value3 = int(value[3])#storing the fourth value into a variable
    if value0 == 10 and value1 >=0 and value1 <=255 and value2 >=0 and value2 <=255 and value3 >=0 and value3 <=255:#checking condtions as per requirement and returning whether public or private
        return "Private"
    elif value0 == 172 and value1 >=16 and value1 <=31 and value2 >=0 and value2 <=255 and value3 >=0 and value3 <=255:
        return "Private" 
    elif value0 == 192 and value1 == 168 and value2 >=0 and value2 <=255 and value3 >=0 and value3 <=255:
        return "Private"     
    else:
        return "Public"


 
#Testing repeat_string method 
print("wrtitten by: {0} ID: {1} \n".format(stud_name, stud_id)) #do not change 
print("Testing repeat_string: \n")#do not change 
print("Testing 'London' and 3:\n", repeat_string("London", 3))
print("Testing 'Hello' and 5:\n", repeat_string("Hello", 5))

#create another test of your own
print("Testing 'ABDUL BAASIT' and 7:\n", repeat_string("ABDUL BAASIT", 7))
print("\n---------------------------------------------------------\n")


#Testing max_of_min
print("wrtitten by: {0} ID: {1}\n".format(stud_name, stud_id)) #do not change
print("Testing max_of_min: \n")#do not change 
print("Testing, group 1: 35 & 5.1 amd group 2: 7 & 6. Results: ", max_of_min(35, 5.1, 7, 6))
print("Testing, group 1: 5.1 & 6amd group 2: 25 & 5.11 Results: ", max_of_min(5.1,6, 25, 5.11))

#create another test of your own
print("Testing, group 1: 9.45 & 9.44 and group 2: 2.5 & 2.56 Results: ", max_of_min(9.45,9.44, 2.5, 2.56))
print("\n---------------------------------------------------------\n")

print("wrtitten by: {0} ID: {1}\n".format(stud_name, stud_id)) #do not change
print("testing results: \n")#do not change 
print("Testing 1.25 Results: ", number_of_cents(1.25))
print("Testing 20 Results: ", number_of_cents(20))
print("Testing 134.02 Results: ", number_of_cents(134.02))

#create another test of your own
print("Testing 18.75 NUmber of Cents: ", number_of_cents(18.75))
print("\n---------------------------------------------------------\n")

print("wrtitten by: {0} ID: {1}\n".format(stud_name, stud_id)) #do not change
print("testing ip_class: \n")#do not change 
print("10.25.0.1 is", ip_class("10.25.0.1"))
print("127.25.0.1 is", ip_class("127.25.0.1"))
print("128.25.0.1 is",ip_class("128.25.0.1"))
print("192.32.1.1 is",ip_class("192.32.1.1"))
print("8.8.8.8 is",ip_class("8.8.8.8"))


#create another test of your own
print("172.32.255.255 is",ip_class("172.32.255.255"))
print("\n---------------------------------------------------------\n")

print("wrtitten by: {0} ID: {1}\n".format(stud_name, stud_id)) #do not change
print("testing private_ip_class: \n")#do not change 
print("130.25.0.1 is:", private_IP_address("130.25.0.1"))
print("172.25.0.1 is:", private_IP_address("172.25.0.1"))
print("192.25.0.1 is:", private_IP_address("192.25.0.1"))
print("192.168.0.1 is:", private_IP_address("192.168.0.1"))
print("8.8.8.8 is:", private_IP_address("8.8.8.8"))
print("10.25.0.1 is:", private_IP_address("10.25.0.1"))

#create another test of your own
print("172.32.255.255 is",private_IP_address("172.32.255.255"))
print("\n---------------------------------------------------------\n")