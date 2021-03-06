import paramiko
import getpass
import telnetlib
from ftplib import FTP

def sshconnect():

    IpAddress = input("Enter the ip address:")
    user = input("Enter the username:")
    passwrd = input("Enter the password:")
    port = 22
    command = input("Enter your command:")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(IpAddress, port, user, passwrd)
    stdin, stdout, stderr = ssh.exec_command(command)
    lines = stdout.readlines()

    print(lines)

def telnetconnect():

    IpAddress = input("Enter the ip address:")
    user = input("Enter the username:")
    passwrd = input("Enter the password:")
    # command = bytes(input("Enter your command:"), 'ascii')
    # res = bytes(command, 'utf-8') 
    # please ignore these commented variables will work on them later
    tn = telnetlib.Telnet(IpAddress)

    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if passwrd:
        tn.read_until(b"Password: ")
        tn.write(passwrd.encode('ascii') + b"\n")

    tn.write(b"ls") #Put your command here, will work on a proper user input later
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))

def ftpconnect():
    ipadd = input("Enter IP address:")
    user = input("Enter the username:")
    passwrd = input("Enter the password:")
    ftp = FTP(ipadd)
    ftp.login(user, passwrd)
    # add your commands here this is a basic FTP connection you can add your own commands after this
    # visit https://docs.python.org/3/library/ftplib.html for further commands

if __name__ == "__main__":
    print("\n Please select a option: \n 1. SSH \n 2. Telnet \n 3. FTP")
    option = int(input("Option:"))
    if option == 1:
        sshconnect()
    elif option == 2:
        telnetconnect()
    elif option == 3:
        ftpconnect()
    else:
        print("Wrong option, terminating")

