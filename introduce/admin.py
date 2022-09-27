from os import access
from django.contrib import admin
from introduce.models import AccessLog


admin.site.register(AccessLog) #'모델을 가지고 와야한다'
