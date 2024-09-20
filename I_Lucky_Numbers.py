i = input()
f = int(i[0])
l = int(i[1])
if l!=0 and f%l == 0:
   print('YES')
elif f!=0 and l%f == 0:
   print('YES')
elif f == l:
   print('YES')
else:
   print('NO')