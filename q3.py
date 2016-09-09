"""
Checking if less than a particular number
"""

def get_list():
  """
  Returns:
    num_list: A list of numbers
  """
  num_list = []
  num_list.append(0)
  while 1:
    num = int(input("Number:"))
    if num == -1:
      break
    num_list.append(num)
  return num_list

def get_short_number():
  """
  Returns:
    short_number: A number with whom the list needs to be
    chcecked against
  """
  return int(input("Check Number:"))

def check_list(my_list, short_number):
  """
  Making a list of numbers which are lesser than short_number
  in my_list
  """
  short_list = [x for x in my_list if x > short_number]
  return short_list

def driver():
  """
  Driver Method
  """
  my_list = get_list()
  print my_list
  short_number = get_short_number()
  print short_number
  short_list = check_list(my_list, short_number)
  print short_list

driver()
