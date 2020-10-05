
#Counting spaces between words
#input file
the_file = open('test.txt')
test = {}

# strip whitespace
for line in the_file:
    line = line.rstrip()
    words = line.split(" ")
     
    for word in words:
        # further study casing addition
        word = word.capitalize() 
        test[word] = test.get(word,0) + 1


print(test)

for test, number in test.items():
    print(f'{test}: {number}')
