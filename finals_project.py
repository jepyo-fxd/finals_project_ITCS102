
user_data = {}
accounts = {}
#activity1
def hello_world(y): 
    
    print()
    print(f"hello {y}, did you know that printing 'hello world' in python is very common in programming")
    print("Hello world")
    print()
    print("**print()** is a built in function in python, just insert quotation marks inside the the parentheses("")")
    


def activity2(): 
    x = input("enter your name: ")
    y = input("enter your age : ")
    z = input("enter your hobby : ")
    yy = input("enter your goals : ")
    print()
    print(f"hello my name is {x}, and I'm {y} years old. my favorite hobby is {z}, and the goal i root the most is {yy}")
    print()
    

def activity3(): 
    # Collecting user information
    name = input("PLEASE INPUT YOUR NAME: ")
    nickname = input("PLEASE INPUT YOUR NICKNAME: ")
    age = input("PLEASE INPUT YOUR AGE: ")
    birth_month = input("PLEASE INPUT YOUR BIRTHMONTH: ")
    birth_day = input("PLEASE INPUT YOUR BIRTHDAY: ")
    birth_year = input("PLEASE INPUT YOUR BIRTHYEAR: ")
    gender = input("PLEASE INPUT YOUR GENDER: ")
    address = input("PLEASE INPUT YOUR ADDRESS: ")
    nationality = input("PLEASE INPUT YOUR NATIONALITY: ")
    is_married = False  # Default value
    civil_status = input("PLEASE INPUT YOUR CIVIL STATUS: ")
    religion = input("PLEASE INPUT YOUR RELIGION: ")
    citizenship = input("PLEASE INPUT YOUR CITIZENSHIP: ")
    height = input("PLEASE INPUT YOUR HEIGHT: ")
    weight = input("PLEASE INPUT YOUR WEIGHT: ")
    father_name = input("PLEASE INPUT YOUR FATHER'S NAME: ")
    father_occupation = input("PLEASE INPUT YOUR FATHER'S OCCUPATION: ")
    father_contact = input("PLEASE INPUT YOUR FATHER'S CONTACT NUMBER: ")
    mother_name = input("PLEASE INPUT YOUR MOTHER'S NAME: ")
    mother_occupation = input("PLEASE INPUT YOUR MOTHER'S OCCUPATION: ")
    mother_contact = input("PLEASE INPUT YOUR MOTHER'S CONTACT NUMBER: ")
    elementary = input("PLEASE INPUT YOUR ELEMENTARY SCHOOL: ")
    elementary_year_start = input("PLEASE INPUT THE YEAR YOU STARTED ELEMENTARY: ")
    elementary_year_end = input("PLEASE INPUT THE YEAR YOU ENDED ELEMENTARY: ")
    high_school = input("PLEASE INPUT YOUR HIGH SCHOOL: ")
    high_school_year_start = input("PLEASE INPUT THE YEAR YOU STARTED HIGH SCHOOL: ")
    high_school_year_end = input("PLEASE INPUT THE YEAR YOU ENDED HIGH SCHOOL: ")
    college = input("PLEASE INPUT YOUR COLLEGE: ")
    course = input("PLEASE INPUT YOUR COURSE: ")
    skills = input("PLEASE INPUT YOUR SKILLS: ")

    # displaying the collected information
    print(f"""
    My name is {name}, and I am often referred to as {nickname}.
    I am {age} years old, born in {birth_month} on {birth_day}, {birth_year}.
    I currently reside at {address}.
    I am {gender} by gender, and my religion is {religion}.
    My nationality is {nationality}, and I hold {citizenship} citizenship.
    It is {is_married} that I am married, and my civil status is {civil_status}.
    My height is {height} cm, and I weigh {weight} kg.

    My father is {father_name}, who works as a {father_occupation}.
    He can be reached at {father_contact}.
    My mother is {mother_name}, who is employed as a {mother_occupation}.
    She can be reached at {mother_contact}.

    In terms of my educational background:
    - I completed my elementary education at {elementary} from {elementary_year_start} to {elementary_year_end}.
    - I then attended high school at {high_school} from {high_school_year_start} to {high_school_year_end}.
    - I pursued higher education at {college}, where I studied {course}.

    I have developed skills in {skills}. Developing these skills will help me navigate complex situations, enhance my professional growth, and contribute more effectively to achieving my goals.
    """)
 

