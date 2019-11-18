from django import forms
from .models import Item, Message


class ItemAddForm(forms.ModelForm):
    class Meta:
        model = Item
        widgets={
        'item_name':forms.TextInput(attrs={'style':'line-height:7px;'}),
        'item_description':forms.TextInput(attrs={'style':'padding:0px;'}),
        'item_location':forms.TextInput(attrs={'style':'padding:0px;'})

        }
        fields = [
        'item_name',
        'item_description',
        'item_price',
        'item_delivery',
        'item_location',
        'item_preferred_payment_method',
        'item_condition',
        'item_categories',
        'item_photo',
        'latitude',
        'longitude'
        ]

class SendMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
        'receiver',
        'subject',
        'text'
        ]
        widgets = {'receiver': forms.TextInput}