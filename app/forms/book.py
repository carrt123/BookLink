from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, DataRequired, NumberRange


class SearchForm(Form):
    q = StringField(validators=[Length(min=1, max=30), DataRequired()])
    page = IntegerField(validators=[NumberRange(min=1, max=90)], default=1)
