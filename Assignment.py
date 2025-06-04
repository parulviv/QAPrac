'''5. How would you use slicing to create a new list containing only the even-indexed elements of a
given list?
 Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 Expected output : [0, 2, 4, 6, 8]

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list[1:10:2])


city = "ETLQALabs"
#Expected O/P : QAlab

print(city[3:8:1])

city = "ETLQALabs"

#output:  “sbaL AQ LTE”

print(city[::-1])

list1 =[1,2,4,3]

uni=[]
dup=[]

for x in list1:
    if x not in uni:
     uni.append(x)
    else:
        dup.append(x)

print(uni)
print(dup)

if len(dup)!=0:
     print("list has duplicate")
else:
    print("list has no duplicates")


s1={1,3,4,5}
s2={3,5,6,7}
print(s1.intersection(s2))
print(s1.union(s2))
List = [1,2,3,4,5,1,3]
count=0
d={}
for i in List:

    d[i]=d.get(i,0)+1

print(d)

#1.	Write a function to return a list with all the duplicate elements from the list

l1=[3,5]

def sum_list(l1):
 sum = 0
 for x in l1:
  sum=sum+x
 print("sum of list is",sum)



sum_list(l1)

#4.	Write a program to find the largest number in the list and return.


l1=[1,4,5,4,7,8]

def duplist(l1):

 s1=set(l1)
 print(s1)


duplist(l1)



List = [1,2,3,4,5,1,3]
count=0
d={}
for i in List:

    d[i]=d.get(i,0)+1

print(d)


list1 =[1,2,5,6,2,5,3]
def dup(list1):
 uni=[]
 dup=[]

 for x in list1:
    if x not in uni:
     uni.append(x)
    else:
        dup.append(x)

 print(uni)
 print(dup)

 if len(dup)!=0:
     print("list has duplicate")
 else:
    print("list has no duplicates")

dup(list1)


def findDuplicateElements(inputList):
    # initiate an empty dictionary to count the occurrence of each elements
    # initiate an empty list to store all the duplicate elements only and return to the function
    dictionaryForElementsCounts = {}
    listOfDuplicateElements = []

    # Iterate through the input list and store the occurrences of each element in dictionary
    for element in inputList:
        if element in dictionaryForElementsCounts:
            dictionaryForElementsCounts[element] += 1
        else:
            dictionaryForElementsCounts[element] = 1

    # Add all the duplicate elements in the list ( which are having counts > 1 )
    for element, count in dictionaryForElementsCounts.items():
        if count > 1:
            listOfDuplicateElements.append(element)

    return listOfDuplicateElements

    # Calling and execute the function
inputList =[1, 2, 3, 1, 7, 3,4, 2, 5, 6,]
ansList = findDuplicateElements(inputList)
print(ansList)


'''

def printTheBiggestNumber(inputList):
    bn = inputList[0]
    # Iterate through the list and compare find the biggest number
    for x in inputList:
        if bn < x:
            bn = x
    print("The biggest number from the given list is :",bn)
# Calling and execute the function
inputList =[1,2,9,3,4,5]
printTheBiggestNumber (inputList)


























