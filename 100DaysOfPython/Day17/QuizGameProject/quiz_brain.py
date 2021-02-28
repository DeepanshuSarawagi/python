class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        choice = input("Q{}: {} True/False?: ".format(self.question_number, question.text))
        ans = ""
        for i in range(len(choice)):
            if i == 0:
                ans += choice[i].upper()
            else:
                ans += choice[i]
        self.check_answer(ans, question.answer)

    def still_has_question(self):

        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, answer, correct_answer):

        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!!")
            print("Your current score is {}/{}".format(self.question_number, self.score))
        else:
            print("That's wrong!!")
        print("The correct answer was {}.".format(correct_answer))
