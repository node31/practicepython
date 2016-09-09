"""
  Question 4
  To print all the factors of a number
"""

def get_factors(dividend):
  """
  Returns a list of all the factors of a number
  Arguments:
    dividend: A number whose factors a required
  Returns:
    factor_list: A list of factors of the dividend
  """
  factor_list = [x for x in range(1, dividend/2 + 1) if dividend % x == 0]
  factor_list.append(dividend)
  return factor_list

print get_factors(int(input("Enter Number:")))
