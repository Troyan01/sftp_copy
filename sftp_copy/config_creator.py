import configparser

config = configparser.ConfigParser()

config.add_section('credentials')
config.set('credentials','host','192.168.0.5')
config.set('credentials','port','22')
config.set('credentials','username','Dell')
config.set('credentials','password','123')


config.add_section('path')
config.set('path','local_dir',r'C:\Users\User\Desktop\ftp')
config.set('path','remote_dir',r'C:\Users\Dell\Desktop\ftp')


config.add_section('mode')
config.set('mode','mode','copy')
config.set('mode','timesleep','15')


with open(r"C:\Users\User\source\repos\sftp_copy\sftp_copy\configfile.ini", 'w') as configfile:
    config.write(configfile)