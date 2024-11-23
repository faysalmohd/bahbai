#importing mysql.connector
import mysql.connector

#asking password from user to access MySQL
pas=input("ENTER YOUR MYSQL PASSWORD : ")


#connecting with mysql
con=mysql.connector.connect(host='localhost',
                            password=pas,
                            user='root')


#checking if the connection is established
if con.is_connected():
    print("\n connecting...")
    print('connection successful')

cur=con.cursor()
cur.execute("SHOW DATABASES")
#checking if the database 'hospital' exists or not
g=()
for i in cur:
    g=g+i
g1=list(g)
count=0
for i in g1:
    if 'hospital' in g1:
        count=count+1
        break
    else:
        count=count+0
#creating new database 'hospital' if it does not exists


if count==0:
    print("\n DATABASE DOES NOT EXIST")
    cur.execute("create database hospital")
    con.commit()
    cur.execute("use hospital")
    con.commit()
    cur.execute("create table patient (p_id int primary key,name varchar(20),gender varchar(10),age int,address varchar(20),contact int,email varchar(30),room int,bed int)")
    con.commit()
    cur.execute("create table doctor (d_id int primary key,name varchar(20),speciality varchar(20),gender varchar(10),age int,salary int,contact int,email varchar(30),room int)")
    con.commit()
    cur.execute("create table appointment (p_id int primary key,appointment_with_doctor varchar(30),name varchar(20),gender varchar(10),age int,address varchar(20),contact int,email varchar(30),room int,bed int)")
    con.commit()
    cur.execute("create table admin (user_id int primary key, password varchar(30),admin_authorisation varchar(20))")
    con.commit()
    cur.execute("create table reception (user_id int primary key, password varchar(30),admin_authorisation varchar(20))")
    con.commit()
    cur.execute("create table messages (user_name varchar(30),contact int primary key,messages varchar(500))")
    con.commit()
    cur.execute("insert into admin (user_id,password) values (1234,'hello1234')")                   #default user id and password in admin
    con.commit()
    cur.execute("insert into reception (user_id,password) values (12345,'hello12345')")             #default user id and password in reception
    con.commit()

    print("\n DATABASE CREATED")
else:
    cur.execute("use hospital")
    con.commit()
    cur.execute("SHOW TABLES")
    data=cur.fetchall()
    #checking if all the tables exists or not
    d=()
    for i in data:
        d+=i
    check=0
    tab=['admin','reception','doctor','patient','appointment','messages']
    for i in range(0,len(tab)):
        if tab[i] in d:
            check+=1
        else:
            check+=0
    if check!=6:                #if tables does not exist, then creating new database with new tables
        cur.execute("drop database hospital")
        con.commit()
        cur.execute("create database hospital")
        con.commit()
        cur.execute("use hospital")
        con.commit()
        cur.execute("create table patient (p_id int primary key,name varchar(20),gender varchar(10),age int,address varchar(20),contact int,email varchar(30),room int,bed int)")
        con.commit()
        cur.execute("create table doctor (d_id int primary key,name varchar(20),speciality varchar(20),gender varchar(10),age int,salary int,contact int,email varchar(30),room int)")
        con.commit()
        cur.execute("create table appointment (p_id int primary key,appointment_with_doctor varchar(30),name varchar(20),gender varchar(10),age int,address varchar(20),contact int,email varchar(30),room int,bed int)")
        con.commit()
        cur.execute("create table admin (user_id int primary key, password varchar(30))")
        con.commit()
        cur.execute("create table reception (user_id int primary key, password varchar(30))")
        con.commit()
        cur.execute("create table messages (user_name varchar(30),contact int primary key,messages varchar(500))")
        con.commit()
        cur.execute("insert into admin (user_id,password) values (1234,'hello1234')")
        con.commit()
        cur.execute("insert into reception (user_id,password) values (12345,'hello12345')")
        con.commit()
        print("\n NEW TABLES CREATED IN DATABASE")
    else:                       #if table existing, then we continue with those tables
        print("\n DATABASE EXIST")




    
#function area


