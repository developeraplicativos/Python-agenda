from flask  import Flask
from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email 

# app = Flask(__name__) 
 
def validateAtividade(form, field):
    if len(field.data.strip()) < 3:
        raise ValidationError('Sua atividade deve possuir no minímo 4 caracteres')
    else:
        return True
 
def validateEmail(form, field):
    if len(field.data.strip()) < 3:
        raise ValidationError('Sua atividade deve possuir no minímo 4 caracteres')
    else:
        return True
def validateSenha(form, field):
    if len(field.data.strip()) < 3:
        raise ValidationError('Sua atividade deve possuir no minímo 4 caracteres')
    else:
        return True

class FormsAtividades(FlaskForm):
    atividade = StringField("Atividade", validators=[DataRequired(), validateAtividade])
    submit = SubmitField('Enviar')


 