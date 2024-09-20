a,b,k = map(int,input().split())
def check(a,b):
   m = a-(a//b)*b
   return m
if check(a,k) == 0 and check(b,k) == 0:
   print('Both')
elif check(a,k) == 0 and check(b,k) != 0:
   print('Memo')
elif check(a,k) != 0 and check(b,k) == 0:
   print('Momo')
else:
   print('No One')
