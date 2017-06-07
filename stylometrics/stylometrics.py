### Anwesh Joshi
### HW 5 - sylometrics.py

def byFreq(pair):
    """byFreq is used so that i can check the second element in a list
       wich will be used when sorting elements in descending order
       on basis of their ratio i.e. second element of list"""

    return pair[1]

def main():
    """This is the function where I ran three of Melville files
     and returned the list of 50 most frequent words in a list and
     did the same for Shakespeare"""

    wordsM=[]
    wordsS=[]

    for text in ["moby.txt", "omoo.txt", "bartleby.txt"]:
        text=open(text,'r').read()
        text=text.lower()
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            text=text.replace(ch,' ')
        wordsM+=text.split()

    for text in ["macbeth.txt", "othello.txt","allswell.txt"]:
        text=open(text,'r').read()
        text=text.lower()
        for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
            text=text.replace(ch,' ')
        wordsS+=text.split()
        
    countsM={}
    countsS={}

    for w in wordsM:
        countsM[w]=countsM.get(w,0)+1
    for w in wordsS:
        countsS[w]=countsS.get(w,0)+1

    FinalM=[]
    FinalS=[]

    itemsM=list(countsM.items())
    itemsM.sort
    itemsM.sort(key=byFreq, reverse=True)
    itemsS=list(countsS.items())
    itemsS.sort
    itemsS.sort(key=byFreq, reverse=True)

    for i in range(50):
        word,count=itemsM[i]
        ratioM=(count+0.0)/len(wordsM)
        A=[word]+[ratioM]
        FinalM+=[A]

    for j in range(50):
        word,count=itemsS[j]
        ratioS=(count+0.0)/len(wordsS)
        B=[word]+[ratioS]
        FinalS+=[B]
    
    return [FinalM]+[FinalS]

if __name__ == '__main__':  main()

def wordScore(word,scoreList):
    "'word is the string whose paired up numeric value is to be \
obtained from the scorelist'"
    if scoreList==[]:
        return 0
    elif word in [x[0] for x in scoreList]: 
        wordvalue=filter(lambda d: d[0]==word,scoreList)
        return wordvalue[0][1]
    else:
        return 0
    


def identifyAuthor(filename):
    """identifyAuthor is the function where I will input any filename
    and will obtain back the name of author as Shakespeare, Melville
     or unknown """
    text=open(filename,'r').read()
    text=text.lower()

    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~':
        text=text.replace(ch, ' ')
    words=text.split()
    
    counts={}
    for w in words:
        counts[w]=counts.get(w,0)+1

    Ukn=[]

    items=list(counts.items())
    items.sort
    items.sort(key=byFreq,reverse=True)
    for i in range(50):
        word,count=items[i]
        ratio=(count+0.0)/len(words)
        U=[word]+[ratio]
        Ukn+=[U]
    
    A=main()
    Mel=A[0]
    Shakes=A[1]
    
    sodS=0
    sodM=0

    for a in range(50):
        k= wordScore(Ukn[a][0],Shakes)
        difS=abs(Ukn[a][1]-k)
        sodS+=difS
        
        l= wordScore(Ukn[a][0],Mel)
        difM=abs(Ukn[a][1]-l)
        sodM+=difM

    
    if sodS<0.128:
       return "Shakespeare"
    if sodM<0.161:
        return "Melville"
    if sodS>0.128 and sodM>0.161:
        return "Unknown"
       
        

    

    
    
        
    
    
