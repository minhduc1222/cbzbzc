def outer():
    global string
    string = "Favtutor" 
    def inner():
        string= "Python Favtutor Classes" # Overwriting value of a variable string
        print("inner function:", string)
 
    inner()
    print("outer function:", string)
 
outer()