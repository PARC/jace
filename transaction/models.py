from user_model.models import *
# Create your models here.
class message:
    User = models.ForeignKey(User)
    Survey = models.ForeignKey(Survey)
    Question = models.ForeignKey(Question)
