#EL project
import mysql.connector
mydb= mysql.connector.connect(
host="localhost",
username="root",
password="root",
)
mycursor=mydb.cursor()

def soulelement():
        points=0
        mycursor.execute("Create table Soulelement(Questions varchar(250),Answers varchar(250))")
        q1="Q1) What three words best describe your personality ?" 
        print("\nQuestions\n"+q1)
        a11="1) Fun,Playful and Friendly"
        a12="2) Creative,Decisive and Clever"
        a13="3) Chill,Easy-Going and Laid-Back"
        a14="4) Passionate,Emotional and Protective"
        print("\nOptions\n"+a11+"\n"+a12+"\n"+a13+"\n"+a14)
        a15=eval(input("Enetr your option:\r"))
        if a15==1:
                sql="Insert into soulelement values(%s,%s)"
                val=(q1,a11)
                points+=20
        elif a15==2:
                sql="Insert into soulelement values(%s,%s)"
                val=(q1,a12)
                points+=40
        elif a15==3:
                sql="Insert into soulelement values(%s,%s)"
                val=(q1,a13)
                points+=30
        elif a15==4:
                sql="Insert into soulelement values(%s,%s)"
                val=(q1,a14)
                points+=10
        else:
                print("Invalid option")
        mycursor.execute(sql,val)
        mydb.commit()

        q2="Q2) Which of these animals do you like the most ?" 
        print("\nQuestions\n"+q2)
        a21="1) Dogs! They're so adorable"
        a22="2) I really love horses,they're incredibly gracious and beautiful"
        a23="3) Butterflies! They're truly fascinating"
        a24="4) Dolphine! They're so smart and friendly"
        print("\nOptions\n"+a21+"\n"+a22+"\n"+a23+"\n"+a24)
        a25=eval(input("Enetr your option:\r"))
        if a25==1:
                sql="Insert into soulelement values(%s,%s)"
                val=(q2,a21)
                points+=40
        elif a25==2:
                sql="Insert into soulelement values(%s,%s)"
                val=(q2,a22)
                points+=10
        elif a25==3:
                sql="Insert into soulelement values(%s,%s)"
                val=(q2,a23)
                points+=20
        elif a25==4:
                sql="Insert into soulelement values(%s,%s)"
                val=(q2,a24)
                points+=30
        else:
                print("Invalid option")
        mycursor.execute(sql,val)
        mydb.commit()

        n=3
        qn="Q3) Which Color Combo do you like the most ?" 
        print("\nQuestions\n"+qn)
        an1="1) Black and Brown"
        an2="2) Nothing beats shades of blue and green together"
        an3="3) Red and Orange,Of Course"
        an4="4) Green and Purple is a killer combo!"
        print("\nOptions\n"+an1+"\n"+an2+"\n"+an3+"\n"+an4)
        an5=eval(input("Enetr your option:\r"))
        if an5==1:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an1)
                points+=40
        elif an5==2:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an2)
                points+=30
        elif an5==3:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an3)
                points+=10
        elif an5==4:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an4)
                points+=20
        else:
                print("Invalid option")
        mycursor.execute(sql,val)
        mydb.commit()
        
        n=4
        qn="Q4) What's your favorite movie genre ?" 
        print("\nQuestions\n"+qn)
        an1="1) Thriller,Mystery,Horror,whatever keeps me on the edge of my seat"
        an2="2) Probably comedies or action movies.I like good fun enetertainment"
        an3="3) I need adventure movies and romantic films to sweep me off my feet"
        an4="4) Nothing better than a touching drama or an educational documentary"
        print("\nOptions\n"+an1+"\n"+an2+"\n"+an3+"\n"+an4)
        an5=eval(input("Enetr your option:\r"))
        if an5==1:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an1)
                points+=30
        elif an5==2:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an2)
                points+=20
        elif an5==3:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an3)
                points+=10
        elif an5==4:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an4)
                points+=40
        else:
                print("Invalid option")
        mycursor.execute(sql,val)
        mydb.commit()

        n=5
        qn="Q5) How many friends do you have ?" 
        print("\nQuestions\n"+qn)
        an1="1) I've got a few different groups with a couple of people in each"
        an2="2) About 5-10 that I consider my pals"
        an3="3) Probably just 2 or 3 close friends"
        an4="4) I have a nicebig group of truly wonderful friends"
        print("\nOptions\n"+an1+"\n"+an2+"\n"+an3+"\n"+an4)
        an5=eval(input("Enetr your option:\r"))
        if an5==1:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an1)
                points+=10
        elif an5==2:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an2)
                points+=30
        elif an5==3:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an3)
                points+=40
        elif an5==4:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an4)
                points+=20
        else:
                print("Invalid option")
        mycursor.execute(sql,val)
        mydb.commit()

        n=6
        qn="Q6) Which of these music geners do you like more than the others ?" 
        print("\nQuestions\n"+qn)
        an1="1) Can't go wrong with some nice soft rock"
        an2="2) Heavy metal all the way!"
        an3="3) Classical music is all I need"
        an4="4) Just anything that's popular today.I love pretty much all the latest hits"
        print("\nOptions\n"+an1+"\n"+an2+"\n"+an3+"\n"+an4)
        an5=eval(input("Enetr your option:\r"))
        if an5==1:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an1)
                points+=20
        elif an5==2:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an2)
                points+=10
        elif an5==3:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an3)
                points+=40
        elif an5==4:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an4)
                points+=30
        else:
                print("Invalid option")
        mycursor.execute(sql,val)
        mydb.commit()

        n=7
        qn="Q7) Which magical charm would you like to have ?" 
        print("\nQuestions\n"+qn)
        an1="1) Something to make me completely free or etremely powerful"
        an2="2) Probably invincibility or immortality"
        an3="3) I want something that would bring me more attention and love"
        an4="4) I'D have to say wisdom or a unique skill of some sort"
        print("\nOptions\n"+an1+"\n"+an2+"\n"+an3+"\n"+an4)
        an5=eval(input("Enetr your option:\r"))
        if an5==1:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an1)
                points+=20
        elif an5==2:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an2)
                points+=30
        elif an5==3:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an3)
                points+=10
        elif an5==4:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an4)
                points+=40
        else:
                print("Invalid option")
        mycursor.execute(sql,val)
        mydb.commit()

        n=8
        qn="Q8) Let's hope this scenario won't ever happen to you.But if someone you love died,how would you handle it?" 
        print("\nQuestions\n"+qn)
        an1="1) I'D definitely grieve and cry for a very long time"
        an2="2) It would be hard but I'd try to accept that they're gone"
        an3="3) I'D try to remember all the good times we had together and focus on the positive to make the pain go away"
        an4="4) I'D give it some time to sink in and let myself feel all the emotions that would come with it"
        print("\nOptions\n"+an1+"\n"+an2+"\n"+an3+"\n"+an4)
        an5=eval(input("Enetr your option:\r"))
        if an5==1:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an1)
                points+=10
        elif an5==2:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an2)
                points+=40
        elif an5==3:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an3)
                points+=20
        elif an5==4:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an4)
                points+=30
        else:
                print("Invalid option")
        mycursor.execute(sql,val)
        mydb.commit()

        n=9
        qn="Q9) If you had 1 Million Dollars,what would you do with it?" 
        print("\nQuestions\n"+qn)
        an1="1) I'D donate it to a charity.A lot of people need this money way more than I do"
        an2="2) I'D save it,of course"
        an3="3) Oh,I'd spend it all with pleasure"
        an4="4) I'D give half the money to my family and use the other half for a good cause,maybe help the homeless.I think that would be fair"
        print("\nOptions\n"+an1+"\n"+an2+"\n"+an3+"\n"+an4)
        an5=eval(input("Enetr your option:\r"))
        if an5==1:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an1)
                points+=20
        elif an5==2:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an2)
                points+=40
        elif an5==3:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an3)
                points+=10
        elif an5==4:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an4)
                points+=30
        else:
                print("Invalid option")
        mycursor.execute(sql,val)
        mydb.commit()

        n=10
        qn="Q10) How would you describe your life?" 
        print("\nQuestions\n"+qn)
        an1="1) Probably just a big spotlight of attention and i don't mind it all"
        an2="2) Full of fun and positive vibes and even a little flirty at times"
        an3="3) Hmm...Emotionally well-rounded.Yeah,that describes it alright"
        an4="4) Maybe a big modest but filled with great love and that's all that matters"
        print("\nOptions\n"+an1+"\n"+an2+"\n"+an3+"\n"+an4)
        an5=eval(input("Enetr your option:\r"))
        if an5==1:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an1)
                points+=40
        elif an5==2:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an2)
                points+=30
        elif an5==3:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an3)
                points+=20
        elif an5==4:
                sql="Insert into soulelement values(%s,%s)"
                val=(qn,an4)
                points+=10
        else:
                print("Invalid option")
        mycursor.execute(sql,val)
        mydb.commit()

        if points>=100 or points<=160:
                mycursor.execute("Insert into soulelement (answers) values('Your soul element is FIRE')")
                print("Your soul element is FIRE")
        elif points>=170 or points<=240:
                mycursor.execute("Insert into soulelement (answers) values('Your soul element is AIR')")
                print("Your soul element is AIR")
        elif points>=250 or points<=320:
                mycursor.execute("Insert into soulelement (answers) values('Your soul element is WATER')")
                print("Your soul element is WATER")
        mydb.commit()

