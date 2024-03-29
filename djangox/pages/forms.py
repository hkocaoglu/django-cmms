from django import forms
from pages.models import Work


class WorkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(WorkForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['detail'].widget.attrs.update({'class' : 'myfieldclass'})
    # create meta class
    class Meta:
        # specify model to be used
        model = Work
 
        # specify fields to be used
        fields = [
            "name",
            "detail"
        ]
    
