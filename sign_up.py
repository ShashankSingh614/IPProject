'''
This code will create a new account for the user
This will be used during sign-up process
'''

import hashlib
import mysql.connector as sqltor

def table_exists(table_name, connection):
    try:
        cursor1 = mycon.cursor()
        cursor1.execute(f"SHOW TABLES LIKE '{table_name}'")
        result = cursor1.fetchone()
        return result is not None
    except sqltor.Error as err:
        return False
    finally:
        cursor1.close()

print(__name__) #main

'''
Conneting to MySQL:
    host : localhost
    username : <username>
    password : <password>
    database : <website_name>
'''

mycon = sqltor.connect(host='localhost',username='<username>',password='<password>',database='<website_name>')
cursor = mycon.cursor()

'''
Taking input from users:
    Email Id
    First Name
    Surname 
    Date of Birth (yyyy-mm-dd)
    Gender (Male/Female/LBGTQ/Rather not say)
    Contact Number
    Create an username
    Create a strong password with mixture of letters, numbers & symbols
    Confirm password
'''

email_id = input("Enter your emial id (exmaple@company.com):")
first_name = input("Enter your first name:")
surname = input("Enter your surname:")
dob = input("Enter your date of birth (yyyy-mm-dd):")
gender = input("Enter your gender (Male/Female/LBGTQ/Rather not say):")
contact_number = int(input("Enter your contact number:"))
        
data = cursor.fetchall()
un = True
while un == True:
    username = input("Create a username:")
    for row in data:
        if (username in row):
            print("Username already taken!")
            un == True
        else:
            un == False
            p = True
            while p == True:
                password = str(input("Create a strong password with mixture of letters, numbers & symbols and having more then 8 characters:"))
                
                '''
                Check if password contains:
                    Uppercase letters
                    Lowecase letters
                    Numbers
                    Symbols
                    Lenght of password more then 8
                '''
                
                count = 0
                symbols = set("!@#$%^&*()_}{[]|;:<>?,.\/")
                for char in password:
                    if char.isupper:
                        count += 1
                    elif char.islower:
                        count += 1
                    elif char.isalnum:
                        count += 1
                    elif char in symbols:
                        count += 1

                if count>=4 and len(password)>8:
                    print("Strong Password!")
                else:
                    print("Weak Password!")
                    p = True
                    break

                confirm_password = input("Confirm password:")
                if(password==confirm_password): #Cheking if password is matching or not

                    '''
                    Converting password to hash
                    '''

                    sha521 = hashlib.sha512()
                    sha521.update(password)
                    hash_sha521 = sha521.hexdigest()

                    '''
                    Creating Table Record:
                        Email_id : varchar(255) NOT NULL
                        First_name : varchar(255) NOT NULL
                        Surname : varchar(255) NOT NULL
                        Date_of_Birth : DATE NOT NULL
                        Gender : varchar(255) NOT NULL
                        Contact : INT(10) NOT NULL
                        Username : varchar(255) NOT NULL PRIMARY KEY
                        Password : varchar(1000) NOT NULL
                    '''

                    table_name_to_check = "Record"
    
                    if table_exists(table_name_to_check, mycon):
                        '''
                        Entering data into MySQL
                        Table name : Record
                        '''
                        record = "INSERT INTO Record(Email,Fname,Sname,DOB,Gender,Contact,Username,Password) VALUES ('{}','{}','{}',{},'{}',{},'{}','{}')".format(email_id,first_name,surname,dob,gender,contact_number,username,hash_sha521)
                        cursor.execute(record)
                        mycon.commit()
                    else:
                        '''
                        Creating table Record
                        Entering data into MySQL
                        '''
                        table_create = "CREATE TABLE Record(Email_id varchar(255) NOT NULL,First_name varchar(255) NOT NULL,Surname varchar(255) NOT NULL,Date_of_Birth DATE NOT NULL,Gender varchar(255) NOT NULL,Contact INT(10) NOT NULL,Username varchar(255) NOT NULL PRIMARY KEY,Password varchar(1000) NOT NULL)"
                        cursor.execute(table_create)
                        mycon.commit()
                        record = "INSERT INTO Record(Email,Fname,Sname,DOB,Gender,Contact,Username,Password) VALUES ('{}','{}','{}',{},'{}',{},'{}','{}')".format(email_id,first_name,surname,dob,gender,contact_number,username,hash_sha521)
                        cursor.execute(record)
                        mycon.commit()

                    p = False
                    break
                else:
                    print("Password doesn't match!") #Error message
                    p = True
            break

mycon.close()