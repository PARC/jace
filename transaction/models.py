from user_model.models import *
# Create your models here.
class message:
    User = models.ForeignKey(User)
    Intervention = models.ForeignKey(Intervention)
    Survey = models.ForeignKey(Survey)
    Question = models.ForeignKey(Question)