def activity4(): #arithmetic
    A = eval(input("Enter a number: "))
    B = eval(input("Enter another number: "))

    C = A + B
    D = A - B
    E = A * B
    F = A / B
    G = A ** B

    
    print(f"The Sum of {A} and {B}, is {C}")
    print(f"The Difference of {A} and {B}, is {D}")
    print(f"The product of {A} and {B}, is {E}")
    print(f"The Quotient of {A} and {B}, is {F}")
    print(f"{A} Exponent by {B}, is {G}")
    




def activity5(): #arithmetic operations
    print()
    x = float(input("Enter a temperature: "))
    y = (x - 32)*5/9
    print(f"The conversion  of degrees fahrenheit is {round(y,2)} degrees celcius")
   

def activity6():
    x = 5
    print(x)
    x += 10
    print(x)
    x += 15
    print(x)
    x += 20
    print(x)
    print()
    


def activity7(): 
    AA =input("What's your name, Miner?: ")
    print("\n")
    A = 0
    B = input("Have you mined today?: ")
    print("\n")

    if B.upper() == "YES":
        C = eval(input(" How many golds have youe mined? :"))
        print("\n")
        D = A + C
        print(f"Congrats, {AA}. you have mined {D} golds, today!")

    elif B.upper() != "YES":
        print("\n")
        print(f"That's unfortunate, {AA}.you've mined {A} golds ")
        print("unfortunatele you mined no golds today")
   

# def activity8(): 
# function to create a new user
def create_user():
    username = input("Enter a username: ")
    if username in user_data:
        print("Username already exists. Please choose another.")
        return
    password = input("Enter a password: ")
    user_data[username] = password
    print("User created successfully!")
    

# function to log in
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if user_data.get(username) == password:
        print()
        print(f"Login successful! Welcome,   {username}  !")
    else:
        print("Invalid username or password.")
        
def activity9(): #comparison
    A = eval(input("Enter Age :"))
    if A >= 1 and A<= 7:
        print("toddler")
    elif A >= 8 and A <= 13:
        print("pre teen")
    elif A >= 14 and A <= 18:
        print("teenager")
    elif A >= 19 and A <= 31:
        print("early adulthood")
    elif A >= 32 and A <= 45:
        print("mid adulthood")
    elif A >= 46 and A <= 59:
        print("post adulthood")
    elif A >= 60 and A <= 100:
        print("senior")
    elif A >= 100:
        print("Ancient")
    
def activity10(): #if else
    name = input("Enter Your Name: ")

    isStudent = input("Are you a student of DLL(Yes/No): ")

    if isStudent.lower()=="yes":
        print("Welcome to the DLL BSIT Scholarship form") 
        GG = input("Are you from Brgy. Talao-Talao? (yes/no):")
        if GG.lower()=="yes":
            print("Please fillup the second form")
            yearlevel = input("What year are you currently enrolled?\nF-Freshnen\nS-Sophomore\nJ-Junior\nR-Senior\nPlease input your answer here: ")
        

            if yearlevel.lower() == 'f':
                print(f"Hi {name}, Freshmen, Welcome to DLL")

            elif yearlevel.lower() == 's': 
                print(f"Hi {name}, Sophomore, Welcome to DLL")

            elif yearlevel.lower() == 'j': 
                print(f"Hi {name}, Junior, Welcome to DLL")

            elif yearlevel.lower() == 'r': 
                print(f"Hi {name}, Senior, Welcome to DLL")

            else:
                print("Invalid Option")
            IsNeeded = input("Would you like to apply for a scholarship? (yes/no): ")

            if IsNeeded.lower() == "yes":
                print("Scholarship approved")
            else:
             print("Unfortunately, this scholarship grant are only for residents of Talao-Talao only")
            print("Your form has been successfully submitted")
            print()
        
    
def activity11(): #for loop
    for x in range(1,5):
        print("input loop")
        name = input("Hi! Please input your name: ")
        print(f"Hi {name}")

    
def activity12(): #for loop
    for a in range(1,111):
        print(f"Number. {a}")

def activity13():
    sum = 1
    num=int(input('Enter a number: '))

    for x in range (num,0,-1):
        sum *= x
    print(f"The factorial of {num} is {sum}")


