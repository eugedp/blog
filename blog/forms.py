from django import forms
from .models import * 
from django.contrib.auth.forms import UserCreationForm



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content','image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})
        }




class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(widget=forms.EmailInput())

    class Meta:
        model = Customer
        fields = ["username", "password", "email", "full_name", "address"]

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Customer with this username already exists.")

        return uname


class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


# Questo modulo è un ModelForm basato sul modello BlogPost creato in precedenza.
# La classe Meta viene utilizzata per specificare il modello su cui si basa il modulo
# e i campi che devono essere inclusi nel modulo.
# In questo esempio, i campi nel modulo sono 'titolo', 'contenuto' e 'immagine' che sono
# gli stessi campi nel modello BlogPost.

# Puoi anche utilizzare gli attributi dei widget nella classe Meta per specificare diversi 
# tipi di widget per ogni campo del modulo.  
# Questo aggiungerà la classe 'form-control' ai campi title e content, e 'form-control-file' 
# al campo immagine Una volta definito il modulo, puoi usarlo nella vista create_blog_post 
# che ho fornito in precedenza per gestire la creazione di nuovi post del blog.
# Per favore fatemi sapere se avete domande o se c'è qualcos'altro in cui posso aiutarvi.


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirmation = forms.CharField(widget=forms.PasswordInput)


