import os
import ftplib
from datetime import datetime


now = datetime.now()


def ftp_download(file_from, file_to):
    url = "ftp.swpc.noaa.gov"

    ftp = ftplib.FTP(url)
    ftp.login()
    # file_ok = ftp.nlst(file)
    fp = file_open(file_to)
    ftp.retrbinary("RETR " + file_from, fp.write)


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
    ftp_download(file_from, file_from)