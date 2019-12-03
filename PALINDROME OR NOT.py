r=1
print("""
Welcome to a program by Swapnil garg,
This program is designed to check whether a given string is a palindrome or not.
This was made under the guidance of Garg Software Co. Pvt. Ltd.""")
while r==1:
    s=str(input("Enter your string"))
    l=int(len(s))
    x=0
    
    a=[]

    while x<l:
        a.append(s[x])
        x=x+1   
    def check(a):
        y=0
        while y<l/2:
            if a[y]==a[l-1-y]:
                check=1
            else:
                check=0
                print(s,"is not a palindrome")
                y=l/2
            y=y+1
        
        if check==1:
            print(s, "is a palindrome")
    check(a)

    
