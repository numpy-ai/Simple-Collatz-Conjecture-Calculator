
# 콜라츠 추측의 계산에 따라 값을 구하는 함수
# @param 2 이상의 정수
def to_collatz(num):
    col_cnt = 0
    while True:
        if num % 2 == 0:
            num /= 2
            col_cnt += 1
            data = "%d " % num
            print(data, end="")
            record_file.write(data)
            if col_cnt % 10 == 0:
                print()
                record_file.write("\n")
            if num == 1:
                print()
                break
        if num % 2 == 1:
            num = 3 * num + 1
            col_cnt += 1
            data = "%d " % num
            print(data, end="")
            record_file.write(data)
            if col_cnt % 10 == 0:
                print()
                record_file.write("\n")

    record_file.close()


log_list = []
record_file = open("record.txt", "w")

while True:
    try:
        select = int(input(" 1. 콜라츠 추측 계산하기\n 2. 지금까지 입력한 숫자 확인하기\n 3. 숫자 기록 목록에서 삭제하기\n 4. 메모장에 열기\n 5. 종료하기\n"))

        if select == 1:
            input_num = int(input("숫자를 입력해주세요: "))
            if input_num <= 0:
                print("1 이상의 수를 입력해주세요.")
            else:
                to_collatz(input_num)
                log_list.append(input_num)

        elif select == 2:
            cnt = 1
            for i in range(len(log_list)):
                print(f"#{cnt}: {log_list[i]}")
                cnt += 1
            if not log_list:
                print("기록된 숫자가 없습니다.")

        elif select == 3:
            print("기록을 삭제했습니다.")
            log_list.clear()

        elif select == 4:
            print("결과가 기록된 메모장을 엽니다.")
            lines = open("record.txt", 'r')
            for line in lines:
                print(line, end='')
            print()

        elif select == 5:
            print("종료합니다.")
            break

        else:
            print("1~5번 기능만 구현돼 있습니다.")
    except ValueError:
        print("1~5번만 입력해주시길 바랍니다.")
