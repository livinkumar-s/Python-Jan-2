import mysql.connector

connection=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345",
    database="employee"
)


cursor=connection.cursor()

# cursor.execute("select * from contacts")
# result =cursor.fetchall()

# print(result)

# cursor.execute("INSERT INTO contacts (name,mobile) VALUES (%s,%s)",("Gwenn",6383366775))
# connection.commit()

def addNewContact(name,mobile):
    cursor.execute("INSERT INTO contacts (name,mobile) VALUES (%s,%s)",(name,mobile))
    connection.commit()
    print("Contact added")

def viewAllContact():
    cursor.execute("select * from contacts")
    result =cursor.fetchall()
    for i in result:
        print(f"{i[1]} : {i[2]}")

while True:
    inp=int(input('''Chooss an Option
-----------------------
0 ---> Exit
1 ---> Add Contact
2 ---> View Contact
3 ---> Update Contact
4 ---> Delete Contact

'''))
    if inp==0:
        break
    elif inp==1:
        name=input("Enter Name: ")
        mobile=int(input("Enter Mobile: "))
        addNewContact(name,mobile)
    elif inp==2:
        viewAllContact()