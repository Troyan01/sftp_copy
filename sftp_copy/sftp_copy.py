
import paramiko
import stat
import os
import configparser
import time
 
def create_sftp_client(host, port, username, password):
    ssh_client = paramiko.SSHClient()
  
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host,port=port,username=username,password=password)

    sftp_client = ssh_client.open_sftp()
    return sftp_client

def upload_file_to_server(sftp_client, local_file, remote_file):
    sftp_client.put(local_file, remote_file)
    
def copy_dirictory(local_dir, remote_dir,sftp_client):
    files = os.listdir(path = local_dir)
    for file in files:
        all_path = local_dir+"\\"+file
        attr = os.stat(all_path)
        if attr.st_file_attributes & stat.FILE_ATTRIBUTE_ARCHIVE: 
            upload_file_to_server(sftp_client, all_path, remote_dir+"\\"+file)
            os.system(f"attrib -a  {all_path}")
            print (f"File {file} was copy")
        

def move_dirictory(local_dir, remote_dir,sftp_client):
    files = os.listdir(path = local_dir)
    for file in files:
        all_path = local_dir+"\\"+file
        upload_file_to_server(sftp_client, all_path, remote_dir+"\\"+file)
        os.remove(all_path)
        print (f"File {file} was remove")


config_obj = configparser.ConfigParser()
config_obj.read("./configfile.ini")

creds = config_obj['credentials']
path = config_obj['path']
mode = config_obj['mode']

host = creds['host']
port = creds['port']
username = creds['username']
password = creds['password']
local_dir = path['local_dir']
remote_dir = path['remote_dir']
spec = mode['mode']
timesleep =int( mode['timesleep'])

print("Configured \nTry conected..")
sftp_client = create_sftp_client(host, port, username, password)

print(f"Connected to {host}")
if spec == 'copy': 
    while(1):
        copy_dirictory(local_dir,remote_dir,sftp_client)
        time.sleep(timesleep)
        
    
elif spec == 'move': 
    while(1):
        move_dirictory(local_dir,remote_dir,sftp_client)
        time.sleep(timesleep)
    
else : print("Unknow mode")
print("End programm")
input()
sftp_client.close()