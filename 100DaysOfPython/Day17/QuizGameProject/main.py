from question_model import Question
from data import question_data
import quiz_brain

question_bank = []

for q in question_data:
    question_bank.append(Question(text=q["text"], answer=q["answer"]))

quiz1 = quiz_brain.QuizBrain(question_bank)
quiz1.next_question()
