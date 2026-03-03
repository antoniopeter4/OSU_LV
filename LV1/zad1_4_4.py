import string

file=open("song.txt",encoding="utf-8")

text=file.read()
text=text.lower()
for sign in string.punctuation:
    text=text.replace(sign,"")


words=text.split()

textD={}
for word in words:
    if word in textD:
        textD[word]+=1
    else:
        textD[word]=1

once=[]
count=0
for key,value in textD.items():
    if value==1:
        once.append(key)
        count+=1
print ("Number of words:",count)
print(once)
