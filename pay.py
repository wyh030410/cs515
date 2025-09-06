import math
def unfair_weekly_paycheck_amount(x):
  work_hour = math.floor(x)
  payment = work_hour * 15
  return payment


def fair_weekly_paycheck_amount(x):
  work_hour = math.ceil(x)
  payment = work_hour * 15
  return payment

