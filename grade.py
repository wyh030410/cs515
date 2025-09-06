def calculate(x):
  if x >= 0 and x < 60:
    grade = "F"
  elif  x < 70:
    grade = "D"
  elif  x < 80:
    grade = "C"
  elif  x < 90:
    grade = "B"
  elif  x <= 100:
    grade = "A"
  elif x < 0 or x > 100:
    grade  = "N/A"
  return grade
