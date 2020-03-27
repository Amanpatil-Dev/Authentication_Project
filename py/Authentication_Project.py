import os

#function to display or to make user choices
def welcome():
    print("Welcome to account login")
    print()
    print("Choose Your Choices")
    print("1.Login")
    print("2.Register")
    print("3.Delete User")
    try:
        inpt=int(input("Enter Your Choices"))
        if inpt==1:
            login()
        if inpt==2:
            register()
        if inpt==3:
            delete()
        for x in range (5,9999999):
            if inpt==x:
                print("Not A Valid Command")
                welcome()
            
                
    except (ValueError, NameError) as V:
        print("select valid input")
        welcome()
        
#function to register new user
def register():
    username=str(input("Enter the username"))
    password=str(input("Enter the password"))
    if len(password) < 8:
        print()
        print("PLEASE ENTER EIGHT(8) CHARACTER ONLY",len(password),":",password,"DETECTED")
        print()
        
    elif len(password) >= 8:
        
        g=open(username,"w+")
        g.write(username)
        g.write("\n"+password)
        g.close()
        print("you account is successfully created")
        print()

    welcome()
    
#another function to delete the existing user                                                              
def delete():
    inpu=str(input("Enter The Input For Delete The File"))
    os.remove(inpu)
    
      
#function to check whether the user is an existing user or not
def login():
    username=str(input("Enter The Username For Login"))
    password=str(input("Enter The Password For Login"))

    try:
        f=open(username,"r")
        
        for x in f:
            if username==x:
                print("")
            if password==x:
                print()
                print("UserName Found Password Also Found")
                welcome()
    except FileNotFoundError as e:
        print(e)
                    
        f.close()

#MAIN FUNCTION
            
welcome()

    






















        
        
    