def activity14(): #for loop
    for x in range(0,11):
        print(x,end="")
        for y in range(0,11):
            print(" * ",end="")
        print()
    
def activity15(): #for loop
    for x in range(1,11,1):
        print(end="")

        for y in range(x,11,1):
            print(end=" ")
        print("* " * x)

        for b in range(11,x,-1):
            print(end=" ")
        print("* " * x)

    
def activity16(): #for loop
    t = int(input("Enter a number range: "))
    for x in range(1,t):

        for a in range(1,x,1):
            print(" ",end="  ")

        for b in range(t,x,-1):
            print("* ",end=" ")
    
def activity17(): #for loop
    A = int(input("Enter a Value: "))
    for x in range(1,11):
        for y in range(1,A+1):
            print(f"{x} x {y} = {x*y}",end=" \t")
        print() 

    
def activity18(): #for loop
    A = int(input("Enter a value: "))
    for x in range(1,6):
        for r in range(1,A+1):
            for y in range(1,x+1):
                print("*",end=" ")
            for z in range(x,6):
                print(" ",end=" ")

   
def activity19(): #while loop
    tama = True

    while tama == True:
        ask = input("Enter your name: ")
        if ask.lower() == "stop":
            break
            ask == False
    
def activity20():  #hybrid loop
    import os
    tama = True
    no = 0
    while tama == True:
        ask = input("Would you like to continue? (yes/no): ")
        if ask.lower() == "no":
            print("Program Terminated")
            break
            ask == False
        else:
            os.system('cls')
            for x in range(1,6):
                no += 1
                for r in range (1,no+1):
                    for y in range(1,x+1):
                        print("*",end=" ")
                    for z in range(5,x,-1):
                        print(" ",end= " ")
                print()
            continue        


#activity 21 whole structure
def pang_hi():
    print("HI IT1C")

def pang_hi_v2(name):
    print(f"Hello {name}")

def termi():
    print("PROGRAM TERMINATED")

def activity_2():
    number1 = eval (input("enter a number--->" ))
    number2 = eval (input("enter another number--->" ))
    answer = (number1 + number2)
    print(f"The sum of {number1} and {number2} is {answer}")

def activity21(): # functions
    tuloy =  True
    while tuloy == True:
        ask = input("Enter a name---> ")

        if ask.lower() != "stop":
            pang_hi_v2(ask)
            if ask == "2":
                activity_2()
                continue
        else:
            termi()
            break

def activity22():

    pass


def activity23(number):  # program calculate factorial
    """This function computes the factorial of any number given."""
    fact = 1
    for x in range(number, 0, -1):  # loop from the number down to 1
        fact *= x
    return fact  # return the factorial result

# call the function and print the result
print(f"The factorial of 13 is {activity23(13)}")


def activity24(y): #dictionary
    x = {"past":"Yesterday","present":"Today","future":"Tommorow"}
    print(x[y])

def activity25(): #list

    courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]

    courses.remove("Delete w/o index")
    courses.pop()
    courses.append("DHRS")
    courses.insert(0, "ABELS")

    print(courses)

#====================================================================== END OF ACTIVITIES ========================================================================
#===================================================================START OF CODE_CHALLENGES======================================================================

def bato_bato_pick():
    x = input("enter a guess: ")

def code_challenge1(): #print
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t***\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t*****\n\n\t\t\t\t\t\t\t\t\t\t\t\t*******\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t*****\t\t\t\t\t\t\t\t\t\t\t\t\t\t***\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*")

def code_challenge2(): #print
    print()
    name = input("Please insert your name >")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t*\n\n\t\t\t\t\t\t\t\t\t\t*\t*\t*\n\n\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\t\t\t\t\t\t\t\t\t\t_________________\n\t\t\t\t\t\t\t\t*\t*\t|\t\b\b" + name + "\t|\t*\t*\n\t\t\t\t\t\t\t\t\t\t-----------------\n\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\n\n\t\t\t\t\t\t\t\t\t\t*\t*\t*\n\n\t\t\t\t\t\t\t\t\t\t\t*\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
def code_challenge3(): #arithmetic operators
    x = eval(input("enter a number: "))
    y = eval(input("enter a number: "))
    z = x + y
    print(f"the sum of {x} and {y} is {z}")
    print()
   
