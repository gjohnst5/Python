import question_model
import data
import quiz_brain

question_bank = []

for i in data.question_data:
    question_bank.append(question_model.Question(i["text"], i["answer"]))

quiz = quiz_brain.QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
