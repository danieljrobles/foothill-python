phoneBook = {'mickey': '213-333-2341', 'minnie': '510-540-2390', 'goofy': '818-399-2763'}

#Keep in mind that Python does not keep these "key:value" pairs in any order. If you print the phoneBook from above, you are likely to get it in a different order. This is OK, because in many applications we just want to find the one value that we are looking for. If we care about order, we should use a list. To find and print minnie's phone number, you just write:

print ( phoneBook['minnie'] )

#If you look for a key in the dictionary that is not there, you get an error:

#print (phoneBook['donald'])

#So to be safe, you need to check if a key is in the dictionary:

if 'donald' in phoneBook:
      print (phoneBook['donald'])

#To get all the keys from the phoneBook, but no values, you can use the keys method:

print (phoneBook.keys())

#The returned value from the keys() method is in a strange format, so you might prefer to convert the returned value to a tuple or list before printing:

print ( tuple(phoneBook.keys() ))

#Adding a new character to the phoneBook is easy:

phoneBook['donald'] = '415-638-4433'

#To print the whole phoneBook, you can just print it directly:

print (phoneBook)

#Or if you would like it in a certain format, use a for/in loop:
print ("############NO SORT##################")
for character in phoneBook:
      print (character + ' has phone number ' + phoneBook[character])

#But if you would like to see it in alphabetical order:
print ("############YES SORT##################")
for character in sorted(phoneBook):
      print (character + ' has phone number ' + phoneBook[character])

