import secrets
import hashlib
import sys

def login():
    login = input('Login: ')
    pw = input('Password: ').encode()
    salt = None
    HASH = None
    with open('db.txt', 'r') as db:
        for line in db:
            row = line.split(';')
            if row[0] == login:
                salt = row[1].encode()
                HASH = row[2]

    if salt == None or HASH == None:
        print('No such user')
        return

    pw_hash = hashlib.scrypt(password=pw, salt=salt, n=8, r=512, p=4, dklen=32).hex()
    if(HASH == pw_hash):
        print('Welcome')
    else:
        print('Uncorrect password')

def register():
    login = input('Login: ')
    pw = input('Password: ').encode()

    salt = secrets.token_hex(32).encode()
    pw_hash = hashlib.scrypt(password=pw, salt=salt, n=8, r=512, p=4, dklen=32).hex()
    
    with open('db.txt', 'w') as db:
        db.write(login + ';' + salt.decode() + ';' + pw_hash)


while True:
    print('1 -- Login\n2-- Register\n0 -- Exit')
    n = int(input())

    if n == 1:
        login()
    elif n == 2:
        register()
    elif n == 0:
        sys.exit()
    else:
        print('Error...')


