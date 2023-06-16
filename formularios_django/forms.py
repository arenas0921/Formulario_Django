from django import forms


class ComentarioForm(forms.Form):
    nombre = forms.CharField(label="Escribe tu nombre ", max_length=100, help_text="100 cararacteres maximo")
    url = forms.EmailField(label="Tu sitio web", required=False, initial='http://')
    comentario = forms.CharField()


class ContactoForm(forms.Form):
    nombre = forms.CharField(label="Nombre: ", max_length=10,
                             widget=forms.TextInput(attrs={'class': 'inputnombre'}))
    email = forms.EmailField(label="Email: ", max_length=10)
    mensaje = forms.CharField(label="Mensaje")

    def clean_mombre(self):
        nombre = self.cleaned_data.get("nombre")
        if nombre != "Roland":
            raise forms.ValidationError("Solo se permite Roland en el nombre")
        else:
            return nombre

    def clean(self):
        x = super().clean()
        nombre = x.get("nombre")
        if nombre:
            self.clean_mombre()
        return x