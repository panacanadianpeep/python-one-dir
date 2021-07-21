"""

1 If the user selects the ‘Enter RLE’ option
2 If the user selects the ‘Convert to ASCII art’ option
3. If the user selects the ‘Convert to RLE’ option

"""

import math

def EnterRLE():
  step2RunLengthEncoding = []
  step2Decompressed = []
  step2RLEAfterCombining = []
  step2RLE = []

  # how many lines of compresesed data to enter?
  linesRLE = int(input("How many lines of compressed data do you want to enter(note: has to be more than 2)?"))
  #validity check: Lines less than 3?



  while linesRLE < 3: 
    linesRLE = int(input("How many lines of compressed data do you want to enter(note: has to be more than 2)?"))
  
  # loops until linesRLE is same as i
  for i in range(linesRLE):
    dataToBeCompressed = input("Please enter data to be compressed")

    # splits string characters into entinity of list
    for j in dataToBeCompressed:
      step2RunLengthEncoding.append(j)
      print(step2RunLengthEncoding)
    # Trying to turn numbers as string into interger

    a = len(step2RunLengthEncoding)
    numberStep2RLE = -1
    for h in range(a):
      if (h+1) % 3 == 2:
        step2RLEAfterCombining.append(step2RunLengthEncoding[h - 1] + step2RunLengthEncoding[h])
        step2RLE.append(int(step2RLEAfterCombining[numberStep2RLE]))
        numberStep2RLE = numberStep2RLE + 2
      elif (h + 1) % 3 == 0:
        step2RLE.append(step2RunLengthEncoding[h])
        print(step2RLEAfterCombining)
        print(step2RLE)
      a = len(step2RLE)
      b = a / 2
      c = int(b)

#

def ConvertToASCIIArt():

  numbers1 = []
  numbers2 = []
  numberscomb = []
  letters = []
  lettersandnumbers = []
  almostfinallist = []
  finalstring = None
  ASCIIArt = ""
  nameoftxtfile = input("Name of the txt file, please")
  with open(nameoftxtfile, "r") as open_file:
    text = open_file.readlines()
  #removes all new lines characters
 
  for i in range(len(text)):
    if text[i][-1] == "\n":
      text[i] = text[i][0: -1]
  
  h = 0

  for i in text:
    
    for j in i:
      if ((h + 1) % 3) == 1:
        numbers1.append(j)
      if ((h + 1) % 3) == 2:
        numbers2.append(j)
      if ((h + 1) % 3) == 0:
        letters.append(j)
      h = h + 1
    for q in range(len(numbers1)):
      numberscomb.append(int(numbers1[q] + numbers2[q]))

    for i in range(len(letters)):
      ASCII1 = letters[i] * numberscomb[i]
      ASCIIArt = ASCIIArt + ASCII1
    print(ASCIIArt)

    #   for l in range(len(numberscomb)):
    #     lettersandnumbers.append(numberscomb[l])
    #     lettersandnumbers.append(letters[q])
    # for g in range(len(lettersandnumbers)):
    #   if (g + 1) % 2 == 0:
    #     almostfinallist.append(lettersandnumbers[g] * lettersandnumbers[g - 1])
    # finalstring = almostfinallist[0]
    # for g in range(len(almostfinallist) - 1):
    #   finalstring = almostfinallist[g + 1] + finalstring
    # print(finalstring)
      
    numbers1 = []
    numbers2 = []
    numberscomb = []
    letters = []
    lettersandnumbers = []
    almostfinallist = []
    finalstring = None
    ASCIIArt = ""