def code_challenge4(): #variables/concatenation and arithmetic operators
    A = eval(input("Enter a number: "))
    B = eval(input("Enter another number: "))

    C = A + B
    D = A - B
    E = A * B
    F = A / B
    G = A ** B
    H = A % B
    I = A // B

    print(f"The Sum of {A} and {B}, is {C}")
    print(f"The Difference of {A} and {B}, is {D}")
    print(f"The product of {A} and {B}, is {E}")
    print(f"The Quotient of {A} and {B}, is {F}")
    print(f"{A} Exponent by {B}, is {G}")
    print(f"The Reminder of {A} and {B},is {H}")
    print(f"The Floor Division of {A} and {B}, is {I}")
    

def code_challenge5(P): #assignment operators
    
    print()
    A = P//1000
    AA = P%1000

    B = AA//500
    BB = AA%500

    C = BB//200
    CC = BB%200

    D = CC//100
    DD = CC%100

    E = DD//50
    EE = DD%50

    F = EE//20
    FF = EE%20

    G = FF//10
    GG = FF%10

    H = GG//5
    HH = GG%5

    I = HH//1
    II = HH%1

    print(f"THANK YOU,",name.upper(),"! The breakdown of your deposit(₱",P,"), is shown below:")
    print()
    print("1000---",A)
    print("500----",B)
    print("200----",C)
    print("100----",D)
    print("50-----",E)
    print("20-----",F)
    print("10-----",G)
    print("5------",H)
    print("1------",I)
    print() 

    

def code_challenge6():  #comparison operators/if-elif-else structure
    n = input("Enter Your Name---------> ")
    print()
    A = float(input("Enter Your Prelim Grade ------> "))
    B = float(input("Enter Your Midterm Grade ------> "))
    C = float(input("Enter Your Semi-finals Grade ------> "))
    D = float(input("Enter Your Finals Grade ------> "))
    E = float(input("Enter Your Quiz Grade ------> "))
    F = float(input("Enter Your Project Grade ------> "))
    print()
    if (A >=65 and A <=100 )and(B >=65 and B <=100 )and(C >=65 and C <=100 )and(D >=65 and D <=100 )and(E >=65 and E <=100 )and(F >=65 and F <=100 ):
        g = (A *.15)+(B *.15)+(C *.15)+(D *.15)+(E *.25)+(F *.15)
        if g >= 75 and g <= 89 :#passed
            print("Congratulations!",n," You Passed With an average of",g," keep it up") 
        elif g >= 85 and g <=89:#acad award
            print("Congratulations!",n," You Passed With academic award with an average of",g," keep it up")  
        elif g >= 90 and g <= 94:#with honors
            print("Congratultions!!,",n,"You Passed and with honors with an average of ",g)
        elif g >= 95 and g <=97:#with high honors
            print("Congratultions!!!,",n,"You Passed and with high honors with an average of ",g)
        elif g>= 98 and g <=100:#with highest honors
            print("Congratultions!!!!,",n,"You Passed and with highest honors!! with an average of ",g)  
    elif A>100 and B>100 and C>100 and D>100 and E>100 and F >100:
        print("You Can't Exceed Over 100, 100 is the maximum")          
    else :
        print("Unfortunately You din't meet the requirements",n," better luck nextime!")

def code_challenge7(): #arithmetic/ if else/ assignment/ comparison
    # Grocery Purchase Program

    A = input("DID YOU BUY A GROCERY GOOD/s (yes/no)? ").strip().lower()

    if A == "yes":
        B = input("Name of the goods: ")
        C = float(input("Price of the goods: "))
        D = int(input("Age: "))
        E = float(input("Amount Given: "))
        print()

        tax_rate = 0.123
        discount_rate = 0.052 if D >= 60 else 0.0  # 5.2% discount for seniors

        # calculate tax and total price
        tax_amount = C * tax_rate
        total_price = C + tax_amount

        # apply discount for seniors
        discount_amount = total_price * discount_rate
        final_price = total_price - discount_amount

        # calculate change
        change = E - final_price

        # print purchase details
        print(f"Hi, customer! You purchased '{B}' with a price of PHP {C:.2f}.")
        print(f"12.3% tax added: PHP {tax_amount:.2f}")
        if D >= 60:
            print(f"Senior discount (5.2%): PHP {discount_amount:.2f}")
            print(f"Total amount: PHP {final_price:.2f}")
            print(f"Amount given: PHP {E:.2f}")
            print(f"Change: PHP {change:.2f}")

        # ask to print the receipt
        rt = input("Do you want us to print your receipt? (yes/no): ").strip().lower()
        if rt == "yes":
            print("\n========== RECEIPT ==========")
            print(f"Name of Goods: {B}")
            print(f"Price of Goods: PHP {C:.2f}")
            print(f"Tax (12.3%): PHP {tax_amount:.2f}")
            if D >= 60:
                print(f"Senior Discount: PHP {discount_amount:.2f}")
            print(f"Total Amount: PHP {final_price:.2f}")
            print(f"Amount Given: PHP {E:.2f}")
            print(f"Change: PHP {change:.2f}")
            print("=============================")
        else:
            print("Thank you for your purchase, customer!")
    else:
        print("Thank you for stopping by!")
