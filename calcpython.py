a=input('Subtraction,Addition,Multiplication,Division,Mean,Avg')
sum=0
mul=1
sub=0
div=1
if(a=='Addition'):
    c=int(input('how many numbers?'))
    while(c>0):
        b=int(input('Enter a number'))
        sum+=b
        print(sum)
        c-=1
elif(a=='Multiplication'):
    c=int(input('how many numbers?'))
    while(c>0):
        b=int(input('Enter a number'))
        mul*=b
        print(mul)
        c-=1
elif(a=='Division'):
    c=int(input('how many numbers?'))
    while True:
        b=int(input('Enter a number'))
        div=b/div
        print(div)
        while(((c-1)>0)):
            b=int(input('Enter a number'))
            div=div/b
            print(div)
            c-=1
        break
elif(a=='Subtraction'):
    c=int(input('how many numbers?'))
    while True:
        b=int(input('Enter your number'))
        # sub=b
        sub=b-sub
        print(sub)
        while ((c-1)>0):
            b=int(input('enter your number'))
            sub=sub-b
            print(sub)
            c-=1
        break
elif(a=='Mean'):
    c=int(input('how many numbers'))
    f=0
    while(c>0):
        b=int(input('Enter integer number'))
        sum=sum+b
        f+=1
        c-=1
        
    print(sum)
    print(sum/f)
    




