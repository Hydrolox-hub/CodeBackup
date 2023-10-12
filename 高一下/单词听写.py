import random

f = open("3500.txt", "r", encoding="UTF-8")
data = list(map(str.strip, f.readlines()))
f.close()

pronounce = {}
meaning = {}
words = []
##for i in range(len(data)//3):
##    w,p,m=data[3*i],data[3*i+1],data[3*i+2]
total=0
for i in range(0, len(data), 3):
    w, p, m = data[i], data[i + 1], data[i + 2]
    words.append(w)
    pronounce[w] = p
    meaning[w] = m
# words为列表，存储所有单词
# pronounce为字典，以单词为键，音标为值
# meaning为字典，以单词为键，释义为值
a = random.sample(words,20)
for word in a:
    print(meaning[word],len(word))
    spell=input()
    if spell=="?":
        print(pronounce[word])
        spell=input()
    if spell==word:
        print("正确，得5分")
        total+=5
    else:
        print("错误，应为",word)
print(total,"/",20*5)
