num = int(input("Enter 1 for coading and enter 2 for decoading :"))

if(num == 1):
    coading=True
else:
    coading = False

st = input("Enter you Message :")
words = st.split()

if(coading) :   #coading

    nwords = []

    for word in words :
        if(len(word)>=3):
            r1 = "yuo"
            r2 = "thn"
            newst = r1 + word[1:] +word[0] +r2
            nwords.append(newst)

        else :
            nwords.append(word[::-1])
    
    print(" ".join(nwords))

else :      #decoading

    nwords = []

    for word in words :
        if(len(word)>=3):
            newst = word[3:-3]
            newst = newst[-1] + newst[:-1]
            nwords.append(newst)

        else :
            nwords.append(word[::-1])
    
    print(" ".join(nwords))
    

