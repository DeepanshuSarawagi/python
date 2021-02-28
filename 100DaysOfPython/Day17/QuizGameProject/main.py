from question_model import Question
from data import question_data

question_bank = []

for q in question_data:
    question_bank.append(Question(text=q["text"], answer=q["answer"]))
