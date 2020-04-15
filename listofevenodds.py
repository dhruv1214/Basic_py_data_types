def ListofEvenOdds():
  l1 = []
  l2 = []  
  l1 = [x for x in range(0, 21) if (x % 2 == 0)]
  l2 = [x for x in range(0, 21) if (x % 2 != 0)]
  return[l1, l2]
  
print(ListofEvenOdds())
