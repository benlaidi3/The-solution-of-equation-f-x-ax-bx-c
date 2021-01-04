def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
     	return float(n).is_integer()
while (1==1) :
    print ("that's program creat by OMIROS05 ")
    print ("that's program give on you a solution of equation  f(x)= ax² +bx + c ")
    a=input("enter number a : ")
    b=input("enter number b : ")
    c=input("enter number c : ")
    if  is_integer(a ) ==	False  or  is_integer(b)  == False or is_integer(c) == False:
    	print ('please chose number not string ')
    else :
	    if a==b==0 :
	        print ("error ")
	    elif a==0 : 
	        X=float(-c/b)
	        print ("the solution is " +str(X))
	    else :
	        a=float(a.lstrip())
	        b=float(b.lstrip())
	        c=float(c.lstrip())
	        d=float((b**2)-4*a*c)
	        if d<0 :
	            print ("the delta is  " + str(d))
	            print ("this equation haven't solution ")
	        if d==0 :
	            x=float(-b/(2*a))
	            print ("the delta is " + str(d ))
	            print ("the solution is " +str(x))
	        if d>0 :
	            print(d)
	            x1=(-b+(d**(1/2)))/(2*a)
	            x2=(-b-(d**(1/2)))/(2*a)
	            print ("the delta is " +str(d ))
	            print ("the  first solution is : " + str(x1) )
	            print ("and the second solution is :" +str(x2))
	        
	   
    print  ("---------------reopening---------------") 
