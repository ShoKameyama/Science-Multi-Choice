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
------------------------------------------------------------------------
      Input is not valid. Please enter your name in alphabets only.
------------------------------------------------------------------------
""")
  except:
    continue

print('')

while True:
  rules = input('Rules? type "y" for yes and "n" for no : ')
  if rules == 'y':
    print("""
************************************************************************
          
    This quiz requires you to input the answers of the questions given.
                  Try to answer all questions correctly.
          All questions will be about the atomic structure and
                the electron configuration of the elements.
                              Pretty simple.
                            Press "y" to start.
                                
                                GOOD LUCK!

************************************************************************
""")
    break
  elif rules == 'n':
    print('')
    break
  else:
    print("""
------------------------------------------------------------------------
                Input is not valid. Please enter y or n.
------------------------------------------------------------------------
""")
    continue

print('')

while True:
  start = input('Start : ')
  if start == 'y':
    print('')
    break
  else:
    print("""
------------------------------------------------------------------------
            Input is not valid. Please enter 'y' to start.
------------------------------------------------------------------------
""")
    continue

print('')


question_1 = input("What is the center of an atom called?\n\n        a)Nucleus \n        b)Protons \n        c)Electrons \n        d)Neutrons \n\nAnswer : ")
if question_1.lower() == 'a' or question_1.lower() == 'nucleus':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
elif question_1.lower() == 'b' or 'c' or 'd' or 'protons' or 'electrons' or 'neutrons' or 'proton' or 'electron' or 'neutron':
  print('\nIncorrect!\n')
else:
  print("""
------------------------------------------------------------------------
            Input is not valid. Please enter a valid answer.
------------------------------------------------------------------------
""")

question_2 = input("Where are the electrons located in the atom?\n\n        a)outside \n        b)inside \n\nAnswer : ")
if question_2.lower() == 'a' or question_2.lower() == 'outside':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
else:
  print('\nIncorrect!\n')

question_3 = input("What is the charge on an electron?\n\n        a)Positive \n        b)Neutral \n        c)Negative \n        d)Other \n\nAnswer : ")
if question_3.lower() == 'c' or question_3.lower() == 'negative':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
else:
  print('\nIncorrect!\n') 

question_4 = input("Which of the three sub-atomic particles is the lightest?\n\n        a)Protons \n        b)Electrons \n        c)Neutrons \n        d)They are the same! \n\nAnswer : ")
if question_4.lower() == 'b' or question_4.lower() == 'electrons' or question_4.lower() == 'electron':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
else:
  print('\nIncorrect!\n') 