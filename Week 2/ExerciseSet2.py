#2 - remove(list, number)
def remove(List, number):
    returnList=[]
    for i in List:
         if i >= number:
             returnList.append(i)
    List=returnList         
    return List

# 3 - copyElementsUnder(List, number)
def copyElementsUnder(List, number):
    newlist=[]
    for i in List:
        if i >= number:
            newlist.append(i)
    return newlist
    
# 4 - removeByList(list, collection)
#why does this work if you iterate through every i in collection but not if you do it the other way around??
def removeByList (List, collection):
    for i in collection:
            if i in List:
                List.remove(i)
    return List

#5 - removeDuplicates(list)
def removeDuplicates(List):
    noDupList = []
    for i in List:
        if i not in noDupList:
            noDupList.append(i)
    return noDupList

#6 - listOverlap(collection, collection)
def listOverlap(collection1, collection2):
    overlapList=[]
    for i in collection1:
        if i in collection2:
            overlapList.append(i)
    return overlapList

def listOverlap2(collection1, collection2):
    overlapList2=[i for i in collection1 if i in collection2]
    return overlapList2


#7 createList(start, stop, step)
def createList(start, stop, step=1):
    newList=[]
    newList = [i for i in range(start, stop, step)]
    return newList

#8 clubEntry(name, guestlist)*

# guestlist={"Jamie":True,"Tomas":False}
def clubEntry(name, guestlist):   
    if name in guestlist:
                if guestlist[name]== True:
                    return True
                else: return False
    else: return False

#9 factorial(number)
def factorial(number):
    if number == 1:
        return 1
    else:
        return n * factorial(number-1)

#Could this be done with a while loop?
    

#10 fibSequence(number)
def fibSequence(number):
    seq = [1,1]
    while number > len(seq):
        next = seq[-1]+seq[-2]
        seq.append(next)
    return seq

# 11 hanoi(number)
# pattern is 2^n -1 (I don't think my solution uses recursion??)
def hanoi(number):
    if number < 1:
        return False
    else:
        return (2** number)- 1


'''12 infiniteRecursion(number)

Every time  you make  a recursive  call, the  computer  needs to remember that there  is  a  live function 

waiting for the return from the recursively  called function.  Write  a function that  will show  you  how 

many recursive calls you can make before the interpreter breaks (you will get an error at the end ‐ it’s 

expected. We’ll cover how to deal with these soon).'''


#13 encode(string)
def encode(string):

    key={"a":"00","b":"01", "c":"02", "d":"03", "e":"04", "f":"05", "g":"06", "h":"07", "i":"08", "j":"09", "k":"10"}
    coded=""
    for letter in string:
        if letter in key:
            coded = coded + key[letter]
        else: coded = coded + letter
    return coded


#14 decode(string)
def decode(string):
    key={"a":"00","b":"01", "c":"02", "d":"03", "e":"04", "f":"05", "g":"06", "h":"07", "i":"08", "j":"09", "k":"10"}
    inverted_key = dict([[letter,code] for code,letter in key.items()])

    original = ""
    coded_chars = [string[i:i+2] for i in range(0, len(string), 2)]

    for i in coded_chars:
        if i in inverted_key:
            original = original + inverted_key[i]
        else: original = original + i
    return original


'''15 encrypt(word, encryptionkey)*

Any fool could crack our encoding above ‐ it’s a straightforward 1 to 1 mapping of letters to numbers. 

Now, we’re going to encrypt it. The function should be passed a normal string. To do so, we take the 

encoded  string,  and  a  sequence  of  numbers  from  0  to  74.  The  encryption  will  work  by  taking  the 

character, and adding the next number in the encryptionkey and adding it to that character. Then, the 

next letter will add the next element in the key. Note that the key could be longer or shorter than the 

word ‐ if you get to the end of the key, start from the beginning.

example:  encrypt(“abc”,(1,2))‐>“010203”‐>“020404”'''

def encrypt(word,encryptionkey):
    key={"a":"00","b":"01", "c":"02", "d":"03", "e":"04", "f":"05", "g":"06", "h":"07", "i":"08", "j":"09", "k":"10"}
    numbersequence = [i+1 for i in range(74)]
    encrypted =""
    for i in range(len(word)):
        if i in key:
            encrypted = encrypted + key[i]+numbersequence[encryptionkey+i]
        #else: encrypted = encrypted 
        return encrypted


# isn't "list" a function like "print" so won't it cause problems??

'''board=[[0,0,0,0,1,0,0,0], #accessthis1withboard[0][4]

[0,0,0,0,0,0,0,0],

[0,0,0,0,0,0,0,0],

[0,0,0,0,0,0,1,0], #accessthis1withboard[3][6]

[0,0,0,0,0,0,0,0],

[0,1,0,0,0,0,0,0], #accessthis1withboard[5][2]

[0,0,0,0,0,0,0,0],

[0,0,0,0,0,0,0,0],


[0,0,0,0,0,0,0,0]]'''

# sum rows & columns
#sum(board
