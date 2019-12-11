from django import forms
from blog.models import Post, Comment

class PostForm(forms.ModelForm):
    """ A class to show the Post() model as a form """

    class Meta():

        # connect PostForm() to Post() model
        model = Post

        # show these fields in the form
        fields = ('author', 'title', 'text')

        # widget attribute:
        # > A dictionary to later add classes to widgets in forms
        # > Solves the bootstrap/CSS problem in {{ form.as_p }}
        #   > Key: field   > Val: forms.actualwidget(attrs={class rules})
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'textinputclass'
            }),
            'text': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea postcontent'
            })
        }


class CommentForm(forms.ModelForm):

    class Meta():

        model = Comment

        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={
                'class': 'textinputclass'
            }),
            'text': forms.Textarea(attrs={
                'class': 'editable medium-editor-textarea'
            })
        }
