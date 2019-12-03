import random
sc=0
ch=1
print("""
WELCOME TO THE FIRST EVER GAME BY SWAPNIL GARG,
THIS IS THE ADDITION QUIZ,
YOU CAN PLAY A GAME OF YOUR PREFERRED LENGTH
AND VIEW YOUR FINAL SCORE AT THE END""")
while ch==1:
    n=int(input("How long of a game you wish to play?"))
    r=0
    while r<n:     
        x=random.randint(1,100)
        y=random.randint(1,100)
        z=x+y
        print(x,"+",y,"=?")
        ans=int(input())
        if ans==z:
            print("The answer is correct!")
            sc=sc+1
            print("Current score is",sc)
        else:
            print("Sorry,The answer is wrong!")
            print("The correct answer is",z)
            sc=sc-1
            print("Current score is",sc)
        r=r+1
    print("Your final score is",sc,"out of",n)
    ch=int(input("Wanna play again,then press 1"))
    
    
    

