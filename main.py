from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in range(0 , len(question_data)):
    questiono = Question(question_data[i]["question"], question_data[i]["correct_answer"])
    question_bank.append(questiono)
quizbraino = QuizBrain(question_bank)
while quizbraino.still_has_questions():
    quizbraino.next_question()

print("You have completed the Quiz!!")
print("Your final score is" , quizbraino.score , "/" , quizbraino.q_number)