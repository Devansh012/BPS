from django import forms
from .models import Project


# creating a form
class ProjectForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Project

		# specify fields to be used
		fields ="__all__" 
		
		