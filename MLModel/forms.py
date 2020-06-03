from flask_wtf import FlaskForm
from wtforms import SubmitField, DecimalField
from wtforms.validators import DataRequired


class DataForm(FlaskForm):
    sepal_length = DecimalField('Sepal Length', validators=[DataRequired()])
    sepal_width = DecimalField('Sepal Width', validators=[DataRequired()])
    petal_length = DecimalField('Petal Length', validators=[DataRequired()])
    petal_width = DecimalField('Petal Width', validators=[DataRequired()])
    submit = SubmitField('Submit')
