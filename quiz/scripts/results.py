from quiz.models import MyUser, UserAnswer, Answer
import pandas as pd
import numpy as np

def run():
	userAnswers = UserAnswer.objects.all()
	score = 0
	data = dict()
	for userAnswer in userAnswers:
		questions = userAnswer.questions.split(',')
		answers = userAnswer.answers.split(',')
		for i,question_id in enumerate(questions):
			correct_answer = Answer.objects.get(pk=question_id).correct_answer
			if correct_answer == answers[i]:
				score = score+1
		data[str(userAnswer.user)] = score
	sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
	dataframe = pd.DataFrame(data=sorted_data, columns=['Participant', 'Score'])
	dataframe.index = np.arange(1, len(dataframe)+1)
	dataframe.to_excel("results.xlsx")