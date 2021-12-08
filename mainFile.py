# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 09:59:29 2021

@author: vicki
"""

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

myList=returnFileFromList("day0101.txt")
##open file 
file =open("day0101.txt","r" )

##make loop to check the elements

counter =0

#myList=[199,200,208,210,200,207,240,269,260,263]

first =myList.pop(0)
second=0
length =len(myList)
print(length)
x=0
while x<length:
    second=myList.pop(0)
    if second>first:
        counter=counter+1
    first=second
    x=x+1
    
print(x)
print("number f increases: ", counter)
    
        