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

def ask_text(prompt):
    while True:
        text = input(prompt).strip()

        if text == "":
            print("빈칸은 입력할 수 없습니다. 다시 입력해 주세요.")
            continue

        return text