#We have a function that outputs "welcome,user" as it is called.we want to make it more personalized ,so 
#redesign the given function so that it will take the name of the user as input and output the welcome message
#with it.
name=str(input())
def welcome(name):
    print("Welcome, " + name)
welcome(name) 
#In Python ,the 'f' before a string literal denotes an f-string ,which stands for "formatted string literal"
#it allows you to embed expressions inside string literals ,using curly braces .
#the expressions inside the curly braces are evaluated at runtimeband formatted using the ---format --protocol 


