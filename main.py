from question import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    new_q = Question(i["text"], i["answer"])
    question_bank.append(new_q)