def code_challenge8():
    sum = 0
    odd = 0
    even = 0

    for j in range(1,11):
        num = int(input(f"\nEnter a Number {j}:  "))
        sum += num 
        if num % 2 == 0:
            odd+=num
        else:
            even+=num

    print(f"\nThe sum of all given numbers is {sum}")
    print(f"\nThe even of all given numbers is {even}")
    print(f"\nThe odd of all given numbers is {odd}")


def code_challenge9(): #for loop
    for x in range(10,0,-1):
        for y in range(10,x,-1):
            print(" ",end=" ")
        print("* "* x)

def code_challenge10():  #for loop
    for x in range (6, 1, -1):
        for y in range(x, 1, - 1):
            print(" ", end =" ")
        for z in range(x, 7, 1):
            print("*",end=" ")
        for j in range (x, 6, 1):
            print("^",end=" ")
        print()
            
    for x in range (1,7):
        for y in range(1, x, 1):
            print(" ", end =" ")
        for z in range(7, x, -1):
            print("^",end=" ")
        for j in range (6, x, -1):
            print("*",end=" ")
        print()

def code_challenge11():  #for loop
    for x in range (7, 1, -1):
        for y in range(1, x + 1):
            print(" ", end =" ")
        for z in range(7, x,- 1):
            print("*",end=" ")
        for j in range (5, x ,- 1):
            print("*",end=" ")
        print()
            
    for x in range (1,7):
        for y in range(1, x + 1):
            print(" ", end =" ")
        for z in range(4, x, -1):
            print("*",end=" ")
        for j in range (6, x, -1):
            print("*",end=" ")
        print() 

def code_challenge12():  #for loop
    for j in range(6,1-1):
        for v in range(1,j):
            print(" ",end=" ")
        for q in range(7,j -1):
            print("*",end=" ")
        for q in range(6,j -1):
            print("*",end=" ")
        print()

    for t in range(1,7):
        for p in range(1,5):
            print(" ",end=" ")
        for s in range(1,4):
            print("*",end=" ")
        print() 

def code_challenge13():  #for loop
    for x in range (6, 1, -1):
        for y in range(x, 1, - 1):
            print(" ", end =" ")
        for z in range(x, 7, +1):
            print(z,end=" ")
        for j in range (x, 6, 1):
            print(j,end=" ")
        print()
            
    for x in range (1,7):
        for y in range(1, x, 1):
            print(" ", end =" ")
        for z in range(7, x, -1):
            print(z,end=" ")
        for j in range (x, 6, +1):
            print(j,end=" ")
        print()

def code_challenge14():  #while Loop
    x = True
    a = 0
    while x:
        try:
            number = int(input("Enter a number ---> "))
            if number == 0:
                print("Program Terminated")
                print(f"The total of the numbers you entered is {a}")
                break
            else:
                a += number
        except ValueError:
            print("Invalid input. Please enter an integer.")


