'''
NAME         Abdul Baasit
DATE         3rd November 2020 
DESCRIPTION  File handling and Binary to decimal conversion 
-------------------------------------------------------------------------'''
#Variables--------------------------------------------------------------
shuffledList = r"C:\\lab_week6\\ipaddress_shuffled_list.txt"
shuffledBinList = "C:\\lab_week6\\ipaddress_shuffled_list_bin.txt"
sorted_List =  "C:\\lab_week6\\AB_ipaddress_sorted.txt"
address_list = []
description = "File created by Abdul Baasit\n"
star_format = "*"*50
#---------------------------------------------------------------------
"""---------------------------------------------------------------------------------------------------
Function: get_file_lines_in_list
date : 3rd November 2020 
Author: Fanshawe College
modified : Abdul Baasit
Input arguement: Text(.txt) file
output: list 
Description : removes the next line('\n') escape character from the text file and appends it to a list
---------------------------------------------------------------------------------------------------"""
def get_file_lines_in_list(file):
    line_list=[]
    with open(file,"r") as f: 
        for line in f:
            line_wo_nline = line[:-1] 
            line_list.append(line_wo_nline)
    print("Next line escape character has been removed from ip_address_shuffled_list.txt\n")
    return line_list
#------end-of-get_file_lines_in_list------------------------------------------------------------------------------------------------

"""---------------------------------------------------------------------------------------------------
Function: bin_to_decimal
date : 3rd November 2020 
Input argument: Text(.txt) file
output: list 
Description : 1.removes the next line('\n') escape character from the text file
              2.converts the binary values to decimal
              3.appends it to the list and returns list
---------------------------------------------------------------------------------------------------"""
def bin_to_decimal(file):
    line_list=[]
    temp_str=""
    with open(file,"r") as f: 
        for line in f:
            line_wo_nline = line[:-1]
            line_wo_nline=line_wo_nline.split(".")
            temp_str = "{0}.{1}.{2}.{3}".format(int(line_wo_nline[0],2),int(line_wo_nline[1],2),int(line_wo_nline[2],2),int(line_wo_nline[3],2))
            line_list.append(temp_str)
    print(star_format)
    print("Next line escape character has been removed from ip_address_shuffled_list_Bin.txt\n")
    print(star_format)
    print("Binary to Decimal Conversion Done\n")
    print(star_format)
    return line_list
#------end-of-bin_to_decimal------------------------------------------------------------------------------------------------

"""---------------------------------------------------------------------------------------------------
Function: write_to_file
date : 3rd November 2020 
Input argument: Text(.txt) file,string
output: none
Description : writes the file input string to text file
---------------------------------------------------------------------------------------------------"""  
def write_to_file(file,data_to_be_added):
    with open(file, "w") as f:
        f.write(data_to_be_added)
    print("Done Writing:",description,"\nTo file :",file)
    print(star_format)
#------end-of-write_to_file------------------------------------------------------------------------------------------------

"""---------------------------------------------------------------------------------------------------
Function: append_to_file
date : 3rd November 2020 
Author: Fanshawe College
modified : Abdul Baasit
Input argument: Text(.txt), list
output: none 
Description : Appends the data from list to text file
---------------------------------------------------------------------------------------------------"""
def append_to_file(file,data_to_append):
    with open(file,"a") as f:
        for line in data_to_append:
            f.write(line)
            f.write("\n")
    print("\nDone appending",len(address_list),"ip addresses\nTo file :",file)
    print(star_format)
#------end-of-get_file_lines_in_list------------------------------------------------------------------------------------------------
    
"""---------------------------------------------------------------------------------------------------
Function: get_file_lines_in_list
date : 3rd November 2020 
Author: Abdul Baasit
modified : none
Input argument: Text(.txt) file
output: list 
Description : removes the next line('\n') escape character from the text file and appends it to a list
---------------------------------------------------------------------------------------------------"""
def sort_ipaddress(data_to_sort):
    for i in range(len(data_to_sort)):
        data = data_to_sort[i]
        if data[3] == '1':
            with open("switch_ipaddress.txt","a") as f:
                f.write(data)
                f.write("\n")
        elif data[3] == '2':
            with open("server_ipaddress.txt","a") as f:
                f.write(data)
                f.write("\n")
        else:
            with open("host_ipaddress.txt","a") as f:
                f.write(data)
                f.write("\n")
    print("\nSorting Completed, Please check your Folder for files")
    print(star_format)
#------end-of-get_file_lines_in_list------------------------------------------------------------------------------------------------
    

#--------CODE--EXECUTION-- BEGINS------------------------------------------
address_list= get_file_lines_in_list(shuffledList)
address_list= address_list + (bin_to_decimal(shuffledBinList))#-combining all ip address into a single list
address_list.sort()#-sorting the addresses
write_to_file(sorted_List,description)
append_to_file(sorted_List,address_list)
sort_ipaddress(address_list)
#----------end--of--code---------------------------------------------------