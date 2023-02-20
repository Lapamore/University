def Prima(A):
  B = A.copy()
  C = []
  C1 = []
  c = 0
  l = []
  for i in B:
    l += list(i[0] + i[1])
  l1=list(set(l))
  m = 2
  p = 1
  B.sort(key = lambda tup: tup[2])
  print(B)
  C += B[0][0]
  C += B[0][1]
  c += B[0][2]
  print(B[0][0], B[0][1], B[0][2])
  del B[0]
  while p!=0:
    for j in range(len(B)):
      if m>=len(l1) and not C1:
        p=0
        break
      if not(B[j][0] in C and B[j][1] in C) and not(B[j][0] in C1 and B[j][1] in C1) and((B[j][0] in C and B[j][1] in C1) or (B[j][1] in C and B[j][0] in C1)):
        print(B[j][0], B[j][1], B[j][2])
        C+=C1
        c+=B[j][2]
        C1=[]
        break
      elif (B[j][0] in C and not B[j][1] in C) or(B[j][1] in C and not B[j][0] in C):
        print(B[j][0], B[j][1], B[j][2])
        C+=B[j][1]
        C+=B[j][0]
        c+=B[j][2]
        m+=1
        break
      elif not(B[j][0] in C or B[j][1] in C):
        if (B[j][0] in C1 and not B[j][1] in C1) or(B[j][1] in C1 and not B[j][0] in C1):
          print(B[j][0], B[j][1], B[j][2])
          C1+=B[j][1]
          C1+=B[j][0]
          c+=B[j][2]
          m+=1
          break
        elif not C1:
          print(B[j][0], B[j][1], B[j][2])
          C1+=B[j][1]
          C1+=B[j][0]
          c+=B[j][2]
          m+=2
          break
  return c
 
 
A = [("A", "B", 1), ("B", "C", 1), ("C", "D", 1), ("A", "D", 1)]
D = [("A", "B", 2), ("B", "C", 2), ("A", "C", 2), ("B", "E", 2), ("A", "E", 7), ("C", "E", 5), ("B", "D", 9), ("D", "E", 10), ("D", "G", 2), ("E", "G", 9), ("G", "H", 17), ("D", "H", 16), ("D", "F", 5), ("F", "H", 17)]
E = [("A", "B", 4), ("A", "E", 6), ("A", "D", 3), ("A", "F", 1), ("B", "C", 2), ("B", "G", 1), ("B", "E", 7), ("B", "D", 3), ("B", "F", 6), ("C", "G", 2), ("C", "E", 4), ("D", "E", 1), ("D", "F", 5), ("D", "G", 3), ("E", "F", 3), ("E", "G", 6), ("F", "G", 7)]

print(Prima(E))
