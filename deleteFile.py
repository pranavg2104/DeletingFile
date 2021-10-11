import os
import time

def get_filepaths(directory):
    """Function to store all the available files at the given location"""
    file_paths = []                                             #list to store all the file loaction
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)             #combining the root location passed and the file to get exact address
            file_paths.append(filepath)                         #appending each location into the list

    return file_paths

def get_time(full_file_paths):
    """ Function to store the date and time of file"""
    file_time_path=[]                                           #list to store the date and time of single file
    for i in full_file_paths:
        ti_m = os.path.getmtime(i)                              #getting the last modification timing of a file
        m_ti = time.ctime(ti_m)                                 #used to convert a time expressed in seconds since the epoch to a string representing local time
        t_obj = time.strptime(m_ti)                             #creates a date time object from the above string that is created
        T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)     #formatting date and time in string format
        file_time_path.append(T_stamp)                          #adding the date and time modifiction of file in list
    return file_time_path
    
def delete_file(fileDict2):
    dele=len(fileDict2)-5                                       #keeping the latest 5 file
    for i in range(0,dele):
        os.remove(fileDict2[i][0])                              #deleting older file


full_file_paths=[]                                              #list to store all file location
time_path=[]                                                    #list to store date and time of file
full_file_paths = get_filepaths("D:\Output")                    #call to create list of location of file
time_path=get_time(full_file_paths)                             #call to create list of date and time of file
fileDict={}                                                     #dictonary to store location and date and time
fileDict=dict(zip(full_file_paths,time_path))                   #initializing dictonary location as key and date and time as value
fileDict2={}                                                    #to store sorted file as per date and time modification
fileDict2=sorted(fileDict.items(),key=lambda x: x[1])           #sorting as per value
delete_file(fileDict2)                                          #call to keep 5 recent files and deleting the older 
