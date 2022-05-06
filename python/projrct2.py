class Emp:
    def __init__(self):
        self.uid=input("Enter ID : ")
        self.name=input("Enter name : ")
        self.age=input("Enter age : ")

    def display(self):
        print("\nEmp Details.......................!")
        records=[str(self.uid),self.name,str(self.age),str(self.salary),self.desig]
        f=open("prj2insert.txt","a")
        for line in records:
            f.write(line)
            f.write("\t")
        f.write("\n")
        f=open("prj2insert.txt","r")
        print(f.read())
        f.close()

    def salaryrise(self):
        records=[str(self.uid),self.name,str(self.age),str(self.salary+200),self.desig]
        f=open("prj2salary.txt","a")
        for line in records:
            f.write(line)
            f.write("\t")
        f.write("\n")
        f.close()

class Clerk(Emp):
    salary=15000
    desig="CLERK"    

class Developer(Emp):
    salary=20000
    desig="DEVELOPER"

class Manager(Emp):
    salary=25000
    desig="MANAGER"

class Tester(Emp):
    salary=30000
    desig="TESTER"

while(True):
    print("-------------------------------------------------------------------")
    print("1)Create\n2)Display\n3)Salary rise\n4)Exit\n")
    opt1=int(input("Enter your choice : "))
    print("-------------------------------------------------------------------")
    if(opt1==1):
        while(True):
            print("-------------------------------------------------------------------")
            print("1)Clerk\n2)Developer\n3)Manager\n4)Tester\n5)Exit\n")
            opt2=int(input("Enter your choice : "))
            print("-------------------------------------------------------------------")
            if(opt2==1):
                print("-------------------------------------------------------------------")
                print("Clerk..........")
                c=Clerk()
                c.display()
                c.salaryrise()
                print("-------------------------------------------------------------------")
            elif(opt2==2):
                print("-------------------------------------------------------------------")
                print("Developer..........")
                d=Developer()
                d.display()
                d.salaryrise()
                print("-------------------------------------------------------------------")
            elif(opt2==3):
                print("-------------------------------------------------------------------")
                print("Manager..........")
                m=Manager()
                m.display()
                m.salaryrise()
                print("-------------------------------------------------------------------")
            elif(opt2==4):
                print("-------------------------------------------------------------------")
                print("Tester..........")
                t=Tester()
                t.display()
                t.salaryrise()
                print("-------------------------------------------------------------------")
            else:
                break
            
    elif(opt1==2):
        f=open("prj2insert.txt","r")
        print(f.read())
        f.close()
        
    elif(opt1==3):
        f=open("prj2salary.txt","r")
        print(f.read())
        f.close()
        
    else:
        break
        
