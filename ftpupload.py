import sys
import os
import ftplib


def main():
    global helpNeeded
    global user
    global password
    global server
    global nopics
    global path
    global port
    port = 21
    helpNeeded = False
    path = '/public_html'
    nopics = False
    for i,o in enumerate(sys.argv):
        if(o == '--user' or o == '-u'):
            user = sys.argv[i+1]
        elif(o == '--password' or o == '-p'):
            password = sys.argv[i + 1]
        elif (o == '--server' or o == '-s'):
            server = sys.argv[i + 1]
        elif (o == '--nopics'):
            nopics = True
        elif (o == '--path'):
            path = sys.argv[i + 1]
        elif (o == '-h' or o == '--help'):
            helpNeeded = True
        elif (o == '--port'):
            port = sys.argv[i + 1]
    if(helpNeeded):
        print('This is a script for uploading an entire folders contents to a specfied FTP server')
        print('The script does not upload itself or any .git files')
        print('To use the script you must use flags, to use a flag type the flag then a space and then the requires information, the three requires flags are as follows:')
        print('The --server or -s flag must go before the server IP')
        print('The --user or -u flag must go before the user name')
        print('The --password or -p flag must go before the password')
        print('The --port flag can be used to specify a port, it defaults to port 21')
        print('Use the --path flag to specify a path to upload the file to on the server')
        print('you can also use the --nopics flag to skip an .jpeg, .jpg, and .png files')
    try:
        server
    except NameError:
        print("server is not defined, it can be defined with the -s flag")
        print('use the -h flag for help')
        exit(1);
    try:
        password
    except NameError:
        print("password is not defined, it can be defined with the -p flag")
        print('use the -h flag for help')
        exit(1);
    try:
        user
    except NameError:
        print("user is not defined, it can be defined with the -u flag")
        print('use the -h flag for help')
        exit(1);


def upload():
    global server
    global password
    global user
    global nopics
    global path
    global port
    for filename in os.listdir(os.getcwd()):
        ftp = ftplib.FTP_TLS()
        ftp.connect(server, port)
        try:
            name, ext = os.path.splitext(filename)
            if(not filename == 'ftpupload.py' or not ext == ".git"):
                if(not (nopics and (ext == '.png' or ext == '.jpg' or ext == '.jpeg'))):
                    print("uploading: "+filename)
                    ftp.login(user, password)
                    ftp.cwd(path)
                    file = open(filename, 'rb')
                    ftp.storbinary('STOR '+filename, file)
                    file.close()
        except:
            "failed to login"
main()
upload()
