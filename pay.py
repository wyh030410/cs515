import math
def unfair_weekly_paycheck_amount():
  work_hour1 = float(input("work hours: "))
  work_hour2 = int(work_hour1)
  payment = work_hour2 * 15
  return payment


def fair_weekly_paycheck_amount():
  work_hour1 = float(input("work hours: "))
  work_hour2 = math.ceil(work_hour1)
  payment = work_hour2 * 15
  return payment

