from django import forms

preprocessingChoices = (
    ('lower', 'Lower'),
    ('punctuation', 'Punctuation'),
    ('numbers', 'Numbers'),
)

machineLearningChoices = (
    ('tfidf', 'TF IDF'),
    ('freq', 'Frequency'),
)

class SplitForm(forms.Form):
	splitPercent = forms.CharField(label="Split Percentage", max_length = 3)

class PreprocessingForm(forms.Form):
    preprocessingVariables = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=preprocessingChoices,
    )

class MachineLearningForm(forms.Form):
    machineLearningVariable = forms.ChoiceField(
        required=False,
        widget=forms.RadioSelect,
        choices=machineLearningChoices,
    )