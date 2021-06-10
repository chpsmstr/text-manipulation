import pyperclip as pc

text = pc.paste()
text = text.lower()
text = text.split()
newText = ''

y = 0

for i in text:
    for j in i:
        if j.isalpha():
            y+=1
        if y % 2 == 0:
            newText += j.upper()
        else:
            newText += j
    newText += " "
            

pc.copy(newText)