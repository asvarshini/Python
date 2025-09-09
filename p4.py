# p1 od dictinory
'''num = input("numbers :")
di_num = {
    "1": "one",
    "2":"two",
    "3":"three"
}
output =""
for ch in num:

    output += di_num.get(ch,"!")+" "
print(output)'''
#return in emojis
message =input(">")
word =message.split(' ')
emo ={
    ":)" :"😊",
    ":(" :'😒'
}
print(word)
output =""
for itam in word:
    output += emo.get(word,word) + " "
print(output) 
