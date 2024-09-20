n,m,k = map(int,input().split())
if n<1 or k<1:
   print(0)
# Two eyes and one body.
# Two eyes, one mouth, and one body.
# One eye, one mouth, and one body.
else:
   def third(n,m,k):
      mi = min(n,m,k)
      n = n-mi
      m = m-mi
      k = k-mi
      return mi,n,m,k

   total,n,m,k = third(n,m,k)
   if k<1 :
      print(total)
   else:
      if n>=2*k:
         total += k
         print(total)
      elif n//2 < k:
         print(n//2+total)
      
   