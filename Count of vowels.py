#the number of vowels and consonants in a String

string = input("Enter any string: ")

vowels = ('a', 'e', 'i', 'o', 'u');
vows = 0

for x in string.lower():
    if x in vowels:
        vows += 1
print("number of vowels: %d" %vows)
print("number of cons: %d" %(len(string)-vows))
