from question_model import Question
from data import question_data
from quizz_brain import quizz_brain
question_list = []


for one_question in question_data:
    question_t = (one_question["question"])
    question_a = (one_question["correct_answer"])
    new_question = Question(question_t,question_a)
    
    question_list.append(new_question)


quizz = quizz_brain(question_list)


while quizz.has_question()==True:
    quizz.next_question()


