from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_bank.append(Question(text=q["text"], answer=q["answer"]))

quiz1 = QuizBrain(question_bank)

while quiz1.still_has_question():
    quiz1.next_question()

print("You have completed the quiz. Your final score is {}/{}.".format(quiz1.score, quiz1.question_number))
