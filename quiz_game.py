from input_utils import ask_number, ask_text
from quiz import Quiz
import json

class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = list(quizzes)
        self.best_score = 0
        self.has_played = False

    def list_quizzes(self):
        print("===== 퀴즈 목록 =====")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for i, quiz in enumerate(self.quizzes, start=1):
            print(f"{i}. {quiz.question}")

        print(f"총 {len(self.quizzes)}개의 퀴즈가 있습니다.")

    def play_quiz(self):
        score = 0
        print("퀴즈 풀기를 시작합니다!")

        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        
        for quiz in self.quizzes:
            quiz.show()

            user = ask_number("정답 번호: ", 1, len(quiz.choices))

            if quiz.is_correct(user):
                print("정답입니다!")
                score += 1
            else:
                print("틀렸어요!")

            print()

        print("===== 퀴즈 결과 =====")
        print(f"총 {len(self.quizzes)}문제 중 {score}문제를 맞혔습니다!")

        self.has_played = True

        if score > self.best_score:
                self.best_score = score
                print("새로운 최고 점수를 기록했습니다!")
       
        self.save_state()

    def add_quiz(self):
        print("===== 새로운 퀴즈 추가 =====")

        question = ask_text("문제를 입력하세요: ")

        choices = []

        for i in range(4):
            choice = ask_text(f"{i + 1}번 선택지: ")
            choices.append(choice)

        answer = ask_number("정답 번호: ", 1, 4)

        new_quiz = Quiz(question, choices, answer)

        self.quizzes.append(new_quiz)

        print("퀴즈가 추가되었습니다!")
        print("현재 퀴즈 개수:", len(self.quizzes))
        
        self.save_state()

    def show_best_score(self):
        print("===== 최고 점수 =====")

        if not self.has_played:
            print("아직 퀴즈를 풀지 않았습니다.")
            return

        print(f"현재 최고 점수: {self.best_score}점")

    def show_menu(self):
        print("\n===== 파이썬 기초 퀴즈 게임 =====")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")

    def run(self):
        try:
            while True:
                self.show_menu()

                choice = ask_number("번호를 선택하세요: ", 1, 5)

                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.list_quizzes()
                elif choice == 4:
                    self.show_best_score()
                elif choice == 5:
                    print("프로그램을 종료합니다.")
                    break

        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 프로그램을 종료합니다.")

    def save_state(self):
        data = {
            "quizzes": [
                {
                    "question": quiz.question,
                    "choices": quiz.choices,
                    "answer": quiz.answer
                }
                for quiz in self.quizzes
            ],
            "best_score": self.best_score,
            "has_played": self.has_played
        }

        with open("state.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("게임 데이터가 저장되었습니다!")

    def load_state(self):
        try:
            with open("state.json", "r", encoding="utf-8") as file:
                data = json.load(file)

            loaded_quizzes = []

            for item in data["quizzes"]:
                quiz = Quiz(
                    item["question"],
                    item["choices"],
                    item["answer"]
                )
                loaded_quizzes.append(quiz)

            self.quizzes = loaded_quizzes
            self.best_score = data["best_score"]
            self.has_played = data.get("has_played", False)

            print("게임 데이터를 불러왔습니다!")

        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            print("저장된 데이터가 없거나 JSON 파일이 손상되었습니다.")
            print("기본 퀴즈로 시작합니다.")

if __name__ == "__main__":
    from quiz_data import quizzes

    game = QuizGame(quizzes)

    game.load_state()
    game.run()