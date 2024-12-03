f = open('m9-1,txt')
s = f.read()
s = s.split('ДД')
s = [word for word in s if len(word) == 34]
s = [word for word in s if word[i] == 'f']
print(len(s))
