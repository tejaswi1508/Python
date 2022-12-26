#How to get the matching elements in an integer array
#first we declare the array and then run loops to compare the elements of the array and then print the element if its matching
#array1 = [10,20,30,40,50,10,30,50]
array1 = ["a","b","c","d","e","a","c","e"]

for x in range(0, len(array1)):
    for y in range(x+1, len(array1)):
        if array1[x]==array1[y]:
            print(array1[y])
     
