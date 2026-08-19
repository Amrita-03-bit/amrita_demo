try:
 with open("marks.txt") as f:
    lines=f.readlines()
 l=[ int(i)**2 for i in lines if int(i)>10 ]
 print(l)
except FileNotFoundError:
  print("not found")