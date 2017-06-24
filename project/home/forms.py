from django import forms

class SearchForm(forms.Form):
    filter_locality=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class' : 'w3-input w3-border'}),
    )
    filter_city=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class' : 'w3-input w3-border'})
    )
    opts=(
        ('All','All'),
        ('Malnutrition', 'Malnutrition'),
        ('Education', 'Education'),
        ('Poverty', 'Poverty'),
        ('Social Welfare', 'Social Welfare'),
        ('Hygiene and Sanitation', 'Hygiene and Sanitation'),
    )
    filter_topic=forms.ChoiceField(
        choices=opts,
        required=True,
        widget=forms.Select(attrs={'class':'w3-select'}),
    )

    # filter_topic = (
    #    (1, ("Mr.")),
    #    (2, ("Ms.")),
    # )
    # prefix = forms.ChoiceField(choices=filter_topic)

    def __init__(self,*args,**kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['filter_locality'].label = "Locality"
        self.fields['filter_city'].label = "City"
        self.fields['filter_topic'].label = "Topic"

class SuggestionForm(forms.Form):
    name=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'w3-input w3-border w3-hover-border-black','style':'width:100%'})
    )
    email=forms.EmailField(
        required=True,
        widget=forms.TextInput(attrs={'class':'w3-input w3-border w3-hover-border-black'})
    )
    subject=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'w3-input w3-border w3-hover-border-black'})
    )
    message=forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class':'w3-input w3-border w3-hover-border-black'})
    )