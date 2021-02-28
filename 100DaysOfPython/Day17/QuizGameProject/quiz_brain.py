class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

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
        print(ans)

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
