from django import forms
from .models import Review


# class ReviewForm(forms.Form):
#     user_name = forms.CharField(max_length=100, label="Your Name", error_messages={
#         "required": "Your name cannot be empty",
#         "max_length": "Name cannot exceed 100 characters"
#     })
#     review_text = forms.CharField(label="Your feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)

# We have commented out above code because we will be creating the ReviewForm by
# implementing the ModelForm class
# Instead of having a class to render the data and have an another class to save the
# data in the DB, we can extend the the forms using ModelForm class. There will be a
# connection between Models and Forms. We will be ultimately saving the data which we get
# from the Forms entered by the user to the Db models.
# Doing this we will let Django create a form based on the Model and its fields


class ReviewForm(forms.ModelForm):  # Creating a ModelForm
    class Meta:
        model = Review  # Telling Django to establish a connection to the desired Model.
        # it should refer to. This connects the ReviewForm to the Review Model

        # fields = ['user_name', 'review_text', 'rating']  # Here we can specify which Model fields we want to show to
        # the user
        fields = '__all__'  # This will display all the Model fields in the form to the user
        # exclude = ['review_text']  # Exclude the Model fields which Django shouldn't render in the form
        labels = {
            "user_name": "Your Name",
            "review_text": "Your Review",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Your name cannot exceed 100 characters"
            }
        }