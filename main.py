import random

rsp = ['가위', '바위', '보']
result = {0: '비김', 1: '이김', 2: '짐'}

def check(user, com):

    print('컴퓨터:', com)

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
    if user == '끝':
        print('게임을 이용해주셔서 감사합니다 ^__^')
        print('-----------------------------------------\n')
        break

    elif not user in rsp:
        print('다시 입력해주세요')
        print('-----------------------------------------\n')
        continue

    com = random.randint(0,2)
    com = rsp[com]

    check(user, com)
    print('-----------------------------------------\n')

#print('-----------------------------------------\n')