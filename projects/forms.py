from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['vote_total','vote_ratio']
        
    def __init__(self,*argr,**kwargs):
          super(ProjectForm, self).__init__(*argr,**kwargs)
          
          for key,value in self.fields.items():
              value.widget.attrs.update()
              
        #   self.fields['title'].widget.attrs.update({'class': 'input'})
