while True:
  try:
    name = input('Input name : ')
    if name.isalpha() == True:
      print("""
Welcome to the science quiz!
            """)
      break
    else:
      print("""
---------------------------------------------------------------------------------------------
              Input is not valid. Please enter your name in alphabets only.
---------------------------------------------------------------------------------------------
""")
  except:
    continue

print('')

while True:
  rules = input('Rules? type "y" for yes and "n" for no : ')
  if rules == 'y':
    print("""
*********************************************************************************************
          
            This quiz requires you to input the answers of the questions given.
                        Try to answer all questions correctly.
            All questions will be about the atomic structure and the electron                                               configuration of elements.
                                      Pretty simple.
                            
                                        GOOD LUCK!

*********************************************************************************************
""")
    break
  elif rules == 'n':
    print('')
    break
  else:
    print("""
---------------------------------------------------------------------------------------------
                      Input is not valid. Please enter y or n.
---------------------------------------------------------------------------------------------
""")
    continue

print('')

while True:
  start = input('Start = y : ')
  if start == 'y':
    print('')
    break
  else:
    print("""
---------------------------------------------------------------------------------------------
                    Input is not valid. Please enter 'y' to start.
---------------------------------------------------------------------------------------------
""")
    continue

print('')

