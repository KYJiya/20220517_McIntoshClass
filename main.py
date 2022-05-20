import os
import ftplib
from datetime import datetime


now = datetime.now()


def ftp_download(file_from, file_to, fail_list):
    url = "ftp.swpc.noaa.gov"

    ftp = ftplib.FTP(url)
    ftp.login()
    fp = file_open(file_to)
    try:
        ftp.retrbinary("RETR " + file_from, fp.write)
    except:
        fp.close()
        os.remove(file_to)

        fail_directory, fail_file = os.path.split(fail_list)
        makedirs(fail_directory)
        fail_file = open(fail_list, "a")
        fail_file.write(file_from + "\n")
        fail_file.close()


def file_open(file_to):
    directory, file = os.path.split(file_to)
    makedirs(directory)
    fp = open(file_to, "wb")

    return fp


def makedirs(directory): 
    try: 
        os.makedirs(directory) 
    except OSError: 
        if not os.path.isdir(directory): 
            raise   


if __name__=="__main__":
    file_from = f"pub/warehouse/{now.year}/SRS/{now.strftime('%Y%m%d')}SRS.txt"
    fail_list = f".fail_list/fail_list.txt"
    
    if os.path.isfile(fail_list):
        fail_directory, fail_file = os.path.split(fail_list)
        fail_file = open(fail_list, "r")
        fail_files = fail_file.readlines()
        fail_file.close()
        os.remove(fail_list)
        fail_files.append(file_from)
        for k in fail_files:
            k = k.strip('\n')
            ftp_download(k, k, fail_list)
    else:
        ftp_download(file_from, file_from, fail_list)