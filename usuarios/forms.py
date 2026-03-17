from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label="Nome de login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: Roberto Carlos"
            }
        )
    )
    
    senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
    
    
class CadastroForms(forms.Form):
        nome_cadastro = forms.CharField(
            label = "Nome de Cadastro",
            required = True,
            max_length= 100,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: Roberto Carlos"
                }
            )
        )
        email=forms.EmailField(
            label = "Email",
            required = True,
            max_length= 150,
            widget = forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Ex.: Joao@gmail.com"
                }
            )
        )
        
        senha=forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )
        
        senha_2=forms.CharField(
        label="Confirme sua senha",
        required=True,
        max_length=70,
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha novamente"
            }
        )
    )
        
        
        def clean_nome_cadastro(self):
            nome = self.cleaned_data.get('nome_cadastro')

            if nome:
                nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
            else:
                return nome  
            
        
            
            
        def clean_senha(self):
            senha = self.cleaned_data.get('senha')
            senha_2 = self.cleaned_data.get('senha_2')
            
            if senha and senha_2:
                if senha  != senha_2:
                    raise forms.ValidationError("Senhas não são iguais")
                else:
                    return senha_2
                