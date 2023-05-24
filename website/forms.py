from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField ,SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class OpinionForm(FlaskForm):
    def capitalize_first_letter(form, field):
        field.data = field.data.capitalize()

    rating = SelectField('Ocena', choices=[(str(i), str(i)) for i in range(5, 0, -1)], validators=[DataRequired()])
    name = StringField('Imię', validators=[DataRequired(), Length(max=50), capitalize_first_letter])
    opinion = TextAreaField('Twoja opinia...', validators=[DataRequired(), Length(max=500), capitalize_first_letter])
    submit = SubmitField('Prześlij opinię')