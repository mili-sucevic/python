count = 10
while(count > 0):
	print("*" * count)
	count -= 1

for i in range(2,10):
	print("*" * i)

myStr = "test"
for a in myStr:
	print(a)

myList = ["Hey there!!", "How's it going?", "More words", "small talk", "..." ]
for s in myList:
	print(s)

for i in range(0, 10):
	if i == 8:
		break
		print("In IF:", i)
	print(i)

for i in range(0, 10):
        if i == 8:
                continue
                print("In IF:", i)
        print(i)

for i in range(0, 10):
        if i < 8:
                pass
        print(i)
