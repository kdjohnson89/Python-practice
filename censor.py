def censor(text, word):
    words = text.split()
    result = ''
    asterisks = '*' * len(word)
    count = 0    
    
    for i in words:
        if i == word:
            words[count] = asterisks
        count += 1
    result =' '.join(words)
    
    return result
  
print censor("My password is guest", "guest")
