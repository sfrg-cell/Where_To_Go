from django import forms

PLACE_TYPES = [
    ("Ресторан", "Ресторан"),
    ("Кав'ярня", "Кав'ярня"),
    ("Парк", "Парк"),
    ("Інше", "Інше"),
]


class CreatePlace(forms.Form):
    name = forms.CharField(label="Назва місця", max_length=50)
    location = forms.CharField(label="Локація", max_length=100, required=False)
    place_type = forms.ChoiceField(label="Тип місця", choices=PLACE_TYPES)
    rating = forms.IntegerField(label="Рейтинг (від 1 до 5)", min_value=1, max_value=5)
    description = forms.CharField(label="Опис", widget=forms.Textarea, max_length=100)
