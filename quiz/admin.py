from django.contrib import admin
from .models import *

# Register models which should be modified my admin
admin.site.register(MyUser)
admin.site.register(Answer)
admin.site.register(Question, AdminQuestion)
admin.site.register(UserAnswer)