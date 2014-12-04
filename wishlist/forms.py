from django import forms
from wishlist.models import Gift,UserInfo
from django.contrib.auth.models import User

class GiftForm(forms.ModelForm):
	short_name = forms.CharField(max_length=250, help_text="I want... ")
	description = forms.CharField(max_length=500, required=False, help_text="Extra description (size, color, style, .etc)")
	link = forms.URLField(max_length=600, required=False, help_text="Link (http://...)")
	user = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.HiddenInput(), required=False)

	class Meta:
		model= Gift
		fields = ('short_name','description','link',)

	def clean(self):
	    cleaned_data = self.cleaned_data
	    url = cleaned_data.get('link')

	    # If url is not empty and doesn't start with 'http://', prepend 'http://'.
	    if url and not url.startswith('http://'):
	        url = 'http://' + url
	        cleaned_data['link'] = url

	    return cleaned_data

class UserInfoForm(forms.ModelForm):
	address_street = forms.CharField(max_length=200)

	address_city = forms.CharField(max_length=200)
	address_state = forms.CharField(max_length=2)

	address_zip = forms.IntegerField()
	user = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.HiddenInput(),required=False)
	class Meta:
		model=UserInfo
		fields=('address_city','address_state','address_street','address_zip',)