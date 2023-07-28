'''
This code which check is the user have an account or not
This will be used during sign-in process
'''

import hashlib
import mysql.connector as sqltor

username = input("Enter username:")
ch = True
while ch == True:
    password = input("Enter password:")
    confirm_password = input("Enter password:")
    if(password==confirm_password): #Cheking if password is matching or not
        print()

        '''
        Converting password to hash
        '''

        sha521 = hashlib.sha512()
        sha521.update(password)
        hash_sha521 = sha521.hexdigest()

        '''
        Conneting to MySQL:
            host : localhost
            username : <username>
            password : <password>
            database : <website_name>
        '''

        mycon = sqltor.connect(host='localhost',username='<username>',password='<password>',database='<website_name>')
        cursor = mycon.cursor()
        
        data = cursor.fetchall()
        for row in data:
            if (username in row):
                if (hash_sha521 in row):
                    print('Login Successfully!')
                else:
                    print("Incorrect password!")
                    ch = True
            else:
                print("Username doesn't exist!")
                ch = True
        mycon.close()

        ch = False
        break
    else:
        print("Password doesn't match!") #Error message
        ch = True