def patient_inputs():           #function for patient inputs
    while True:
        while True:
            p_id=input("Patient ID : ")
            a=p_id.isdigit()
            if a==True:
                p_id=int(p_id)
                break
            else:
                print("ERROR! Patient ID must be in NUMBERS")
        name=str(input("Patient Name : "))
        gender=str(input("Patient Gender : "))
        while True:
            age=input("Patient Age : ")
            a=age.isdigit()
            if a==True:
                age=int(age)
                break
            else:
                print("ERROR! Patient AGE must be in NUMBERS")
        address=str(input("Patient Address : "))
        while True:
            contact=input("Patient Contact : ")
            a=contact.isdigit()
            if a==True:
                contact=int(contact)
                break
            else:
                print("ERROR! Patient CONTACT must be in NUMBERS")
        email=input("Patient Email : ")
        while True:
            room=input("Patient Room No. : ")
            a=room.isdigit()
            if a==True:
                room=int(room)
                break
            else:
                print("ERROR! Patient ROOM must be in NUMBERS")
        while True:
            bed=input("Patient Bed No. : ")
            a=bed.isdigit()
            if a==True:
                bed=int(bed)
                break
            else:
                print("ERROR! Patient BED must be in NUMBERS")
        cur.execute("insert into patient values(%s,'%s','%s',%s,'%s',%s,'%s',%s,%s)" %(p_id,name,gender,age,address,contact,email,room,bed))
        con.commit()
        print("CONGRATULATIONS!!!CHANGES SUCCESSFULLY SAVED!")
        ch=input("DO YOU WANT TO ENTER NEW RECORDS? (Y/N)")
        if ch in 'Nn':
            break
        else:
            continue


def doctor_inputs():            #function for doctor input
    while True:
        while True:
            d_id=input("Doctor ID : ")
            a=d_id.isdigit()
            if a==True:
                d_id=int(d_id)
                break
            else:
                print("ERROR! Doctor ID must be in NUMBERS")
        name=str(input("Doctor's Name : "))
        speciality=str(input("Speciality In : "))
        gender=str(input("Gender : "))
        while True:
            age=input("Age : ")
            a=age.isdigit()
            if a==True:
                age=int(age)
                break
            else:
                print("ERROR! Doctor AGE must be in NUMBERS")
        while True:
            salary=input("Salary : ")
            a=salary.isdigit()
            if a==True:
                salary=int(salary)
                break
            else:
                print("ERROR! Doctor salary must be in NUMBERS")
        while True:
            contact=input("Contact : ")
            a=contact.isdigit()
            if a==True:
                contact=int(contact)
                break
            else:
                print("ERROR! Doctor CONTACT must be in NUMBERS")
        email=input("Email : ")
        while True:
            room=input("Doctor's Room No. : ")
            a=room.isdigit()
            if a==True:
                room=int(room)
                break
            else:
                print("ERROR! Doctor ROOM must be in NUMBERS")
        cur.execute("insert into doctor values(%s,'%s','%s','%s',%s,%s,%s,'%s',%s)" %(d_id,name,speciality,gender,age,salary,contact,email,room))
        con.commit()
        print("CHANGES SUCCESSFULLY SAVED!")
        ch=input("DO YOU WANT TO ENTER NEW RECORDS? (Y/N)")
        if ch in 'Nn':
            break
        else:
            continue

def admin():                    #sign up function for admin
    while True:
        while True:
            user_id=input("ENTER EXISTING ADMIN's ID : ")
            a=user_id.isdigit()
            if a==True:
                user_id=int(user_id)
                break
            else:
                print("ERROR! USER_ID must be in NUMBERS")
        password=input("Password : ")
        cur.execute("select user_id from admin")
        data=cur.fetchall()
        k=()
        count=0
        for i in data:
            k+=i
        if user_id in k:
            count+=1
        else:
            count+=0
        cur.execute("select password from admin")
        data1=cur.fetchall()
        p=()
        ct=0
        for i in data1:
            p+=i
        if password in p:
            ct+=1
        else:
            ct+=0
        if count==1 and ct==1:
            print(" ")
            print("ENTER NEW RECORDS")
            print(" ")
            while True:
                user_id2=input("NEW ADMIN's ID : ")
                a=user_id2.isdigit()
                if a==True:
                    user_id2=int(user_id2)
                    break
                else:
                    print("ERROR! USER ID must be in NUMBERS")
            password=input("Password : ")
            repass=input("Confirm Password : ")
            if password==repass:
                cur.execute("insert into admin values(%s,'%s','%s')"%(user_id2,password,user_id))
                con.commit()
                print("CHANGES SUCCESSFULLY SAVED!")
                break
            else:
                print("ERROR! THE ENTERED PASSWORD and the CONFIRMATION PASSWORD do not match")
                choice=input("DO YOU WANT TO SIGN UP AGAIN? : ")
                if choice in "Nn":
                    break
                else:
                    continue
        else:
            print("ERROR! YOU HAVE ENTERED A WRONG USER ID OR PASSWORD. PLEASE RE-TRY")
            ch=input("DO YOU WANT TO RE-TRY? : ")
            if ch in "Nn":
                break
            else:
                continue


