#write a python program to translate a message into secret code language.Use the rules below to translate 
# normal english into secret code language
#coding:
#if the world contain atleast 3 character, remove the first letter and append it at the end
#now append three random characters at the starting and the end
#else:
#simply reverse the string
#decoding:
#if the world contain less than 3 character, reverse it
#else:
#remove 3 random character from start and end. Now remove the last letter and the beginning
#Your program should ask wheteher you want to code or decode

text=input("Enter a message")
words = text.split(" ")
coding = input("1 for coding or 0 for Decoding")
coding = True if (coding=="1") else False
print(coding)
if(coding):
    nwords = []
    for word in words:
        if(len(word)>=3):
         r1="dsf"
         r2="jkr"
         textnew = r1 + word[1:] + word[0] +r2
         nwords.append(textnew)
        else:
            nwords.append(word[::-1]) # aapn string la reverse as pn karu shakto
            print("".join(nwords))
else:
    nwords = []
    for word in words:
        if(len(word)>=3):
         textnew = word[3:-3]
         textnew = textnew[-1] + textnew[::-1]#this use to reverse keyword
         nwords.append(textnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