"""

  individual = []
  individualFullNumbers = []
  completyconverted = []
  linetoprintout = ""
  m = 0

  nameoftxtfile = input("Name of the txt file, please")
  with open(nameoftxtfile, "r") as open_file:
    text = open_file.readlines()
  for i in range(len(text)):
    if text[i][-1] == "\n":
      text[i] = text[i][0: -1]
  for i in range(len(text)):
    for j in text[i]:
      individual.append(j)
    for h in range(len(individual)):
      if (h+1) % 3 == 2:
        individualFullNumbers[m].append(individual[h] + individual[h - 1])
        individualFullNumbers.append(individual[h + 1])
        m = m + 1
    for h in range(len(individualFullNumbers)):
      if (h + 1) % 2 == 1:
        individualFullNumbers[h] == int(individualFullNumbers[h])
      if (h + 1) % 2 == 0:
        completyconverted.append(individualFullNumbers[h - 1] * individualFullNumbers[h])
    for h in range(len(completyconverted)):
      linetoprintout = linetoprintout + completyconverted[h]
    print(linetoprintout)
        
"""     

def ConvertToRLE():
  ntimecounter = 1
  nindex = 0
  h = None

  nameoftxtfile = input("Name of the txt file, please")
  with open(nameoftxtfile, "r") as open_file:
    text = open_file.readlines()
  for i in range(len(text)):
    if text[i][-1] == "\n":
      text[i] = text[i][0: -1]
  for i in range(len(text)):
    for j in text[i]:
        """
      #checking if the letter previous was equal to the letter after
      if h == j:
        #adding number of times a letters appears so that later can combine into RLE
        ntimecounter = ntimecounter + 1
      #if j is not going to in letterusedlist, add ntimecounter at right spot, and then add index by 2, and reset n time counter
      elif j not in letterusedlist:
        #if not first time, do this
        if h != None:
          letterusedlist.insert(nindex, ntimecounter)
          letterusedlist.remove(None)
          nindex = nindex + 2
          ntimecounter = 0
        #adds the number to be replaced and the letter after it
        letterusedlist.append(None)
        letterusedlist.append(j)
        """
      text[i].count(j)
            
        

    print(letterusedlist)

def DisplayASCIIArt():

  letterusedlist = []
  a = 0

  nameoftxtfile = input("Name of the txt file, please")
  with open(nameoftxtfile, "r") as open_file:
    text = open_file.readlines()
  for i in range(len(text)):
    if text[i][-1] == "\n":
      text[i] = text[i][0: -1]
  for i in range(len(text)):
    print(text[i])
        

  """
  for i in range(len(text)):
    for j in text[i]:
      if j not in letterusedlist:
        letterusedlist.append(1)
        letterusedlist.append(j)
        ntimecounter = letterusedlist.index(j)
        if letterusedlist[ntimecounter - a]:
          letterusedlist.insert(ntimecounter, letterusedlist[ntimecounter + 1])
          a = a + 1
      if i == 0:
        print(letterusedlist)
  """
  
"""
  for i in range(linesRLE):
    for j in range(step2RunLengthEncoding[i][i]):
      step2Decompressed.append(dataToBeCompressed[i, i*2])
"""
menuinput = input("Press the key according to what you want to do(based on the letters before the options) and click enter:\na.Enter RLE\nb.Display ASCII art\nc.Convert to ASCII art\nd.Convert to RLE\ne.Quit")

while True:
  if menuinput != "a" and menuinput != "b" and menuinput != "c" and menuinput != "d" and menuinput != "e":
    invalidinput = True
    while invalidinput == True:
      menuinput = input("Invalid input. Please only use the keys a,b,c,d,e only once. Enter another input that is valid.")
      print(menuinput)
      if menuinput == menuinput == "a" or menuinput == "b" or menuinput == "c" or menuinput == "d" or menuinput == "e":
        invalidinput = False

  if menuinput == "a" or menuinput == "b" or menuinput == "c" or menuinput == "d" or menuinput == "e":
    if menuinput == "a":
      EnterRLE()
    elif menuinput == "b":
      DisplayASCIIArt()
    elif menuinput == "c":
      ConvertToASCIIArt()
      menuinput == None
    elif menuinput == "d":
      ConvertToRLE()
    elif menuinput == "e":
      print("Stopping program")
      break

  menuinput = input("Press the key according to what you want to do(based on the letters before the options) and click enter:\na.Enter RLE\nb.Display ASCII art\nc.Convert to ASCII art\nd.Convert to RLE\ne.Quit")