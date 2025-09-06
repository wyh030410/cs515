def calculate(x):
  if x >= 0 and x < 60:
    grade = "F"
  elif x >= 60 and x < 70:
    grade = "D"
  elif x >= 70 and x < 80:
    grade = "C"
  elif x >= 80 and x < 90:
    grade = "D"
  elif x >= 90 and x < 100:
    grade = "A"
  elif x < 0 or x > 100:
    grade  = "N/A"
  return (grade)
