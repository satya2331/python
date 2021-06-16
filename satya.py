##a=100
##b=20
##if a<b:
##    print(a+b)
##else:
##    print(a-b)
##
##print('done')












##m=int(input())
##
##if m>=0 and m<=100:
##   if m>=60 and m<80:
##       print('B grade')
##   elif m>=80:
##      print('A grade')
##   elif m>=40 and m<60:
##      print('C grade')
##   else:
##      print('Failed')
##
##else:
##print('Invalid marks')


##for i in range(1,10):
##               print(i,end=' ')




##for i in range(1,11,1):
##   print(i,end=' ')
##   i+=2
##   print(i)







##for i in range(-10,10,1):
##   print(i,end=' ')





##i=-10
##while i<=1:
##   print(i,end=' ')
##   i+=2



##i=1
##while i<10:
##   print(i,end=' ')




##for i in range(1,11):
##    if i==5:
##        break
##    print(i,end=' ')
##
##print('done')




##for i in range(1,11):
##    if i==5:
##        continue
##    print(i,end=' ')
##
##print('done')



##i=1
##while i<=10:
##    if i==6:
##        break
##    print(i,end=" ')
##    i+=1
##
##print('done')



##i=0
##while i<10:
##    i+=1
##    if i==5:
##        continue
##    print(i,end=" ")
##print('done')


##for i in range(1,11,1):
##    print(i,end=' ')
##    i+=2
##
##    print(i)


##n=int(input('enter a number: '))
##s=int(input('enter a start point: '))
##e=int(input('enter end point: '))
##
##for i in range(s,e+1):
##    print(n,'*',i,'=',n*i)
##
##while s<=e:
##    print(n,'*',s,'=',n*s)
##    s+=1



##n=int(input('enter a number: '))
##import math
##s=int(math.sqrt(n))
##c=0
##for i in range(1,s+1):
##    if n%i==0:1
##        c+=1
##
##if c>1:
##    print(n,'is not a prime')
##else:
##    print(n,'is a prime number')



##n=input('enter a number: ')
##if n==n[::-1]:
##    print(n,'is a palindrome')
##else:
##    print(n,'is not a palindrome')



##n=int(input('enter series range: '))
##a=0
##b=1
##print(a,end=' ')
##for i in range(2,n+1):
##    print(b,end=' ')
##    c=2*a+b
##    a=b
##    b=c


##for i in range (1,6):
##    print(i*i)



##a=int(input())
##b=int(input())
##c=b
##while True:
##    if c%a==0 and c%b==0:
##        print('LCM of',a,b,'is',c)
##        break
##    c+=1



##a=int(input())
##b=int(input())
##if a>b:
##    a,b=b,a
##print(a,b)
##for i in range(a,0,-1):
##    if a%i==0 and b%i==0:
##        print('gcd of',a,b,'is',i)
##        break


##def example():
##    print(10+20)
##
##example()
##
##example()

##def example(a,b):#formal parameters
##    print(a+b)
##
##x=int(input('enter a number: '))
##y=int(input('enter a number: '))
##example(x,y) #actual parameters
##
##n=int(input('enter a number: '))
##m=int(input('enter a number: '))
##example(n,m) #actual parameters



##def example():
##    a=12#local variable
##    print('inside function',a)
##
##a=10#global variable
##
##print('before function',a)
##
##example()
##
##print('after function',a)


##def example():
##    b=12
##    print('inside function',b)
##
##example()
##
##print('after function',b)

##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            #print(n,'is not a prime')
##            break 
##        else:
##           print(n,'is a prime')
##
##s=int(input('enter a number: '))
##e=int(input('enter a number: '))
##for i in range(s,e+1):
##    prime(i)


##def add(a,b):
##    print(a+b)
##
##add(5,4)
##
##def addl(a,b):
##    return(a+b)
##print(addl(5,4))
  
##def prime(n):
##    for i in range(2,n):
##        if n%i==0:
##            return False
##        else:
##            return True


##a=int(input('enter a number: '))
##if prime(a):
##    print(a,'is prime')
##while True:
##    a+=1
##    if prime(a):
##        print(a,'is a prime')
        

def fun(a):
    l=0
    for i in a:
        l+=1
    return(l)








#EMOJI'S CODE
##print("\U0001F600")
##print("\U0001F618")
##print("\U0001F917")
##print("\U0001F62A")
##print("\U0001F637")
##print("\U0001F612")
##print("\U0001F62B")









    