def reception():                    #sign up function for reception
    while True:
        while True:
            user_id=input("ENTER EXISTING ADMIN's ID : ")
            a=user_id.isdigit()
            if a==True:
                user_id=int(user_id)
                break
            else:
                print("ERROR! USER ID must be in NUMBERS")
        password=input("Password : ")
        cur.execute("select user_id from admin")
        data=cur.fetchall()
        k=()
        count=0
        for i in data:
            k+=i
        if user_id in k:
            count+=1
        else:
            count+=0
        cur.execute("select password from admin")
        data1=cur.fetchall()
        p=()
        ct=0
        for i in data1:
            p+=i
        if password in p:
            ct+=1
        else:
            ct+=0
        if count==1 and ct==1:
            print(" ")
            print("ENTER NEW RECORDS")
            print(" ")
            while True:
                user_id2=input("NEW RECEPTIONIST's ID : ")
                a=user_id2.isdigit()
                if a==True:
                    user_id2=int(user_id2)
                    break
                else:
                    print("ERROR! USER ID must be in NUMBERS")
            password=input("Password : ")
            repass=input("Confirm Password : ")
        if password==repass:
            cur.execute("insert into reception values(%s,'%s',%s)"%(user_id,password,user_id))
            con.commit()
            print("CHANGES SUCCESSFULLY SAVED!")
            break
        else:
            print("ERROR! the ENTERED PASSWORD and the CONFIRMATION PASSWORD do not match")
            choice=input("DO YOU WANT TO SIGN UP AGAIN? : ")
            if choice in "Nn":
                break
            else:
                continue