def code_challenge15(): #hybrid Loop
    import os

    isContinue = True
    no = 0
    while isContinue == True:
        ask = input("Would you like to add another triangle (yes / no )--> ")

        if ask.lower() == "no":
            print("PROGRAM TERMINATED")
            break
            isContinue = False
        elif ask.lower() == "yes":
            os.system('cls')
            no += 1
            for x in range (1, 6):
                for r in range (1 , no + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
        else:
            print("INVALID ANSWER it's only (yes/no)")
            continue


##code_challenge16(): function
def denomination(amount):
    print("\nDenomination Breakdown:")
    A = amount // 1000
    AA = amount % 1000

    B = AA // 500
    BB = AA % 500

    C = BB // 200
    CC = BB % 200

    D = CC // 100
    DD = CC % 100

    E = DD // 50
    EE = DD % 50

    F = EE // 20
    FF = EE % 20

    G = FF // 10
    GG = FF % 10

    H = GG // 5
    HH = GG % 5

    I = HH // 1

    print("1000---", A)
    print("500----", B)
    print("200----", C)
    print("100----", D)
    print("50-----", E)
    print("20-----", F)
    print("10-----", G)
    print("5------", H)
    print("1------", I)




def account():
    x = input("Enter an account name: ")
    if x in accounts:
        print("Account already exists!")
    else:
        accounts[x] = 0
        print(f"Account created successfully for {x}.")


def deposit():
    x = input("Enter your account name: ")
    if x in accounts:
        try:
            amount = int(input("Enter amount to deposit : "))
            if amount > 0:
                accounts[x] += amount
                print(f"Deposited {amount} successfully. New balance: {accounts[x]}")
                denomination(amount)
            else:
                print("Amount must be positive!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
    else:
        print("Account not found!")


def withdrawal():
    x = input("Enter your account name: ")
    if x in accounts:
        try:
            amount = int(input("Enter amount to withdraw : "))
            if 0 < amount <= accounts[x]:
                accounts[x] -= amount
                print(f"Withdrawn {amount} successfully. Remaining balance: {accounts[x]}")
                denomination(amount)
            else:
                print("Insufficient funds or invalid amount!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
    else:
        print("Account not found!")


def check_balance():
    x = input("Enter your username: ")
    if x in accounts:
        print(f"Your balance: {accounts[x]}")
    else:
        print("Account not found!")

def menu():
    while True:
        print("|————————————————————————————————————————————————————————————————————|————————————————————————————————————————————————————————————————————|")
        print("|                                                                                                                                         |")
        print("|                                                          WELKAM SA AKONG PROGRAM                                                        |")
        print("|                                                                                                                                         |")
        print("|————————————————————————————————————————————————————————————————————|————————————————————————————————————————————————————————————————————|")
        print("|                                                                    |                                                                    |")
        print("|                            ACTIVITIES                              |                         CODE CHALLENGES                            |")
        print("|                                                                    |                                                                    |")
        print("|       1 - ACTIVITY 1                        14 - ACTIVITY 14       |       C1 - CODE CHALLENGE 1          C14 - CODE CHALLENGE 14       |")
        print("|                                                                    |                                                                    |")
        print("|       2 - ACTIVITY 2                        15 - ACTIVITY 15       |       C2 - CODE CHALLENGE 2          C15 - CODE CHALLENGE 15       |")
        print("|                                                                    |                                                                    |")
        print("|       3 - ACTIVITY 3                        16 - ACTIVITY 16       |       C3 - CODE CHALLENGE 3          C16 - CODE CHALLENGE 16       |")
        print("|                                                                    |                                                                    |")
        print("|       4 - ACTIVITY 4                        17 - ACTIVITY 17       |       C4 - CODE CHALLENGE 4                                        |")
        print("|                                                                    |                                                                    |")
        print("|       5 - ACTIVITY 5                        18 - ACTIVITY 18       |       C5 - CODE CHALLENGE 5                                        |")
        print("|                                                                    |                                                                    |")
        print("|       6 - ACTIVITY 6                        19 - ACTIVITY 19       |       C6 - CODE CHALLENGE 6                                        |")
        print("|                                                                    |                                                                    |")
        print("|       7 - ACTIVITY 7                        20 - ACTIVITY 20       |       C7 - CODE CHALLENGE 7                                        |")
        print("|                                                                    |                                                                    |")
        print("|       8 - ACTIVITY 8                        21 - ACTIVITY 21       |       C8 - CODE CHALLENGE 8                                        |")
        print("|                                                                    |                                                                    |")
        print("|       9 - ACTIVITY 9                        22 - ACTIVITY 22       |       C9 - CODE CHALLENGE 9                                        |")
        print("|                                                                    |                                                                    |")
        print("|       10 - ACTIVITY 10                      23 - ACTIVITY 23       |       C10 - CODE CHALLENGE 10                                      |")
        print("|                                                                    |                                                                    |")
        print("|       11 - ACTIVITY 11                      24 - ACTIVITY 24       |       C11 - CODE CHALLENGE 11                                      |")
        print("|                                                                    |                                                                    |")
        print("|       12 - ACTIVITY 12                      25 - ACTIVITY 25       |       C12 - CODE CHALLENGE 12                                      |")
        print("|                                                                    |                                                                    |")
        print("|       13 - ACTIVITY 13                                             |       C13 - CODE CHALLENGE 13                                      |")
        print("|                                                                    |                                                                    |")
        print("|————————————————————————————————————————————————————————————————————|————————————————————————————————————————————————————————————————————|")
        print("|   - TYPE THE NUMBER OF THE ACTIVITY YOU WANT TO CHECK OUT          |   - TYPE THE COMMAND OF THE CODE CHALLENGE YOU WANT TO CHECK OUT   |")
        print("|   - COMMAND ( 1-25 ('1'))                                          |   - COMMAND ( 1-16 ('1'))                                          |")
        print("|————————————————————————————————————————————————————————————————————|————————————————————————————————————————————————————————————————————|")
        
        pili = input("enter a number: ")
        if pili == "exit":
            break
     
        elif pili != "exit":
            if pili == "1":
                y = input(" enter your name here: ")
                hello_world(y)
                continue
            elif pili == "2":
                activity2()
                continue
            elif pili == "3":
                activity3()
                continue
            elif pili == "4":
                activity4()
                continue
            elif pili == "5":
                activity5()
                continue
            elif pili == "6":
                activity6()
                continue
            elif pili == "7":
                activity7()
                continue
            elif pili == "8":            
                    while True:
                        print("1. create user")
                        print("2. login")
                        print("0. exit")
                        print()
                        choice = input("enter a num: ")
                        if choice == "0":
                            break
                        elif choice == "1":
                                create_user()
                                continue
                        elif choice == "2":
                                login()
                                continue      
            
            elif pili == "9": 
                activity9()  
                continue             
            elif pili == "10":  
                activity10()
                continue  
            elif pili == "11":
                activity11()
                continue
            elif pili == "12":
                activity12()
                continue
            elif pili == "13":
                activity13()
                continue
            elif pili == "14":
                activity14()
                continue
            elif pili == "15":
                activity15()
                continue
            elif pili == "16":
                activity16()
                continue
            elif pili == "17":
                activity17()
                continue
            elif pili == "18":
                activity18()
                continue
            elif pili == "19":
                activity19()
                continue
            elif pili == "20":
                activity20()
                continue
            elif pili == "21":
                activity21()
                continue
            elif pili == "22":
                activity22()
                continue
            elif pili == "23":
                activity23()
                continue
            elif pili == "24":
                activity24()
                continue
            elif pili == "25":
                activity25()
                continue
            elif pili == "C1":
                code_challenge1()
                continue
            elif pili == "C2":
                code_challenge2()
                continue
            elif pili == "C3":
                code_challenge3()
                continue
            elif pili == "C4":
                code_challenge4()
                continue
            elif pili == "C5":
                code_challenge5()
                continue
            elif pili == "C6":
                code_challenge6()
                continue
            elif pili == "C7":
                code_challenge7()
                continue
            elif pili == "C8":
                code_challenge8()
                continue
            elif pili == "C9":
                code_challenge9()
                continue
            elif pili == "C10":
                code_challenge10()
                continue
            elif pili == "C11":
                code_challenge11()
                continue  
            elif pili == "C12":
                code_challenge12()
                continue
            elif pili == "C13":
                code_challenge13()
                continue
            elif pili == "C14":
                code_challenge14()
                continue
            elif pili == "C15":
                code_challenge15()
                continue
            elif pili == "C16":
                print("1. create account")
                print("2. deposit")
                print("3. withdrawal")
                print("4. check balance")
                choice = input("enter a command")
                if choice == "1":
                    account()
                    continue
                elif choice == "2":
                    deposit()
                    continue
                elif choice == "3":
                    withdrawal()
                    continue 
                elif choice == "4":
                    check_balance()
                    continue          
menu()                                                                                      