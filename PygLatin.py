#define variable "pyg"
pyg = 'ay'
#define original as user input asking for a word
original = raw_input('Enter a word:')
#use if statement to determine if user input letters
if len(original) > 0 and original.isalpha():
#define variables that will add up to pyglatin translation  
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
#begin at second letter and on, then add the first letter and 'ay'
  new_word = new_word[1:len(new_word)]
  print new_word
#if invalid characters were input, print the word empty
else:
    print 'empty'
