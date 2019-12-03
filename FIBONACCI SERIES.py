r=1
while r==1:
    print("""
Welcome to another program by swapnil garg,
This program will display the first few numbers of the Fibonacci series""")
    a,b=0,1
    n=int(input("How many numbers do you wish to see?"))
    x=0
    while x<n:
        print(a)
        a,b=b,a+b
        x=x+1
    r=int(input("Do you want to do any more(1/0)"))
    
        
