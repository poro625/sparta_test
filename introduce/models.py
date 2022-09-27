from django.db import models

class AccessLog(models.Model):

    
    created_at = models.DateTimeField('접속 시간' , auto_now_add=True)
    updated_at = models.DateTimeField('수정 시간' , auto_now=True)
    location =  models.CharField('접속 경로' , max_length=50)
    # user = # 누가접속했는지 수집하고싶은 데이터를  여기에 작성하면 된다
