import random

rsp = ['가위', '바위', '보']  #list에 가위 바위 보 저장
result = {0: '비김', 1: '이김', 2: '짐'} #딕셔너리에 승패 저장

def check(user, com): # 승패를 확인하는 함수

    print('컴퓨터:', com) # 컴퓨터의 랜덤 값 출력

    if user == com:
        print(result.get(0))
    elif user == '가위' and com == '바위':
        print(result.get(2))
    elif user == '바위' and com == '보':
        print(result.get(2))
    elif user == '보' and com == '가위':
        print(result.get(2))
    else:
        print(result.get(1))

print('\n-----------------------------------------')
print('가위바위보 게임^_^')
print('게임을 끝내려면 "끝"을 입력하세요\n')

while True:
    user = input('입력해주세요>> ')
    if user == '끝': #유저가 끝을 입력한 경우
        print('게임을 이용해주셔서 감사합니다 ^__^')
        print('-----------------------------------------\n')
        break

    elif not user in rsp: # rsp 리스트에 없는 값을 입력했을 경우
        print('다시 입력해주세요')
        print('-----------------------------------------\n')
        continue

    com = random.randint(0,2) #랜덤 값 0~2중 하나 부여
    com = rsp[com] #받은 값을 리스트의 값으로 변환

    check(user, com) #check함수 호출
    print('-----------------------------------------\n')
