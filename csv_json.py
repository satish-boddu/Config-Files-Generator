import json
import pandas as pd
import math
import numpy as np
from isstring import isstring
from ast import literal_eval
#********************************************************

#WORKS TO DO WITH THIS FILE

    #1) Comment the Code                   DONE B|

    #2) Convert the int64 to float(temp)   DONE :D
    #3) Convert the float(temp) to int     DONE B|
    #4) Skip 2) and 3) and do it directly  DONE xD

    #5) Make sure to check for Lists       DONE :D

    #6) Accounting for the empty spaces    DONE ^_^

#********************************************************

#Reading the CSV File and gathering the Data

csv_data = pd.read_csv("config_tobegenerated.csv")
csv_data = csv_data.set_index('filename')        #Setting the Filename to be the Index
                    

# Index and Keys in the form of a List to use for Retrieving Information
index = (csv_data.index.tolist())                  #All the files names in a List                   
keys = (csv_data.columns.values.tolist())


#******************#*****************#*******************#
                 #   TEST SPACE   #



#******************#******************#******************#
                 #   WORKING CODE  #


#Function used for converting the type for numeric values to "int"
#The correct format that can be read by JSON files
def convert_int(val):
    try:
        return int(val)
    except ValueError:
        return np.nan

#Function to check for Empty spaces, An Empty space is a floating point number "nan"
#to convert the floating point number to the right format to check for empty spaces
def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


# Retrieving Information from the CSV and Forming the JSON Config Files
for i in range (len(index)):   #This loop runs for every row in the CSV File hence creating a seperate JSON File for each
    json_dict = {}                                               #Empty dict that will contain the JSON data
    for x in keys:
        single_data = (csv_data.iloc[[i]])  #Taking the Pandas DataFrame of Information for the single file being created

        
        #Checking the Recieved Data in Cases: First Case with Strings
        #Checking every Column (Key) and updating the JSON file with the right type
        if isstring(single_data.ix[0,x]):

            if isFloat((single_data.ix[0,x])):
                if math.isnan((single_data.ix[0,x])):
                    continue

            else:
                    #Checking Cases: First Case for Lists
                if (single_data.ix[0,x])[0] == '[':
                    list_data = single_data.ix[0,x]

                    #_____Removing any extra characters_______#
                    list_data = list_data.replace("\"", "").replace("\'", "").replace(" ", "")
                    #_________________________________________#

                    list_data = list_data[1:-1].split(',')
                    json_dict[x] = list_data

                #Checking Cases: Rest of the Strings
                else:
                    json_dict[x] = single_data.ix[0,x].replace("\"", "").replace("\'", "")

        #Assuming if not string then it will be Numeric based on given samples        
        else:
            data = single_data.ix[0,x]
            data = convert_int(data)
            json_dict[x] = data




    File_Name = index[i] + ".json"                               #Write the file name for the config file
    with open(File_Name, 'w') as outfile:  
        json.dump(json_dict, outfile, indent = 4)                #Open and Add the data into the Config File


print ("Compeleted making the Config(JSON) Files")































# Converting the Numbers obtained from the CSV File to float temporarily to 
# add on the to JSON File
'''
for x in keys:
    if (csv_data[x].dtype == 'int64'):
        csv_data[x] = csv_data[x].astype(float) 
'''

























#Version 1 (Vertical Keys and Values)


'''
for data in csv_data['Key']:  
    Keys.append(data)              #Filling in Keys

for data in csv_data['Value']:
    Values.append(data)            #Filling in Values

for x in range(len(Keys)):          #Forming the Data Dictionary
    json_dict[Keys[x]] = Values[x]

#********************************************************
#********************************************************

#Creating and Adding the Data to a JSON File

File_Name = input("Enter the name of the file: ") + ".json"  #Write the file name for the config file
with open(File_Name, 'w') as outfile:  
    json.dump(json_dict, outfile, indent = 4)                #Open and Add the data into the Config File

print ("Config(json) File Created Successfully")

'''