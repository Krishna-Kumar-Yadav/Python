def prime():
  for i in range(11,101):
    for j in range(2,i):
      if i%j == 0:
         return False
      return True

prime()       