from datetime import datetime

from django.contrib.auth import get_user_model
User = get_user_model()

import django.forms as forms
from validator.models import ValidationRun


## See https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html
class ValidationRunForm(forms.ModelForm):

    class Meta:
        model = ValidationRun
        ## specify the fields of the model that should be included in the form:
        fields = [
            'interval_from',
            'interval_to',
            'scaling_method',
            'name_tag',
            ]

    scaling_ref = forms.fields.ChoiceField(choices=[(ValidationRun.SCALE_TO_REF, 'Reference'), (ValidationRun.SCALE_TO_DATA, 'Data'), ])

    def __init__(self, *args, **kwargs):
        super(ValidationRunForm, self).__init__(*args, **kwargs)
        ## Specifiy the fields of the model that are OPTIONAL in the form:
        self.fields['interval_from'].required = False
        self.fields['interval_to'].required = False

        ## give default/initial values to widgets
        self.fields['interval_from'].initial = datetime(1978, 1, 1).strftime('%Y-%m-%d')
        self.fields['interval_to'].initial = datetime.now().strftime('%Y-%m-%d')
