from quiz.models import MyUser, UserAnswer, Answer
import pandas as pd
import numpy as np

def run():
	'''
	Script to fetch results. Submitted answers and questions are pulled from db. Actual answers and given answers are 
	compared and score is incremented accordingly. Excel sheet is created with scores in descending order to give 
	actual ranks of participants. 
	'''
	userAnswers = UserAnswer.objects.all()
	data = dict()
	try:
		for userAnswer in userAnswers:
			score = 0
			questions = userAnswer.questions.split(',')
			answers = userAnswer.answers.split(',')
			for i,question_id in enumerate(questions):
				correct_answer = Answer.objects.get(question_id=question_id).correct_answer
				if correct_answer == answers[i]:
					score = score+1
			data[str(userAnswer.user)] = score
		sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
		dataframe = pd.DataFrame(data=sorted_data, columns=['Participant', 'Score'])
		dataframe.index = np.arange(1, len(dataframe)+1)
		dataframe.to_excel("results.xlsx")
	except:
		pass