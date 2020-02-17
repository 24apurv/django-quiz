from django.contrib import admin
from .models import *

admin.site.register(MyUser)
admin.site.register(Answer)
admin.site.register(Question, AdminQuestion)
admin.site.register(Result)
admin.site.register(UserAnswer)