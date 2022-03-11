x = 0
score = x

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
          Questions will be put in sections split into different                                     topics of science
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

print("""************************************************************************
                            Chemistry Section
                      (Atomic Structures and ions)
************************************************************************
      
      """)

question_1 = input("What is the center of an atom called?\n\n        a)Nucleus \n        b)Protons \n        c)Electrons \n        d)Neutrons \n\nAnswer : ")
if question_1.lower() == 'a' or question_1.lower() == 'nucleus':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nThey are called the Nucleus\n\n')
  
question_2 = input("Where are the electrons located in the atoms?\n\n        a)outside \n        b)inside \n\nAnswer : ")
if question_2.lower() == 'a' or question_2.lower() == 'outside':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nElectrons are located outside the atoms\n\n')

question_3 = input("What is the charge on an electron?\n\n        a)Positive \n        b)Neutral \n        c)Negative \n        d)Other \n\nAnswer : ")
if question_3.lower() == 'c' or question_3.lower() == 'negative':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nElectrons have a negative charge\n\n') 

question_4 = input("Which of the three sub-atomic particles is the lightest?\n\n        a)Protons \n        b)Electrons \n        c)Neutrons \n        d)They are all the same \n\nAnswer : ")
if question_4.lower() == 'b' or question_4.lower() == 'electrons' or question_4.lower() == 'electron':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nElectrons is the lightest among these sub-atomic particles\n\n') 

question_5 = input("Electron configuration of a 'Lithium Atom'?\n\n        a)2,8 \n        b)2,3 \n        c)2,7 \n        d)2,1 \n\nAnswer : ")
if question_5.lower() == 'd' or question_5 == '2,1' or question_5 == '2 1':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nThere are 3 electrons in a lithium atom\n\n')

question_6 = input("What is the eletron configuration of a 'Neon Atom'?\n\n        a)2,9 \n        b)2,8,8 \n        c)2,8 \n        d)2,8,8,2 \n\nAnswer : ")
if question_6.lower() == 'c' or question_6 == '2,8' or question_6 == '2 8':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nThere are 10 electrons in a neon atom\n\n')

question_7 = input("What is the electron configuration of an 'Argon Atom'?\n\n        a)2,6 \n        b)2,8,8 \n        c)2,8,8,1 \n        d)2,8,7 \n\nAnswer : ")
if question_7.lower() == 'b' or question_7 == '2,8,8' or question_7 == '2 8 8':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nThere are 18 electrons in an argon atom\n\n')

question_8 = input("The amount of protons and electrons are equal in an atom?\n\n        a)True \n        b)False \n\nAnswer : ")
if question_8.lower() == 'a' or question_8.lower() == 'true':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nThere are the same amount of protons as there is electrons\n\n')

question_9 = input("What do you call an atom that loses or gains one or more electrons?\n\n        a)Isotopes \n        b)Elements \n        c)Compounds \n        d)Ions \n\nAnswer : ")
if question_9.lower() == 'd' or question_9.lower() == 'ions' or question_9.lower() == 'ion':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nThey are called ions\n\n')

question_10 = input("What do you call an atom with the same atomic number but different mass numbers?\n\n        a)Element \n        b)Products \n        c)Isotopes \n        d)Compound Elements \n\nAnswer : ")
if question_10.lower() == 'c' or question_10.lower() == 'isotopes' or question_10.lower() == 'isotope':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nThey are called isotopes\n\n')

question_11 = input("Which of the following sub-atomic particles have a positive charge?\n\n        a)Protons \n        b)Electrons \n        c)Neutrons \n\nAnswer : ")
if question_11.lower() == 'a' or question_11.lower() == 'protons' or question_11.lower() == 'proton':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nProtons have a positive charge\n\n')

question_12 = input("Negatively charged ions are not called 'Anions'?\n\n        a)True \n        b)False \n\nAnswer : ")
if question_12.lower() == 'b' or question_12.lower() == 'false':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nThey ARE called anions\n\n')


print("""************************************************************************
                            Physics Section
************************************************************************""")

question_13 = input("What is the rate that the distance is traveled in a particular direction called?\n\n        a)Distance \n        b)Mass \n        c)Velocity \n        d)Acceleration \n\nAnswer : ")
if question_13.lower() == 'c' or question_13.lower() == 'velocity':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nThe rate is velocity\n\n')

question_14 = input("What is the rate at which speed changes called?\n\n        a)Mass \n        b)Distance \n        c)Friction \n        d)Acceleretion")
if question_14.lower() == 'd' or question_14.lower() == 'acceleration':
  print("""                              *-*-*-*-*-*
                                Correct!
                              *-*-*-*-*-*
""")
  x = x + 1
else:
  print('\nIncorrect!\n\nThe rate is acceleration\n\n')
  

#Total Score
score = int(x / 11 * 100)
print(name,"you scored :",score,"%")