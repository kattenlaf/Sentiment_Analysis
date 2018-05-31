File1 = open('newFile.txt', 'r')
File2 = open('Test.csv', 'r')

num1 = 0;
num2 = 0;

for word in File1:
	++num1;
for word in File2:
	++num2;

print num1
print "\n"
print num2