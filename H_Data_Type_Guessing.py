a,b,c = map(int,input().split())
r = (a*b)%c
n = (a*b)//c

if r == 0:
   if n>= -2147483648 and n<= 2147483648:
      print('int')
      
   else:
      print('long long')
     
else:
   print('double')