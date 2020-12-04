f = open("text.txt", "r")

list = f.read().splitlines()

f.close()

#example: 1-3 a: abcde
passCounter = 0
for i in list:
	el = i.split(" ")
	occ = el[0].split("-")
	char = el[1][0]
	word = el[2]
	charCounter = 0
	if word[eval(occ[0])-1] == char:
		charCounter += 1
	if word[eval(occ[1])-1] == char:
		charCounter += 1
	if charCounter == 1:
		passCounter+=1

print(passCounter)
