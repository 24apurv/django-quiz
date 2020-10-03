[![DeepSource](https://deepsource.io/gh/24apurv/django-quiz.svg/?label=active+issues&show_trend=true)](https://deepsource.io/gh/24apurv/django-quiz/?ref=repository-badge)

# Django Quiz Application
A quiz application created in django to conduct mcq quizzes. The application has the following features : 
1) Add/update/delete questions from admin.
2) JavaScript timer
3) Random questions from set of questions
4) Production ready

# Installation
1) Install python3
2) Install pip for python3
3) Install virtualenv
  `pip install virtualenv` or `pip3 install virtualenv`
4) Create virtual environment and cd into it
  `virtualenv django-quiz --python python3 && cd django-quiz`
5) Clone git repository into src folder and cd into it `git clone <url> src && cd src`
6) Install requirements `pip install -r requirements.txt` or `pip3 install -r requirements.txt`
7) Make appropriate changes to settings module and make migrations using `python manage.py makemigrations` and then 
  `python manage.py migrate`
8) Run using `python manage.py runserver`
9) Create superuser to log into admin `python manage.py createsuperuser`

# Implementation
1) Add questions from admin
2) Conduct the quiz
3) To get results, run the results script `python manage.py runscript -v2 results`
4) To send reviews, run the reviews script `python manage.py runscript -v2 reviews`
  WARNING : Reviews script will send emails to all participants.
            Make sure to update email settings in settings module.
            Try not to use fake emails to avoid sending emails to random people.
            
            
