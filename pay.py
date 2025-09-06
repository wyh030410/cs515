import math
def unfair_weekly_paycheck_amount(x):
  work_hour = math.floor(x)
  payment = work_hour * 15
  return payment


def fair_weekly_paycheck_amount(x):
  payment = x * 15
  return payment
print(fair_weekly_paycheck_amount(3.75))

