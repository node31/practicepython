"""
  Question 5
  To get intersection of two lists
"""

def get_list():
  """
    To get a list of numbers entered by the user
  """
  num_list = []
  while 1:
    num = int(input("Number:"))
    if num == -1:
      break
    num_list.append(num)
  return num_list

def intersection(nl1, nl2):
  """
    Function to generate the intersection of two lists
    Arguments:
      nl1: Number List 1
      nl2: Number List 2
    Returns:
      nl3 : Intersection of two lists
  """
  nl3 = [x for x in nl1 if x in nl2]
  return nl3

def driver():
  """
    Driver Function
  """
  nl1 = get_list()
  nl2 = get_list()
  print nl1
  print nl2
  nl3 = intersection(nl1, nl2)
  print nl3

driver()
