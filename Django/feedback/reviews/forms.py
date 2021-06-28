from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=100, label="Your Name", error_messages={
        "required": "Your name cannot be empty",
        "max_length": "Name cannot exceed 100 characters"
    })
    review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)
