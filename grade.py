def calculate(x):
    if x < 0 or x > 100:
        return "N/A"
    elif x < 60:
        return "F"
    elif x < 70:
        return "D"
    elif x < 80:
        return "C"
    elif x < 90:
        return "B"
    else:  
        return "A"
