import os
import time

def get_filepaths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths

def get_time(full_file_paths):
    file_time_path=[]
    for i in full_file_paths:
        ti_m = os.path.getmtime(i)
        m_ti = time.ctime(ti_m)
        t_obj = time.strptime(m_ti)
        T_stamp = time.strftime("%Y-%m-%d %H:%M:%S", t_obj)
        file_time_path.append(T_stamp)
    return file_time_path
    
def delete_file(fileDict2):
    dele=len(fileDict2)-5
    for i in range(0,dele):
        os.remove(fileDict2[i][0])


full_file_paths=[]
time_path=[]
full_file_paths = get_filepaths("D:\Output")
time_path=get_time(full_file_paths)
fileDict={}
fileDict=dict(zip(full_file_paths,time_path))
fileDict2={}
fileDict2=sorted(fileDict.items(),key=lambda x: x[1])
delete_file(fileDict2)