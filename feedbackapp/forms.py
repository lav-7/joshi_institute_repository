from django import forms

class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'placeholder':"Your name please",
                'class':"form-control",
            }
        )
    )

    rating=forms.IntegerField(
        label="Enter your Rating",
        widget=forms.NumberInput(
            attrs={
                'placeholder':"Your Rating Please",
                'class':"form-control",
            }
        )
    )


    feedback=forms.CharField(
        label="Enter your feedback",
        widget=forms.Textarea(
            attrs={
                'placeholder':"Your feedback please",
                'class':"form-control",
            }
        )
    )


    '''date=forms.DateTimeField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'placeholder':"Your name please",
                'class':"form-control",
            }
        )
    )'''
