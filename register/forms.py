from django import forms
from register.models import Group
from django.utils import timezone

class RegisterForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model=Group
        fields='__all__'
        exclude=['gid','final_song','pay_status']

    def __init__(self, *args, **kwargs):
            super(RegisterForm, self).__init__(*args, **kwargs)
            self.fields['category'].widget.attrs.update({
                'class': 'ui dropdown',
                })
            self.fields['group_name'].widget.attrs.update({
                'placeholder':'有團名的話，請告訴我們哦'
                })
            self.fields['cellphone'].widget.attrs.update({
                'placeholder':'0987654321'
                })


    def clean_cid(self):
        pass
        return cid

    def save(self,commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
        return user

