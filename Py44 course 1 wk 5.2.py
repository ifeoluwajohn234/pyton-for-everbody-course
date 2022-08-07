score = input("Enter Score: ")
try:
  if float(score) > 1.0:
        print("out of range")
  elif float(score) >= 0.9:
      print("A")
  elif float(score) >= 0.8:
      print("B")
  elif float(score) >= 0.7:
      print("C")
  elif float(score) >= 0.6:
      print("D")
  else:
      print("F")
except:
    print("Enter only numbers between zero and one")
    exit()
          