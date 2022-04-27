# 콜라츠 추측의 계산에 따라 값을 구하는 함수
# @param 2 이상의 정수
def toCol(num):
    while True:
        if num % 2 == 0:
            num /= 2
            print(num)
            if num == 1:
                break
        if num % 2 == 1:
            num = 3 * num + 1
            print(num)
            if num == 1:
                break

logList = []

while True:
    try:
        print(" 1. 콜라츠 추측 계산하기\n 2. 지금까지 입력한 숫자 확인하기\n 3. 숫자 기록 삭제하기\n 4. 종료하기")
        select = int(input())

        if select == 1:
            isInputNum = int(input("숫자를 입력해주세요: "))
            toCol(isInputNum)
            logList.append(isInputNum)

        elif select == 2:
            cnt = 1
            for i in range(len(logList)):
                print("#%d: %d " % (cnt, logList[i]))
                cnt += 1
            if not logList:
                print("기록된 숫자가 없습니다.")

        elif select == 3:
            print("삭제했습니다.")
            logList.clear()

        elif select == 4:
            print("종료합니다.")
            break

        else:
            print("1~4번 기능만 구현돼 있습니다.")
    except ValueError:
        print("1~4번만 입력해주시길 바랍니다.")
