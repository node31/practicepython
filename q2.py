"""
Question 2
"""

def oe_check():
  """
  Checks whether a number is odd or even and a corresponding
  message is displayed
  """
  num = int(input("Enter a Number:"))
  msg = ''
  if num % 4 == 0:
    msg = 'Divisible by 4'
  elif num % 2 == 0:
    msg = 'Even'
  else:
    msg = 'Odd'
  print msg

oe_check()
