import random
import time
import datetime

print('\n로또번호 생성기 입니다\n')
limitcycle = input("몇회 실행 할까요? ")
filename = input("결과가 저장될 txt 파일명을 입력하세요 : ")


data = list(range(1,46)) #1~45까지의 숫자 리스트 생성

start_time = time.time()
lotto_cycle = 0 #반복문의 시작

while lotto_cycle < int(limitcycle): #n번 반복 엑셀은 1048576줄 까지 한번에 가능
  random.shuffle(data) #data를 랜덤으로 섞음
 # print("로또 예상번호 : %s" % (data[:6]))
  sort_data = data[:6] #램덤으로 섞은 데이타에서 첫 6자리 숫자를 추출
  sort_data.sort() #추출된 숫자를 오름차순 정렬
  converted_list = [str(element) for element in sort_data] #리스트를 문자형 자료로 변환
  joined_string = ",".join(converted_list)
  f = open('%s.txt' % filename , 'a') # W : 새로 쓴다, a : 추가한다. 추가를 해야 누적된다.
  f.write(joined_string)
  #f.write('\n') #줄바꿈을 할때
  f.write(',') #줄바꿈을 안할때(카운트용)
  f.close()
  lotto_cycle = lotto_cycle + 1
#  print(joined_string)
  print('총',limitcycle,'회중',lotto_cycle,'회 실행중 입니다.') #몇회 돌았는지 보여주기

stop_time = time.time()
total_time = stop_time - start_time

result = datetime.timedelta(seconds=total_time) #0:00:00초 형태로 표시

print('총', lotto_cycle, '번 완료했습니다.')
#print('총 소요시간은', float(result),"입니다.")
print('총 소요시간은', result,"입니다.")

exit()