def College():
        mycursor.execute("Create table College(Questions varchar(250),Answers varchar(250))")
        q1="Q1) What is the name of your College?" 
        print("\nQuestions\n"+q1)
        a1=str(input("Ans:\r"))
        sql="Insert into College values(%s,%s)"
        val=(q1,a1)
        mycursor.execute(sql,val)
        mydb.commit()

        q2="Q2) What is your Department?" 
        print(q2)
        a2=str(input("Ans:\r"))
        sql="Insert into College values(%s,%s)"
        val=(q2,a2)
        mycursor.execute(sql,val)
        mydb.commit()

        q3="Q3) What is your branch?" 
        print(q3)
        a3=str(input("Ans:\r"))
        sql="Insert into college values(%s,%s)"
        val=(q3,a3)
        mycursor.execute(sql,val)
        mydb.commit()

def Intro():
        mycursor.execute("Create table Intro(Questions varchar(250),Answers varchar(250))")
        q1="Q1) What is your name?" 
        print("\nQuestions\n"+q1)
        a1=str(input("Ans:\r"))
        sql="Insert into Intro values(%s,%s)"
        val=(q1,a1)
        mycursor.execute(sql,val)
        mydb.commit()

        q2="Q2) What is your Qualification?" 
        print(q2)
        a2=str(input("Ans:\r"))
        sql="Insert into Intro values(%s,%s)"
        val=(q2,a2)
        mycursor.execute(sql,val)
        mydb.commit()

        q3="Q3) What is your Profession?" 
        print(q3)
        a3=str(input("Ans:\r"))
        sql="Insert into Intro values(%s,%s)"
        val=(q3,a3)
        mycursor.execute(sql,val)
        mydb.commit()




