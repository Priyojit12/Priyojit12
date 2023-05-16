
words = input("ENTER YOUR MESSAGE:")
i = list(words)
if (len(i)<=2 ):
    i.reverse()
    print(str(i))
elif(len(i)>2):
    i.append(i[0])
    i.remove(i[0])
    i.insert(0,1)
    i.insert(1,2)
    i.insert(2,3)
    print(i)

decode = list(input("DECODE YOUR WORDS:"))
if (len(decode)<=2 ):
    decode.reverse()
    print(str(decode))
elif(len(decode)>2):
    decode.remove(decode[0])
    decode.remove(decode[0])
    decode.remove(decode[0])
    decode.insert(0,decode[-1])
    decode.pop()
    print(decode)
    
