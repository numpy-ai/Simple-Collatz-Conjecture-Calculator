# 콜라츠 추측의 계산에 따라 값을 구하는 함수
# @param 2 이상의 정수
def toCollatz(num):
    colCnt = 0
    while True:
        if num % 2 == 0:
            num /= 2
            colCnt += 1
            print(num, end = " ")
            if colCnt % 10 == 0:
                print()
            if num == 1:
                print()
                break
        if num % 2 == 1:
            num = 3 * num + 1
            colCnt += 1
            print(num, end=" ")
            if colCnt % 10 == 0:
                print()


logList = []

while True:
    try:

        select = int(input(" 1. 콜라츠 추측 계산하기\n 2. 지금까지 입력한 숫자 확인하기\n 3. 숫자 기록 삭제하기\n 4. 종료하기\n"))

        if select == 1:
            isInputNum = int(input("숫자를 입력해주세요: "))
            toCollatz(isInputNum)
            logList.append(isInputNum)

        elif select == 2:
            cnt = 1
            for i in range(len(logList)):
                print(f"#{cnt}: {logList[i]}")
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