print("1)New User\n2)Existing User")
x=eval(input('Enter your option:\r'))

if x==1:
    q=str(input('\nEnter your new username:\r'))
    w=str(input('Enter your new password:\r'))
    mycursor.execute("Use Main")
    mycursor.execute("Select username from Main where username='"+q+"'")
    for e in mycursor:
            print("This username already exists")
            exit()
    sql="Insert into Main Values(%s,%s)"
    val=(q,w)
    mycursor.execute(sql,val)
    mydb.commit()
    mycursor.execute("Create database\t"+q)
    mycursor.execute("use\t"+q)
    print("\nSelect the topic:\n1)Know your soul element\n2)College\n3)Intro")
    x1=eval(input("Enter your choice:\r"))
    if x1==1:
        soulelement()
        print("\n1)Continue\n2)Exit")
        x11=eval(input("Enter your choice:\r"))
        if x11==1:
                print("\nSelect the topic:\n1)College\n2)Intro")
                x111=eval(input("Enter your choice:\r"))
                if x111==1:
                        College()
                        print("\n1)Answer questions on 'Intro'\n2)Exit")
                        x1111=eval(input("Enter your choice:\r"))
                        if x1111==1:
                                Intro()
                                print("END")
                        if x1111==2:
                                print("END")
                if x111==2:
                        Intro()
                        print("\n1)Answer questions on 'College'\n2)Exit")
                        x1112=eval(input("Enter your choice:\r"))
                        if x1112==1:
                                College()
                                print("END")
                        if x1112==2:
                                print("END")
        if x11==2:
                print("END")




    if x1==2:
        College()
        print("\n1)Continue\n2)Exit")
        x12=eval(input("Enter your choice:\r"))
        if x12==1:
                print("\nSelect the topic:\n1)Know your soul element\n2)Intro")
                x121=eval(input("Enter your choice:\r"))
                if x121==1:
                        soulelement()
                        print("\n1)Answer questions on 'Intro'\n2)Exit")
                        x1211=eval(input("Enter your choice:\r"))
                        if x1211==1:
                                Intro()
                                print("END")
                        if x1211==2:
                                print("END")
                if x121==2:
                        Intro()
                        print("\n1)Answer questions on 'Know your soul element'\n2)Exit")
                        x1212=eval(input("Enter your choice:\r"))
                        if x1212==1:
                                soulelement()
                                print("END")
                        if x1212==2:
                                print("END")
        if x12==2:
                print("END")




    if x1==3:
        Intro()
        print("\n1)Continue\n2)Exit")
        x13=eval(input("Enter your choice:\r"))
        if x13==1:
                print("\nSelect the topic:\n1)College\n2)Know your soul element")
                x131=eval(input("Enter your choice:\r"))
                if x131==1:
                        College()
                        print("\n1)Answer quiz 'Know your soul element'\n2)Exit")
                        x1311=eval(input("Enter your choice:\r"))
                        if x1311==1:
                                soulelement()
                                print("END")
                        if x1311==2:
                                print("END")
                if x131==2:
                        soulelement()
                        print("\n1)Answer questions on 'College'\n2)Exit")
                        x1312=eval(input("Enter your choice:\r"))
                        if x1312==1:
                                College()
                                print("END")
                        if x1312==2:
                                print("END")
        if x13==2:
                print("END")




