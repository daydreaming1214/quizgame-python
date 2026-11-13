from quiz_game import QuizGame
from quiz_data import quizzes


def main():
    game = QuizGame(quizzes)
    game.load_state()
    game.run()


if __name__ == "__main__":
    main()