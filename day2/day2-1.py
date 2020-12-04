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
	for el in word:
		if el == char:
			charCounter+=1
	if charCounter >= eval(occ[0]) and charCounter <= eval(occ[1]):
		passCounter+=1

print(passCounter)
