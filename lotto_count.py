import time

starttime = time.time()

file = open('1억.txt', "r")
 
text = file.read() 
 
wordList = text.split(',')
 
wordCount = {} 
 
for word in wordList:
 
    # Get 명령어를 통해, Dictionary에 Key가 없으면 0리턴
 
    wordCount[word] = wordCount.get(word, 0) + 1 
    
    keys = sorted(wordCount.keys())
 
for word in keys:
 
    print(word + ':' + str(wordCount[word])) 

endtime = time.time()
total_time = endtime - starttime

print('총 소요시간은', float(total_time),"초 입니다.")