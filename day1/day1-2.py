f = open("text.txt", "r")

text = f.readlines()
list = []
for i in text:
	list.append(eval(i))

f.close()

for i in range(len(list)):
	for j in range(i+1, len(list)):
		for k in range(j+1, len(list)):
			if(list[i] + list[j] + list[k] == 2020):
				print(list[i] * list[j] * list[k]) 
