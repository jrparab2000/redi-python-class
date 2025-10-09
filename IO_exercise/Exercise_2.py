path = r"D:\redi_a25_python\IO_exercise"
write = r"\exercise2.txt"
read = r"\story.txt"

rf = open(path+read, 'r')
wf = open(path+write, 'w')

wf.write(rf.read())

wf.close()
rf.close()

wf = open(path+write,'r')
list_lines = wf.readlines()

dict_words = {}

for i in list_lines:
    words = i.split()
    for j in words:
        if j in dict_words.keys():
            dict_words[j] += 1
        else:
            dict_words[j] = 1

print(dict_words)