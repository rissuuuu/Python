import os

file = open('D:/file.txt', 'w')
file.write("This is the text written into the file \n another fileis also written")
file.close()

file1 = open('D:/file.txt', 'r')
print(file1.read())
file1.close()
#os.rename('D:/file.txt','D:/file.txt')
#os.remove('D:/risu.txt')


