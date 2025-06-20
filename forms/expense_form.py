from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, FloatField, BooleanField
from wtforms.validators import InputRequired, NumberRange, Optional

class ExpenseForm(FlaskForm):
    age = IntegerField("Age", validators=[InputRequired(), NumberRange(min=1, max=120)])
    gender = RadioField("Gender", choices=[("Male", "Male"), ("Female", "Female")], validators=[InputRequired()])
    income = FloatField("Total Income", validators=[InputRequired(), NumberRange(min=0)])
    utilities = BooleanField("Utilities")
    utilities_amount = FloatField("Amount", validators=[Optional(), NumberRange(min=0)])
    entertainment = BooleanField("Entertainment")
    entertainment_amount = FloatField("Amount", validators=[Optional(), NumberRange(min=0)])
    school_fees = BooleanField("School Fees")
    school_fees_amount = FloatField("Amount", validators=[Optional(), NumberRange(min=0)])
    shopping = BooleanField("Shopping")
    shopping_amount = FloatField("Amount", validators=[Optional(), NumberRange(min=0)])
    healthcare = BooleanField("Healthcare")
    healthcare_amount = FloatField("Amount", validators=[Optional(), NumberRange(min=0)])
