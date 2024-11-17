name=input("Please tell (Yes/No) if you want to shut down the program: ")

def shutdown(name):
    if name=="Yes":
        print("Okay! I will Shut Down the progrm.")
    elif name=="No":
        print("Okay! I will not shut down the program.")
    else:
        print("Sorry!")

shutdown(name)
        
