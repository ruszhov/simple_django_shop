from django import forms
from .models import *

# class SubscriberForm(forms.ModelForm):	#означає що форма буде створена на основі моделі Subscribers(поля теж з моделі , їх там два)
# 	class Meta:
# 		model = Subscriber
# 		#fields = [""]
# 		exclude = [""]
# 		