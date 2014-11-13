""" takes a whole number as parameter and returns a string containing the number spelled out in English
"""
#IMPORTS
import string

#This function gets the number of digits in a number
def getNumberOfDigits(num):
    return len(str(abs(num)))

#This function converts a number into list of lists that contain the digit and the position of that digit
def makeDigitAndPositionList(num):
    tempList = []
    counter = 0
    for x in str(abs(num)):
        position = abs(counter - getNumberOfDigits(num))
        counter = counter + 1
        tempList.append([int(x), int(position)])
    return tempList  

#This function associates a numerical position with the english counterpart
def getEnglishPosition(p):
      if p == 1:    return ""
      elif p == 2:  return "ty "      
      elif p == 3:  return " Hundred "
      elif p == 4:  return " Thousand "
      elif p == 5:  return "ty "
      elif p == 6:  return " Hundred "
      elif p == 7:  return " Million "
      elif p == 8:  return "ty "
      elif p == 9:  return " Hundred "

#This function associates the number with the english counterpart
def getEnglishDigitName(d):
      if d == 0:  return "Zero"
      elif d == 1:  return "One"
      elif d == 2:  return "Two"      
      elif d == 3:  return "Three"
      elif d == 4:  return "Four"
      elif d == 5:  return "Five"
      elif d == 6:  return "Six"
      elif d == 7:  return "Seven"
      elif d == 8:  return "Eight"
      elif d == 9:  return "Nine"

#This function fixes the teens placement
def replaceEnglishTeenWords (s):
    s = s.replace("Onety Zero","Ten")
    s = s.replace("Onety One","Eleven")
    s = s.replace("Onety Two","Twelve")
    s = s.replace("Onety Three","Thirteen")
    s = s.replace("Onety Four","Fourteen")
    s = s.replace("Onety Five","Fifteen")
    s = s.replace("Onety Six","Sixteen")
    s = s.replace("Onety Seven","Seventeen")
    s = s.replace("Onety Eight","Eighteen")
    s = s.replace("Onety Nine","Nineteen")
    return s

#Delete garbage English Words
def deleteGarbageEnglishWords(s):
    listOfWords = ["Zeroty"," Zero","Zero Hundred ","Million Hundred ","Thousand Hundred "]
    for x in listOfWords:
        s = s.replace(x,"")
    return s
    
#This function removes the nonfunctional silly English translations
def fixSillyEnglish(s):
    s = replaceEnglishTeenWords(s)
    
    s = s.replace("Twoty","Twenty")
    s = s.replace("Threety","Thirty")
    s = s.replace("Fourty","Forty")
    s = s.replace("Fivety","Fifty")
    s = s.replace("Eightty","Eighty")
    s = deleteGarbageEnglishWords(s)
    s = s.replace("  "," ")
    return s
    
#This function returns the english word for a digit and its numerical position
def spell(n,p):
    return "%s%s" % (getEnglishDigitName(n),getEnglishPosition(p))


NUM_int = -2246800
isNUMPositive = ""
if NUM_int < 0:
    isNUMPositive = "Negative " 
NUM_list = makeDigitAndPositionList(NUM_int)
NUM_english = ""
for x in NUM_list:
    NUM_english = NUM_english + spell(x[0],x[1])
NUM_english = fixSillyEnglish(NUM_english)
print(str(NUM_int)+": "+isNUMPositive+NUM_english)
"""

text_file = open("workfile.txt", "w")
text_file.write("")
text_file.close()

This Section is for QA, and I want to keep it so that I can reference at a later date
for n in range(290187,999999999,10003):#999999999,100000):
    isNUMPositive = ""
    if n < 0:
        isNUMPositive = "Negative " 
    NUM_list = makeDigitAndPositionList(n)
    NUM_english = ""
    for x in NUM_list:
        NUM_english = NUM_english + spell(x[0],x[1])
    NUM_english = fixSillyEnglish(NUM_english)
    text_file = open("workfile.txt", "a")
    text_file.write(str(n)+": "+isNUMPositive+NUM_english+"\n")
    text_file.close()
    #print(isNUMPositive+NUM_english)
"""
