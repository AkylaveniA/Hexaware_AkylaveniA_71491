class Clerk:
    salary=15000
    desig="CLERK"

    def __init__(self):
        self.uid=input("Enter ID : ")
        self.name=input("Enter name : ")
        self.age=input("Enter age : ")

    def display(self):
        print("Clerk Details.......................!")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age :",self.age)
        print("Salary :",self.salary)
        print("Designation :",self.desig)

    def salaryrise(self):
        print("Clerk Salary increment Details......!")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age :",self.age)
        print("Salary :",self.salary+2000)
        print("Designation :",self.desig)

class Developer:
    salary=20000
    desig="DEVELOPER"

    def __init__(self):
        self.uid=input("Enter ID : ")
        self.name=input("Enter name : ")
        self.age=input("Enter age : ")

    def display(self):
        print("\nDeveloper Details..................!")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age :",self.age)
        print("Salary :",self.salary)
        print("Designation :",self.desig)

    def salaryrise(self):
        print("\nDeveloper Salary increment Details......!")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age :",self.age)
        print("Salary :",self.salary+2000)
        print("Designation :",self.desig)

class Manager:
    salary=25000
    desig="MANAGER"

    def __init__(self):
        self.uid=input("Enter ID : ")
        self.name=input("Enter name : ")
        self.age=input("Enter age : ")

    def display(self):
        print("\nManager Details.......................!")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age :",self.age)
        print("Salary :",self.salary)
        print("Designation :",self.desig)

    def salaryrise(self):
        print("\nManager Salary increment Details......!")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age :",self.age)
        print("Salary :",self.salary+2000)
        print("Designation :",self.desig)

class Tester:
    salary=30000
    desig="TESTER"

    def __init__(self):
        self.uid=input("Enter ID : ")
        self.name=input("Enter name : ")
        self.age=input("Enter age : ")

    def display(self):
        print("\nTester Details.......................!")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age :",self.age)
        print("Salary :",self.salary)
        print("Designation :",self.desig)

    def salaryrise(self):
        print("\nTester Salary increment Details........!")
        print("Name :",self.name)
        print("ID :",self.uid)
        print("Age :",self.age)
        print("Salary :",self.salary+2000)
        print("Designation :",self.desig)

opt1=0
while(opt1!=4):
    print("-------------------------------------------------------------------")
    print("1)Create\n2)Display\n3)Salary rise\n4)Exit\n")
    opt1=int(input("Enter your choice : "))
    print("-------------------------------------------------------------------")
    if(opt1==1):
        opt2=0
        while(opt2!=5):
            print("-------------------------------------------------------------------")
            print("1)Clerk\n2)Developer\n3)Manager\n4)Tester\n5)Exit\n")
            opt2=int(input("Enter your choice : "))
            print("-------------------------------------------------------------------")
            if(opt2==1):
                print("Clerk..........")
                c=Clerk()
            if(opt2==2):
                print("Developer..........")
                d=Developer()
            if(opt2==3):
                print("Manager..........")
                m=Manager()
            if(opt2==4):
                print("Tester..........")
                t=Tester()
    if(opt1==2):
        c.display()
        d.display()
        m.display()
        t.display()
    if(opt1==3):
        c.salaryrise()
        d.salaryrise()
        m.salaryrise()
        t.salaryrise()
        


