# did they put jiggle physics on Aloy
import pyperclip as pc

text = pc.paste()
newText = ''
for i in range(len(text)):
    newText += text[i]
    newText += " "
pc.copy(newText)
