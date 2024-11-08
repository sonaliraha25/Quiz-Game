from data import question_data
from questionmodel import Question
from quizbrain import QuizBrain

question_bank=[]
for question in question_data:
    text=question['question']
    ans=question['correct_answer']
    new_question=Question(text,ans)
    question_bank.append(new_question)
quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("You have completed the game")