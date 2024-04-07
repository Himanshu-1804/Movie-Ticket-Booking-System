import mysql.connector as sqltor
mycon = sqltor.connect(host = "localhost", user = "root", password = "himanshu_2005", database = "project")
cursor = mycon.cursor()
if mycon.is_connected() :
    print("--------------------------------------------------")
    print("          WELCOME TO VPR CINEMAS BOOKING          ")
    print("--------------------------------------------------")
else :
    print("Connection has not been established!")
    
print("1. LOG IN")
print("2. SIGN UP")
print("3. VIEW MOVIES")
print("4. EXIT")
ch = int(input("Enter your choice (1-4): "))

if ch == 1 :
    uid = input("Enter your User-ID : ")
    cursor.execute("select user_id from user")
    l = cursor.fetchall()
    count1 = 0
    count4 = 0
    for i in range(len(l)) :
        utd = l[i][0]
        if uid == utd :
            count1 = count1 + 1
    if count1 == 0 :
        print("Invalid User-ID!")
    if count1 > 0 :
        psw = input("Enter your password : ")
        cursor.execute("select password from user where user_id = '{}'" .format(uid))
        m = cursor.fetchall()
        if psw == m[0][0] :
            print("---------------------------------------------------")
            print("          YOU HAVE LOGGED IN SUCCESSFULLY!         ")
            print("---------------------------------------------------")
            print("1. BOOK A TICKET")
            print("2. VIEW MY BOOKINGS")
        else :
            print("Incorrect Password!")
            count4 = count4 + 1
        if count4 == 0 : 
            ch11 = int(input("Enter your choice (1-2) : "))
            if ch11 == 1 :
                print("----------------------------------------------------")
                print("       MOVIES STREAMING ON 11th JANUARY 2023        ")
                print("----------------------------------------------------")
                cursor.execute("select * from mv_11_jan")
                p = cursor.fetchall()
                for i in p :
                    print("__________", i[0], "__________")
                    print("Start Time : ", i[1])
                    print("End Time : ", i[2])
                    print("Screen : ", i[3])
                    print("Price per Ticket : ", i[4])
                    print("Tickets Booked : ", i[5])
                print("-------------------------------------")
                print("-------------------------------------")
                mvname = input("Enter Movie Name : ")
                stime = input("Enter Start Time : ")
                screen = input("Enter Screen : ")
                ntickets = int(input("Enter number of Tickets : "))
                cursor.execute("update mv_11_jan set tickets_booked = tickets_booked + {} where mv_name = '{}' and screen = {} and start_time = '{}'" .format(ntickets, mvname, screen, stime))
                mycon.commit()
                print("Your tickets have been booked successfully!")
                cursor.execute("select price_per_ticket from mv_11_jan where mv_name = '{}' and screen = {} and start_time = '{}'" .format(mvname, screen, stime))
                x = cursor.fetchall()
                bill = (int(x[0][0])) * (ntickets)
                print("Your total bill is : ", bill)
                cursor.execute("insert into user_movie values('{}', '{}', '{}', {}, {})" .format(uid, mvname, stime, screen, ntickets))
                mycon.commit()
            elif ch11 == 2 :
                cursor.execute("select * from user_movie where user_id = '{}'" .format(uid))
                f = cursor.fetchall()
                if f == [] :
                    print("--------------------------------------------------")
                    print("        YOU HAVE NOT MADE ANY BOOKINGS :(         ")
                    print("--------------------------------------------------")
                else :
                    print("---------------------------------------------------")
                    print("      YOU HAVE MADE THE FOLLOWING BOOKINGS!        ")
                    print("---------------------------------------------------")
                    for i in f :
                        print("__________", i[1], "__________")
                        print("Start Time : ", i[2])
                        print("Screen : ", i[3])
                        print("Tickets Booked : ", i[4])
                        print("-------------------------------------")
                        print("-------------------------------------")
                

elif ch == 2 :
    fname = input("Enter your first name : ")
    lname = input("Enter your last name : ")
    pnum = int(input("Enter your phone number : "))
    uid1 = input("Enter your User-ID : ")
    cursor.execute("select user_id from user")
    o = cursor.fetchall()
    count2 = 0
    count3 = 0
    for i in range(len(o)) :
        utd1 = o[i][0]
        if uid1 == utd1 :
            count2 = count2 + 1
    if count2 > 0 :
        print("User-ID already exists!")  
    if count2 == 0 :
        psw1 = input("Enter your password : ")
        while len(psw1) < 8 :
            print("Password must be 8 characters long!")
            psw1 = input("Re-enter your password : ")
        if len(psw1) >= 8 :
            cursor.execute("insert into user values('{}', '{}', {}, '{}', '{}')" .format(fname, lname, pnum, uid1, psw1))
            mycon.commit()
        print("You have successfully created your account!")


elif ch == 3 :
    print("----------------------------------------------------")
    print("       MOVIES STREAMING ON 11th JANUARY 2023        ")
    print("----------------------------------------------------")
    cursor.execute("select * from mv_11_jan")
    p = cursor.fetchall()
    for i in p :
        print("__________", i[0], "__________")
        print("Start Time : ", i[1])
        print("End Time : ", i[2])
        print("Screen : ", i[3])
        print("Price per Ticket : ", i[4])
        print("Tickets Booked : ", i[5])

elif ch == 4 :
    quit()

if ch not in [1, 2, 3, 4] :
    print("Invalid Choice")
            





        
