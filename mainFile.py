# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:59:29 2021

@author: vicki
"""

import numpy as np
## advent of Code 2022 Start 

print("Starting advent of code")

##HIER KOMMEN ALLE METHODEN HIN

# diese Methode liest eine File ein und gibt jedes zeilenelement als Teil 
# einer Liste aus
def returnFileFromList(fileName):
    file=open(fileName, "r")
    myList=[]
    for x in file: 
        myList.append(x)
    return myList


#methode um den Input des ersten Tags auszugeben
#gibt de Werten der Ehröhung der Zahlen zurück 
##Error: somehow off with one? 
def day0101Answer(inputList):
    counter =0
    
    first =inputList.pop(0)
    second=0
    length =len(inputList)
    print(length)
    x=0
    while x<length:
        second=inputList.pop(0)
        if second>first:
            counter=counter+1
        first=second
        x=x+1
        
    print(x)
    print("number f increases: ", counter)
    return counter

def day0102Answer(inputList):
    #the variable for counting the number  of increases
    counter =0
    
    length = len(inputList)
    if (length<4):
        return 0
    else :
        first= int(inputList.pop(0)) 
        second= int(inputList.pop(0)) 
        third=int( inputList.pop(0)) 
        
        firstSum=first+second+third
        
        while(len(inputList)>0): 
            first=second
            second=third
            third=int( inputList.pop(0))
            
            secondSum= first+second+third
            
            if (secondSum>firstSum): 
                counter=counter+1
            
            firstSum=secondSum
            
    
    
    print("number f increases in threepart interval: ", counter)
    return counter


#this method implements the day 2 part 1 
def day0201Answer(inputList):
    horizontal= 0
    depth=0
    
    
    while (len(inputList)>0): 
        currentString=inputList.pop(0)
                
        #intpos=len(currentString)-1
        intStr=currentString.split()[1]
        intval=int(intStr)
        
        if (currentString.find("up")>=0):
            depth=depth-intval
        elif ( currentString.find("forward")>=0):
            horizontal=horizontal+intval
        elif (currentString.find("down")>=0): 
            depth=depth+intval
        else: 
            print("couldnt deal with this string: ", currentString)
        
    
    ##should be done now with moving the submarine
    print(" current horizontal position: ", horizontal)
    print(" current depth: ", depth)
    print("current test score: ", depth*horizontal)
    return depth*horizontal

#this method implements the day 2 part 2
def day0202Answer(inputList):
    horizontal= 0
    depth=0
    aim=0
    
    while (len(inputList)>0): 
        currentString=inputList.pop(0)
                
        #intpos=len(currentString)-1
        intStr=currentString.split()[1]
        intval=int(intStr)
        
        if (currentString.find("up")>=0):
            aim=aim-intval
        elif ( currentString.find("forward")>=0):
            depth=depth+aim*intval
            horizontal=horizontal+intval
        elif (currentString.find("down")>=0): 
            aim=aim+intval
        else: 
            print("couldnt deal with this string: ", currentString)
        
    
    ##should be done now with moving the submarine
    print("Part 2 Answers: ")
    print(" current horizontal position: ", horizontal)
    print(" current depth: ", depth)
    print("current test score: ", depth*horizontal)
    return depth*horizontal
        

#this returns the answer of the day 3 puzzle 
# bits to gamma and epsilon rate
def day0301Answer(myInputList): 
    #number of elements to check out
    numElements= len(myInputList)
    
    #get the first element in order to get the length of each BitField
    currentBitField= myInputList.pop(0)
    
    
    #get legnth of input number in order to know how long the Bitcounter Array has to be
    numbOfBits= len(currentBitField)
    #this array holds track of how often a one appears at the corresponding position
    Bitscounter=np.zeros(numbOfBits)
    
    ##add the object again in order to iterate over list element
    myInputList.append(currentBitField)
    
    for strBits in myInputList: 
        #strBits ist nun der entsprechende String
        
        #iterieren über alle chars
        #for mit range betrachtet nicht das letzte Element
        for x in range (0,numbOfBits):
            Bitscounter[x]=Bitscounter[x]+int(strBits[x])
        
    ##umwandeln der Bitcounters in Zahlen
    
    gammaRate=0
    epsilonRate=0
    for x in range(0,numbOfBits):
        if (Bitscounter[x]/numElements>0.5): 
            gammaRate=gammaRate+2**(numbOfBits-x-1)
        else: 
            epsilonRate=epsilonRate+2**(numbOfBits-x-1)
    print("final gamma Rate: ", gammaRate)
    print("final epsilon rate: ", epsilonRate)
    print("final solution: ", gammaRate*epsilonRate)
    return gammaRate*epsilonRate

## input: 
def getDecimalFromBinaryString(inputArray): 
    #get number of elements
    numbOfBits= len(inputArray)
    #define returnnumber
    retNumber=0
    for x in range(0,numbOfBits):
            retNumber+=int(inputArray[x])*2**(numbOfBits-x-1)
    return retNumber
    
    
#this method returns the        
def day0302Answer(myInputList):
    # start with the oygen generator rater oxygenRate
    myOxyGenRateList=myInputList.copy()
    pos=0
    mostCommonBit=0
    while (len(myOxyGenRateList)>1): 
        
        bitSummation=0
        #summiere auf um das total zu kriegen, x ist dabei immernoch ein String
        for x in myOxyGenRateList: 
            bitSummation+= int(x[pos])
        
        if (bitSummation/len(myOxyGenRateList) >=0.5):
            mostCommonBit=1
        else: 
            mostCommonBit=0
        
        #sortiere die Elemente aus, die nicht das most Common Bit an der Stelle haben
        filtered = filter(lambda c: int(c[pos]) == mostCommonBit, myOxyGenRateList)
        myOxyGenRateList=list(filtered)
        #setze Position eins weiter 
        pos+=1
    
    #jetzt sllte nur nch ein String in der Liste sein -> kann umgewandelt werden in den 
    #gewollten Wert
    oxyGenRate= getDecimalFromBinaryString(myOxyGenRateList.pop(0))
    
    #now same for CO2scrubberrating
    myCO2List= myInputList.copy()
    pos=0
    leastCommonBit=0
    
    while (len(myCO2List)>1): 
        
        bitSummation=0
        #summiere auf um das total zu kriegen, x ist dabei immernoch ein String
        for x in myCO2List: 
            bitSummation+= int(x[pos])
        
        if (bitSummation/len(myCO2List) >=0.5):
            leastCommonBit=0
        else: 
            leastCommonBit=1
        
        #sortiere die Elemente aus, die nicht das most Common Bit an der Stelle haben
        filtered = filter(lambda c: int(c[pos]) == leastCommonBit, myCO2List)
        myCO2List=list(filtered)
        #setze Position eins weiter 
        pos+=1
    
    #jetzt sllte nur nch ein String in der Liste sein -> kann umgewandelt werden in den 
    #gewollten Wert
    CO2scrubRate= getDecimalFromBinaryString(myCO2List.pop(0))
    
    print("oxgen generation rate is: ", oxyGenRate)
    print("CO2 scrubber rate is: ", CO2scrubRate)
    print(" quiz output: ", oxyGenRate*CO2scrubRate)
    
    
    

##Day 1
#myList=returnFileFromList("day0101.txt")
#x=day0101Answer(myList)
#Test List for day 1 
#myList2=[199,200,208,210,200,207,240,269,260,263]

#day0102Answer(myList)

##Day 2
#myDay2TestList= ["forward 5", "down 5","forward 8","up 3", "down 8","forward 2"]
#myDay2InputList= returnFileFromList("day0201.txt")
#day0201Answer(myDay2TestList)
#print("actual input calculation: ")
#day0201Answer(myDay2InputList)

#day0202Answer(myDay2TestList)
#day0202Answer(myDay2InputList)

##Day 3

myDay3TestList= ["00100","11110", "10110","10111","10101","01111","00111","11100","10000","11001","00010","01010"]
#myDay3TestList=returnFileFromList("day03Test.txt")
myDay3InputList= returnFileFromList("day0301.txt")

#testen: 
#day0301Answer(myDay3TestList)
print("DOES THIS WORK WITH THE ACTUAL INPUT?:")

#try removing spaces in Input list
#myDay3InputList = [line.replace(' ', '') for line in myDay3InputList]
myDay3InputList = [line.strip() for line in myDay3InputList]
#day0301Answer(myDay3InputList)

#filtered = filter(lambda c: int(c[0]) == 1, myDay3TestList)
#myC02List= list(filtered)
#print("I like big butss")
day0302Answer(myDay3InputList)





        