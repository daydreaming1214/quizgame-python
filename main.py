def ask_number(prompt, min_value, max_value):
    """min_value~max_value 범위의 정수를 안전하게 입력받아 반환한다."""
    while True:  # 올바른 입력이 들어올 때까지 반복
        try:
            raw = input(prompt).strip()   # 1) 앞뒤 공백 제거

            if raw == "":                 # 2) 빈 입력(그냥 Enter)
                print("입력이 비어 있습니다. 다시 입력해 주세요.")
                continue

            number = int(raw)             # 3) 숫자 변환 (실패 시 ValueError)

            if number < min_value or number > max_value:  # 4) 범위 검사
                print(f"{min_value}~{max_value} 사이의 숫자를 입력해 주세요.")
                continue

            return number                 # 모든 검사 통과 → 값 반환

        except ValueError:                # 3)의 변환 실패 처리 (예: abc)
            print("숫자만 입력할 수 있습니다. 다시 입력해 주세요.")


def show_menu():
        """메뉴를 출력한다."""
        print("\n===== 파이썬 기초 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")


def run():
    """메뉴를 반복 출력하고 선택을 처리한다."""
    try:
        while True:
            show_menu()
            choice = ask_number("번호를 선택하세요: ", 1, 5)
        
            if choice == 1:
                print("[퀴즈 풀기] 준비 중입니다.")

            if choice == 1:
                print("[퀴즈 풀기] 준비 중입니다.")
            elif choice == 2:
                print("[퀴즈 추가] 준비 중입니다.")
            elif choice == 3:
                print("[퀴즈 목록] 준비 중입니다.")
            elif choice == 4:
                print("[점수 확인] 준비 중입니다.")
            elif choice == 5:
                print("프로그램을 종료합니다. 안녕히 가세요!")
                break

    except (KeyboardInterrupt, EOFError):   # Ctrl+C / 입력 종료
        print("\n프로그램을 안전하게 종료합니다.")


if __name__ == "__main__":
    run()