def update_patient():           #updating patient information
    while True:
        print("1. UPDATE NAME")
        print("2. UPDATE GENDER")
        print("3. UPDATE AGE")
        print("4. UPDATE ADDRESS")
        print("5. UPDATE CONTACT")
        print("6. UPDATE EMAIL")
        print("7. UPDATE ROOM")
        print("8. UPDATE BED")
        choice=input("Enter your choice : ")
        if choice=='1':
            while True:
                p_id=input("Enter patient ID : ")
                a=p_id.isdigit()
                if a==True:
                    p_id=int(p_id)
                    break
                else:
                    print("ERROR! Patient ID must be in NUMBERS")
            new=input("Enter new NAME : ")
            cur.execute("update patient set name='%s' where p_id=%s "%(new,p_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='2':
            while True:
                p_id=input("Enter patient ID : ")
                a=p_id.isdigit()
                if a==True:
                    p_id=int(p_id)
                    break
                else:
                    print("ERROR! Patient ID must be in NUMBERS")
            new=input("Enter new GENDER : ")
            cur.execute("update patient set gender='%s' where p_id=%s "%(new,p_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='3':
            while True:
                p_id=input("Enter patient ID : ")
                a=p_id.isdigit()
                if a==True:
                    p_id=int(p_id)
                    break
                else:
                    print("ERROR! Patient ID must be in NUMBERS")
            while True:
                new=input("Enter new AGE : ")
                a=new.isdigit()
                if a==True:
                    new=int(new)
                    break
                else:
                    print("ERROR! Patient AGE must be in NUMBERS")
            cur.execute("update patient set age=%s where p_id=%s "%(new,p_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='4':
            while True:
                p_id=input("Enter patient ID : ")
                a=p_id.isdigit()
                if a==True:
                    p_id=int(p_id)
                    break
                else:
                    print("ERROR! Patient ID must be in NUMBERS")
            new=input("Enter new ADDRESS : ")
            cur.execute("update patient set address='%s' where p_id=%s "%(new,p_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='5':
            while True:
                p_id=input("Enter patient ID : ")
                a=p_id.isdigit()
                if a==True:
                    p_id=int(p_id)
                    break
                else:
                    print("ERROR! Patient ID must be in NUMBERS")
            while True:
                new=input("Enter new CONTACT : ")
                a=new.isdigit()
                if a==True:
                    new=int(new)
                    break
                else:
                    print("ERROR! Patient CONTACT must be in NUMBERS")
            cur.execute("update patient set contact=%s where p_id=%s "%(new,p_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='6':
            while True:
                p_id=input("Enter patient ID : ")
                a=p_id.isdigit()
                if a==True:
                    p_id=int(p_id)
                    break
                else:
                    print("ERROR! Patient ID must be in NUMBERS")
            new=input("Enter new EMAIL : ")
            cur.execute("update patient set email='%s' where p_id=%s "%(new,p_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='7':
            while True:
                p_id=input("Enter patient ID : ")
                a=p_id.isdigit()
                if a==True:
                    p_id=int(p_id)
                    break
                else:
                    print("ERROR! Patient ID must be in NUMBERS")
            while True:
                new=input("Enter new ROOM : ")
                a=new.isdigit()
                if a==True:
                    new=int(new)
                    break
                else:
                    print("ERROR! Patient ROOM must be in NUMBERS")
            cur.execute("update patient set room=%s where p_id=%s "%(new,p_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='8':
            while True:
                p_id=input("Enter patient ID : ")
                a=p_id.isdigit()
                if a==True:
                    p_id=int(p_id)
                    break
                else:
                    print("ERROR! Patient ID must be in NUMBERS")
            while True:
                new=input("Enter new BED : ")
                a=new.isdigit()
                if a==True:
                    new=int(new)
                    break
                else:
                    print("ERROR! Patient BED must be in NUMBERS")
            cur.execute("update patient set bed=%s where p_id=%s "%(new,p_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        else:
            print("\t SORRY! YOU HAVE SELECTED THE WRONG OPTION. ")
            print("\t THANKK YOU")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue


def doctor_update():                #updating doctors information 
    ch="Y"
    while ch in "Yy" :
        print("1. UPDATE NAME")
        print("2. UPDATE SPECIALITY")
        print("3. UPDATE GENDER")
        print("4. UPDATE AGE")
        print("5. UPDATE SALARY")
        print("6. UPDATE CONTACT")
        print("7. UPDATE EMAIL")
        print("8. UPDATE ROOM")
        choice=input("Enter your choice : ")
        if choice=='1':
            while True:
                d_id=input("Enter doctor ID : ")
                a=d_id.isdigit()
                if a==True:
                    d_id=int(d_id)
                    break
                else:
                    print("ERROR! Doctor ID must be in NUMBERS")
            new=input("Enter new NAME : ")
            cur.execute("update doctor set name='%s' where d_id=%s "%(new,d_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='2':
            while True:
                d_id=input("Enter doctor ID : ")
                a=d_id.isdigit()
                if a==True:
                    d_id=int(d_id)
                    break
                else:
                    print("ERROR! Doctor ID must be in NUMBERS")
            new=input("Enter new SPECIALITY : ")
            cur.execute("update doctor set speciality='%s' where d_id=%s "%(new,d_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='3':
            while True:
                d_id=input("Enter doctor ID : ")
                a=d_id.isdigit()
                if a==True:
                    d_id=int(d_id)
                    break
                else:
                    print("ERROR! Doctor ID must be in NUMBERS")
            new=input("Enter new GENDER : ")
            cur.execute("update doctor set gender='%s' where d_id=%s "%(new,d_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='4':
            while True:
                d_id=input("Enter doctor ID : ")
                a=d_id.isdigit()
                if a==True:
                    d_id=int(d_id)
                    break
                else:
                    print("ERROR! Doctor ID must be in NUMBERS")
            new=input("Enter new AGE : ")
            cur.execute("update doctor set age=%s where d_id=%s "%(new,d_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='5':
            while True:
                d_id=input("Enter doctor ID : ")
                a=d_id.isdigit()
                if a==True:
                    d_id=int(d_id)
                    break
                else:
                    print("ERROR! Doctor ID must be in NUMBERS")
            while True:
                new=input("Enter doctor salary : ")
                a=new.isdigit()
                if a==True:
                    new=int(new)
                    break
                else:
                    print("ERROR! Doctor SALARY must be in NUMBERS")
            cur.execute("update doctor set salary=%s where d_id=%s "%(new,d_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='6':
            while True:
                d_id=input("Enter doctor ID : ")
                a=d_id.isdigit()
                if a==True:
                    d_id=int(d_id)
                    break
                else:
                    print("ERROR! Doctor ID must be in NUMBERS")
            while True:
                new=input("Enter doctor contact : ")
                a=new.isdigit()
                if a==True:
                    new=int(new)
                    break
                else:
                    print("ERROR! Doctor ID must be in NUMBERS")
            cur.execute("update doctor set contact=%s where d_id=%s "%(new,d_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='7':
            while True:
                d_id=input("Enter doctor ID : ")
                a=d_id.isdigit()
                if a==True:
                    d_id=int(d_id)
                    break
                else:
                    print("ERROR! Doctor ID must be in NUMBERS")
            new=input("Enter new EMAIL : ")
            cur.execute("update doctor set email='%s' where d_id=%s "%(new,d_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        elif choice=='8':
            while True:
                d_id=input("Enter doctor ID : ")
                a=d_id.isdigit()
                if a==True:
                    d_id=int(d_id)
                    break
                else:
                    print("ERROR! Doctor ID must be in NUMBERS")
            while True:
                new=input("Enter doctor room : ")
                a=new.isdigit()
                if a==True:
                    new=int(new)
                    break
                else:
                    print("ERROR! Doctor ROOM must be in NUMBERS")
            cur.execute("update doctor set room=%s where d_id=%s "%(new,d_id))
            con.commit()
            print("UPDATE WAS SUCCESSFUL")
            ch=input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)")
            if ch in "Nn":
                break
            else:
                continue
        else:
            print("SORRY! YOU HAVE SELECTED THE WRONG OPTION. ")
            print("THANKK YOU")
            ch=eval(input("DO YOU WANT TO CONTINUE UPDATING? (Y/N)"))
            if ch in "Nn":
                break
            else:
                continue
            

def delete_p_records():               #delete patient records
    ch="Yy"
    while True:
        while True:
            p_id=input("Enter DELETING ID : ")
            a=p_id.isdigit()
            if a==True:
                p_id=int(p_id)
                break
            else:
                print("ERROR! ID must be in NUMBERS")
        p=cur.execute("select p_id from patient ")
        b=cur.fetchall()
        k=()
        for i in b:
            k+=i
        if p_id in k:
            cur.execute("delete from patient where p_id=%s"%(p_id))
            con.commit()
            print("PATIENT ID '",p_id,"' HAS BEEN DELETED SUCCESSSFULLY")
        else:
            print("PATIENT ID '",p_id,"' DOES NOT EXIST")
        choice=input("DO YOU WANT TO DELETE ANY OTHER RECORD (Y/N) : ")
        if choice in "Nn":
            break
        else:
            continue



def delete_d_records():               #delete doctor records
    ch="Yy"
    while True:
        while True:
            d_id=input("Enter DELETING ID : ")
            a=d_id.isdigit()
            if a==True:
                d_id=int(d_id)
                break
            else:
                print("ERROR! ID must be in NUMBERS")
        cur.execute("select d_id from doctor ")
        b=cur.fetchall()
        k=()
        for i in b:
            k+=i
        if d_id in k:
            cur.execute("delete from doctor where d_id=%s"%(d_id))
            con.commit()
            print("DOCTOR ID '",d_id,"' HAS BEEN DELETED SUCCESSSFULLY")
        else:
            print("DOCTOR ID '",d_id,"' DOES NOT EXIST")
        choice=input("DO YOU WANT TO DELETE ANY OTHER RECORD (Y/N) : ")
        if choice in "Nn":
            break
        else:
            continue



def appointment():                  #booking an appointment
    while True:
        ch="y"
        while ch in "Yy":
            cur.execute("select name,speciality from doctor")
            data=cur.fetchall()
            info=[]
            for i in data:
                info.append(i)
            while True:
                p_id=input("Patient ID : ")
                a=p_id.isdigit()
                if a==True:
                    p_id=int(p_id)
                    break
                else:
                    print("ERROR! Patient ID must be in NUMBERS")
            for i in info:
                print("\nName = ",i[0])
                print("Speciality = ",i[1])
            a_w_d=str(input("\nENTER A DOCTOR'S NAME FROM THE ABOVE LIST WITH WHOM YOU WANT TO BOOK AN APPOINTMENT : "))
            cur.execute("select name from doctor")
            data1=cur.fetchall()
            k=()
            for i in data1:
                k+=i
            if a_w_d in k:
                pass
            else:
                print("\n ERROR! YOU HAVE ENTER A WRONG DOCTOR'S NAME. PLEASE RE-CHECK.")
                print("\n")
                break
            name=str(input("Patient Name : "))
            gender=str(input("Patient Gender : "))
            while True:
                age=input("Patient Age : ")
                a=age.isdigit()
                if a==True:
                    age=int(age)
                    break
                else:
                    print("ERROR! Patient AGE must be in NUMBERS")
            address=str(input("Patient Address : "))
            while True:
                contact=input("Patient Contact : ")
                a=contact.isdigit()
                if a==True:
                    contact=int(contact)
                    break
                else:
                    print("ERROR! Patient CONTACT must be in NUMBERS")
            email=input("Patient Email : ")
            date=input("When do you wish to visit (yyyy-mm-dd) : ")
            cur.execute("insert into appointment values(%s,'%s','%s','%s',%s,'%s',%s,'%s','%s')" %(p_id,a_w_d,name,gender,age,address,contact,email,date))
            con.commit()
            print("\n CONGRATULATIONS!!!YOU HAVE SUCCESSFULLY BOOKED AN APPOINTMENT ")
            break
        ch=input("DO YOU WANT TO TAKE A NEW APPOINTMENT? (Y/N) : ")
        if ch in 'Nn':
            break
        else:
            continue
    


def search_patient():                       #search for patient
    while True:
        while True:
            ct=0
            search=input("ENTER THE SEARCHING VALUE : ")
            while True:
                if search=="" or search in "              ":
                    ct+=1
                    break
                elif search in ('m','M','male','MALE','Male','f','F','female','Female','FEMALE'):
                    ct+=1
                    break
                else:
                    ct+=0
                    break
            if ct==1:
                print("ERROR! YOU CANT'T SEARCH EMPTY VALUES. ")
            else:
                break
        a=search.isdigit()
        if a==True:
            search=int(search)
        cur.execute('select * from patient')
        data=cur.fetchall()
        info=list()
        for i in data:
            info.append(i)
        count=0
        while True:
            for i in info:
                if search in i:
                    print("\nPatient Id = ",i[0])
                    print("Patient Name = ",i[1])
                    print("Gender = ",i[2])
                    print("Age = ",i[3])
                    print("Address = ",i[4])
                    print("Contact = ",i[5])
                    print("E-Mail = ",i[6])
                    print("Room No. = ",i[7])
                    print("Bed No. = ",i[8],"\n")
                    count+=1
                else:
                    continue
            if count>=1:
                break
            else:
                print("SORRY! THE RECORD YOU ARE LOOKING FOR IS NOT AVAILABLE IN THE DATABASE")
                break
                
        ch=input("Do you want to continue? (Y/N) : ")
        if ch in "Nn":
            break
        else:
            pass


def search_doctor():                           #search for doctor
    while True:
        while True:
            ct=0
            search=input("ENTER THE SEARCHING ELEMENT : ")
            while True:
                if search=="" or search in "              " :
                    ct+=1
                    break
                elif search in ('m','M','male','MALE','Male','f','F','female','Female','FEMALE'):
                    ct+=1
                    break
                else:
                    ct+=0
                    break
            if ct==1:
                print("ERROR! YOU CANT'T SEARCH EMPTY VALUES. ")
            else:
                break
        a=search.isdigit()
        if a==True:
            search=int(search)
        cur.execute('select * from doctor')
        data=cur.fetchall()
        info=list()
        for i in data:
            info.append(i)
        count=0
        while True:
            for i in info:
                if search in i:
                    print("\nDoctor id = ",i[0])
                    print("Patient Name = ",i[1])
                    print("Speciality = ",i[2])
                    print("Gender = ",i[3])
                    print("Age = ",i[4])
                    print("Contact = ",i[6])
                    print("E-Mail = ",i[7])
                    print("Room No. = ",i[8],"\n")
                    count+=1
                else:
                    continue
            if count>=1:
                break
            else:
                print("SORRY! THE RECORD YOU ARE LOOKING FOR IS NOT AVAILABLE IN THE DATABASE")
                break
                
        ch=input("Do you want to continue? (Y/N) : ")
        if ch in "Nn":
            break
        else:
            continue




def show_messages():
    while True:
        while True:
            cur.execute("select messages from messages")
            data=cur.fetchall()
            info=()
            for i in data:
                info+=i
            print("\n1. Show 3 new messages")
            print("2. Show all messages")
            print("")
            ch=input("ENTER YOUR CHOICE : ")
            if ch=='1':
                if info==():
                    print("No messages to display. ")
                    break
                else:
                    print("1. ",info[-1])
                    print("2. ",info[-2])
                    print("3. ",info[-3])
                    break
            elif ch=='2':
                if info==():
                    print("No messages to display. ")
                    break
                else:
                    for i in range(0,len(info)):
                        print(info[i])
            else:
                print("\nSORRY! YOU HAVE ENTERED A WRONG CHOICE.")
                break
        rep=input("Do you want to continue seeing messages (Y/N) : ")
        if rep in "Nn":
            break





def admin_log_in():                    #log in function for admin
    while True:
        while True:
            user_id=input("ADMIN's ID : ")
            h=user_id.isdigit()
            if h==True:
                break
            else:
                print("ERROR! ADMIN'S ID MUST BE IN NUMBERS ONLY.")
        user_id=int(user_id)
        password=input("Password : ")
        cur.execute("select user_id,password from admin")
        data=cur.fetchall()
        c=0
        for i in range(0,len(data)):
            if (user_id,password)==data[i]:
                c+=1
                break
            else:
                c+=0
        if c==1:
            print(" ")
            print("welcome")
            print(" ")
            print("1. DOCTORS ")
            print("2. PATIENTS ")
            print("3. MESSAGES ")
            m=input("ENTER YOUR choice : ")
            while True:
                if m=='1':
                    print("1. ENTER NEW DOCTOR ")
                    print("2. DELETE DOCTOR'S RECORD ")
                    print("3. UPDATE DOCTOR'S RECORD ")
                    n=input("ENTER YOUR CHOICE : ")
                    print(" ")
                    if n=='1':
                        doctor_inputs()
                    elif n=='2':
                        delete_d_records()
                    elif n=='3':
                        doctor_update()
                    else:
                        print("YOU HAVE ENTERED A WRONG CHOICE. PLEASE MAKE SURE TO ENTER A CHOICE FROM THE LIST PROVIDED")
                        p=input("DO YOU WANT TO CONTINUE YOUR SERVICE WITH THE DOCTOR'S PAGE : ")
                        if p in "Nn":
                            print("THANK YOU!")
                            break
                        else:
                            continue
                elif m=='2':
                    print("1. ENTER NEW PATIENT ")
                    print("2. DELETE PATIENT'S RECORD ")
                    print("3. UPDATE PATIENT'S RECORD ")
                    n=input("ENTER YOUR CHOICE : ")
                    if n=='1':
                        patient_inputs()
                    elif n=='2':
                        delete_p_records()
                    elif n=='3':
                        update_patient()
                    else:
                        print("YOU HAVE ENTERED A WRONG CHOICE. PLEASE MAKE SURE TO ENTER A CHOICE FROM THE LIST PROVIDED")
                        p=input("DO YOU WANT TO CONTINUE YOUR SERVICE WITH THE DOCTOR'S PAGE : ")
                        if p in "Nn":
                            print("THANK YOU!")
                            break
                        else:
                            continue
                elif m=='3':
                    show_messages()
                    break
                else:
                    print("YOU HAVE ENTERED A WRONG CHOICE. PLEASE MAKE SURE TO ENTER A CHOICE FROM THE LIST PROVIDED")
                    break
        else:
            print("ERROR! the ENTERED PASSWORD or the USER ID is incorrect. Please re-try!")
        choice=input("DO YOU WANT TO RE-TRY ? : ")
        if choice in "Nn":
            print("THANK YOU!")
            break
        else:
            continue
    



def reception_log_in():                    #log in function for reception
    while True:
        while True:
            user_id=input("RECEPTIONIST's ID : ")
            h=user_id.isdigit()
            if h==True:
                break
            else:
                print("ERROR! RECEPTIONIST'S ID MUST BE IN NUMBERS ONLY.")
        user_id=int(user_id)
        password=input("Password : ")
        cur.execute("select user_id,password from reception")
        data=cur.fetchall()
        c=0
        for i in range(0,len(data)):
            if (user_id,password)==data[i]:
                c+=1
                break
            else:
                c+=0
        if c==1:
            print(" ")
            print("welcome")
            print(" ")
            print("1. ENTER NEW PATIENT ")
            print("2. DELETE PATIENT'S RECORD ")
            print("3. UPDATE PATIENT'S RECORD ")
            n=input("ENTER YOUR CHOICE : ")
            if n=='1':
                patient_inputs()
            elif n=='2':
                delete_p_records()
            elif n=='3':
                update_patient()
            else:
                print("YOU HAVE ENTERED A WRONG CHOICE. PLEASE MAKE SURE TO ENTER A CHOICE FROM THE LIST PROVIDED")
                ch=input("DO YOU WANT TO CONTINUE YOUR SERVICE WITH THE DOCTOR'S PAGE : ")
                if ch in "Nn":
                    print("THANK YOU!")
                    break
                else:
                    continue
                
        else:
            print("ERROR! the ENTERED PASSWORD or the USER ID is incorrect. Please re-try!")
        choice=input("DO YOU WANT TO RE-TRY ? (Y/N) : ")
        if choice in "Nn":
            print("THANK YOU!")
            break
        else:
            continue




def search():                       #search function for both doctors and patient
    while True:
        print("1. SEARCH DOCTOR")
        print("2. SEARCH PATIENT")
        choice=input("ENTER YOUR CHOICE : ")
        if choice=='1':
            search_doctor()
        elif choice=='2':
            search_patient()
        else:
            print("ERROR! YOU HAVE ENTERED A WORNG CHOICE. PLEASE RE-TRY")
            ch=input("ENTER YOUR CHOICE : ")
            if ch in "Nn":
                break
            else:
                continue



def contact_us():
    while True:
        user_name=input("ENTER YOUR NAME : ")
        contact=int(input("ENTER YOUR CONTACT : "))
        message=input("TYPE YOUR MESSAGE HERE : ")
        cur.execute("insert into messages values('%s',%s,'%s')"%(user_name, contact, message))
        con.commit()
        print("\nSENDING...")
        print("\nSEND SUCCESSFUL")
        print("\nTHANK YOU")
        ch=input(" Do you want to continue contacting us? (Y/N) : ")
        if ch in "Nn":
            break
        else:
            continue





def help_me():
    while True:
        print("\nHello there. Welcome to BAHBAI HOSPITAL MANAGEMENT SYSTEM. Here we do task like:")
        print("\nA quick walk-through the application:")
        print("\nWhen you open this application, you will be directed to the main screen. From there you will get various options.")
        print("You need to select the option that provides the servise you are looking for with BAHBAI HOSPITAL MANAGEMENT SYSTEM.")
        print("Also you will be provided with an input box. Select an option in NUMBER ")
        print("After selecting an option of your choice,if you choose log in options (OPTION 1 AND 2 ), ")
        print("you will be asked to enter user id and password to further proceed. ")
        print("\nOption 3. SEARCH is open to all users. In it, you can search a patient or a doctor.")
        print("\nOption 4. appointment is for booking an appointment with any doctor of your choice.")
        print("\nOption 5. SIGN UP is a function in which you can sign up for ADMIN OR RECEPTIONIST. ")
        print("\t \t NOTE: OPTION 5. SIGN UP requires an admin's access for further processing.")
        print("\t \t \t i.e. you will need an existing admin's user id and password to sign up.")
        print("\nOPTION 6. is for contacting us. You can write a re-view for us or any question regarding medical purposes.")
        print("\nOPTION 7. is this service going-on")
        print("\nOPTION 8. is for quiting the program and leaving this site.")
        print("\n \n ANY MORE ASSISSTANCE CAN BE PROVIDED BY OPTION 6. FEEL FREE TO USE IT.")
        print("\n \n \t \t \t THANK YOU!")
        break
    





def owner():
    print("ADMIN Log in:")
    print("\t user id = 1234")
    print("\t password = hello1234")
    print("\n\nRECEPTION Log in:")
    print("\t user id = 12345")
    print("\t password = hello12345")



    
#main area

print(" ")
print("\t\t*****************************************")
print("\t\t***...................................***")
print("\t\t**....WELCOME TO AL BAHBAI HOSPITAL....**")
print("\t\t***...................................***")
print("\t\t*****************************************")
print(" ")
ch="y"
while ch=="y": 
   print("Please choose a service:")
   print("\n\t1. ADMIN")
   print("\t2. RECEPTION USER")
   print("\t3. SEARCH")
   print("\t4. APPOINTMENT")
   print("\t5. SIGN UP")
   print("\t6. CONTACT US")
   print("\t7. HELP!")
   print("\t8. QUIT")
   choice=input("\t\tENTER YOUR CHOICE : ")

   
   if choice=='1':
       admin_log_in()

       
   elif choice=='2':
       reception_log_in()

     
   elif choice=='3':
       search()

     
   elif choice=='4':
       appointment()
       
   elif choice=='5':
        print("SIGN UP AS:")
        print("1. ADMIN")
        print("2. RECEPTIONIST")
        choice=input("ENTER YOUR CHOICE : ")
        if choice=='1':
            admin()
        elif choice=='2':
            reception()
        else:
            print("ERROR! YOU HAVE ENTERED A WRONG CHOICE. PLEASE RE-TRY")
            ch=input("DO YOU WANT TO CONTINUE FOR SIGN UP AGAIN? : ")
            if ch in"Nn":
                break

   elif choice=='6':
       contact_us()

   elif choice=='7':
       help_me()

   elif choice=='8':
       quit()

   elif choice=='2003':
       owner()

   else:
     print("\t \n SORRY! YOU HAVE SELECTED THE WRONG OPTION. PLEASE MAKE SURE FOR WHAT SERVICE YOU ARE LOOKING FOR.")
     print("\t \n THANKK YOU")
     ch=input("\n DO YOU WISH TO CONTINUE THE PROGRAM AGAIN : (Y/N)")
     if ch in "Nn":
         break
