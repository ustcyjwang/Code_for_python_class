print("This is a python code for homework7-3: Read and Write")
f = open("hw7_3_READ_DAT.txt", encoding="utf-8")
temp = f.read()
f.close()

f = open("hw7_3_WRITE_DAT.txt", mode="w", encoding="utf-8")
f.write(temp)
f.close()
