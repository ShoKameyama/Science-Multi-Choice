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
      All questions will be about the atomic structure and the electron                       configuration of the elements.
    You can either input the letters of the answers or the word / number.
                              Pretty simple.
                                
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
  start = input("Press 'Enter' to start ")
  if start == '':
    print('')
    break
  else:
    print("""
------------------------------------------------------------------------
            Input is not valid. Please press 'Enter' to start.
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
else:
  print('\nIncorrect!\nThey are called the Nucleus\n')
  
question_2 = input("Where are the electrons located in the atoms?\n\n        a)outside \n        b)inside \n\nAnswer : ")
if question_2.lower() == 'a' or question_2.lower() == 'outside':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
else:
  print('\nIncorrect!\nElectrons are located outside the atoms\n')

question_3 = input("What is the charge on an electron?\n\n        a)Positive \n        b)Neutral \n        c)Negative \n        d)Other \n\nAnswer : ")
if question_3.lower() == 'c' or question_3.lower() == 'negative':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
else:
  print('\nIncorrect!\nElectrons have a negative charge\n') 

question_4 = input("Which of the three sub-atomic particles is the lightest?\n\n        a)Protons \n        b)Electrons \n        c)Neutrons \n        d)They are all the same \n\nAnswer : ")
if question_4.lower() == 'b' or question_4.lower() == 'electrons' or question_4.lower() == 'electron':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
else:
  print('\nIncorrect!\nElectrons is the lightest among these sub-atomic particles\n') 

question_5 = input("Electron configuration of a 'Lithium Atom'?\n\n        a)2,8 \n        b)2,3 \n        c)2,7 \n        d)2,1 \n\nAnswer : ")
if question_5.lower() == 'd' or question_5 == '2,1' or question_5 == '2 1':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
else:
  print('\nIncorrect!\nThere are 3 electrons in a lithium atom')

question_6 = input("What is the eletron configuration of a 'Neon Atom'?\n\n        a)2,9 \n        b)2,8,8 \n        c)2,8 \n        d)2,8,8,2 \n\nAnswer : ")
if question_6.lower() == 'c' or question_6 == '2,8' or question_6 == '2 8':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
else:
  print('\nIncorrect!\nThere are 10 electrons in a neon atom')

question_7 = input("What is the electron configuration of an 'Argon Atom'?\n\n        a)2,6 \n        b)2,8,8 \n        c)2,8,8,1 \n        d)2,8,7 \n\nAnswer : ")
if question_7.lower() == 'b' or question_7 == '2,8,8' or question_7 == '2 8 8':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
else:
  print('\nIncorrect!\nThere are 18 electrons in an argon atom')

