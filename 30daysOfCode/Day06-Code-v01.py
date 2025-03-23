# Enter your code here. Read input from STDIN. Print output to STDOUT
listRange = int(input())
listString = []
i = 0
while i < listRange:  
    element = input()
    listString.append(element)
    i+=1
for string in listString:
    even = []
    odd = []
    for index, char in enumerate(string):
        if index%2==0:
            even.append(char)
        if index%2!=0:
            odd.append(char)

    evenList = ''.join(even)
    oddList = ''.join(odd)

    print(evenList, oddList)
    #print(oddList)
