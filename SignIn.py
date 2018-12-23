import time

time = time.asctime()
def AddUser():
    username = raw_input(' Username : ')
    if username == "clear all users":
        file = open('Users.txt','w')
        file.write('')
        file.close()
        log = open('Logs.txt','a')
        log.write('[ ! ] '+'ALL USERS HAS BEEN DELETED ! '+' Time ['+time+']'+'\n')
        log.close()
        exit()
    if username == "clear all logs":
        logcl = open('Logs.txt','w')
        logcl.write('')
        logcl.close()
        exit()
    password = raw_input(' Password : ')
    f = open('Users.txt','a')
    f.write(username+' : '+password+'\n')
    f.close()
    logs = open('Logs.txt','a')
    logs.write('# '+username+' '+'ADDED Successfully !'+' Time ['+time+']'+'\n')
    logs.close()

AddUser()