if x==2:
        q=str(input('\nEnter your username:\r'))
        w=str(input('Enter your password:\r'))
        mycursor.execute("Use Main")
        sql="Select * from Main where username=%s and password=%s"
        val=(q,w)
        mycursor.execute(sql,val)
        for e in mycursor:
                if e!='':
                        print("\nAccess Granted")
                        mycursor.execute("Use\r"+q)
                        for i in range(1,4):
                                print("\n1)Check old answers\n2)Exit")
                                x2=eval(input("Enter your choice:\r"))
                                if x2==1:
                                        mycursor.execute("Show tables")
                                        a=0
                                        print("\nSelect the topic:")
                                        for e in mycursor:
                                                z=''.join(e)
                                                a+=1
                                                print(str(a)+")"+z)
                                        x21=str(input("Type the topic(case sensitive):\r"))
                                        if x21=='soulelement':
                                                mycursor.execute("Select questions from soulelement")
                                                print("\nQuestions")
                                                for e in mycursor:
                                                        z=''.join(e)
                                                        print(z)
                                                mycursor.execute("Select answers from soulelement")
                                                print("\nAnswers")
                                                s=0
                                                for i in mycursor:
                                                        c=''.join(i)
                                                        s+=1
                                                        print("Ans"+str(s)+":\r"+c)
                                        if x21=='college':
                                                mycursor.execute("Select questions from college")
                                                print("\nQuestions")
                                                for e in mycursor:
                                                        z=''.join(e)
                                                        print(z)
                                                mycursor.execute("Select answers from college")
                                                print("\nAnswers")
                                                s=0
                                                for i in mycursor:
                                                        c=''.join(i)
                                                        s+=1
                                                        print("Ans"+str(s)+":"+c)
                                        if x21=='intro':
                                                mycursor.execute("Select questions from intro")
                                                print("\nQuestions")
                                                for e in mycursor:
                                                        z=''.join(e)
                                                        print(z)
                                                mycursor.execute("Select answers from intro")
                                                print("\nAnswers")
                                                s=0
                                                for i in mycursor:
                                                        c=''.join(i)
                                                        s+=1
                                                        print("Ans"+str(s)+":"+c)
                                if x2==2:
                                        print("End")
                                        break
