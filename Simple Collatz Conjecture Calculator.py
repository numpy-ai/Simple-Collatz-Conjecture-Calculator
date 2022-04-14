# 콜라츠 추측의 계산에 따라 값을 구하는 함수
# @param 2 이상의 정수

def col(x) :
	while True :
		if x % 2 == 0 :
			x /= 2
			print(x)
			if x == 1:
				break
		if x % 2 == 1 :
			x  = 3 * x + 1
			print(x)
			if x == 1:
				break


x_list = []
while True :
    print(" 1. 콜라츠 추측 계산하기\n 2. 지금까지 입력한 숫자 확인하기\n 3. 숫자 기록 삭제하기\n 4. 종료하기")
    select = int(input())
    
    if select == 1 :
        x = int(input())
        col(x)
        x_list.append(x)
    
    elif select == 2 :
        cnt = 1
        for i in range(len(x_list)) :
            print("#%d: %d " %(cnt, x_list[i]))
            cnt += 1

    elif select == 3 :
        print("삭제했습니다.")
        x_list.clear()
    elif select == 4 :
        break
    
    else :
        print("1~4번 기능만 구현돼있습니다.")
