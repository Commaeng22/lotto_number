import random

print('\n로또번호 생성기 입니다\n')
limitcycle = input("몇회 실행 할까요? ")
filename = input("결과가 저장될 txt 파일명을 입력하세요 : ")

lotto_cycle = 0 #반복문의 시작

while lotto_cycle < int(limitcycle): #n번 반복 엑셀은 1048576줄 까지 한번에 가능
    lotto = random.sample(range(1, 45), 6)
    lotto.sort() #추출된 숫자를 오름차순 정렬
    converted_list = [str(element) for element in lotto] #리스트를 문자형 자료로 변환
    joined_string = ",".join(converted_list)
    f = open('%s.txt' % filename , 'a') # W : 새로 쓴다, a : 추가한다. 추가를 해야 누적된다.
    f.write(joined_string)
    f.write('\n') #줄바꿈을 한다
    f.close()
    lotto_cycle = lotto_cycle + 1
    #print(joined_string, lotto_cycle)
    print(lotto_cycle)

exit()