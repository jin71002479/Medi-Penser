from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['subject', 'content', 'file']
       
        labels = {
            'subject': '제목',
            'content': '내용',
            
        }
        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['file'].required = False


class AnswerForm(forms.ModelForm):
    
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
        'content': '답변내용',
        }