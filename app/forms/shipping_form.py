from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired
from app.map.map import map


class ShippingForm(FlaskForm):
  sender_name = StringField('', [DataRequired()], render_kw={"placeholder" : 'Sender Name'})
  recipient_name = StringField('', [DataRequired()], render_kw={"placeholder" : 'Recipient Name'})
  origin = SelectField('Origin', [DataRequired()], choices=map.keys())
  destination = SelectField('Destination', [DataRequired()], choices=map.keys())
  is_express = BooleanField('Express Shipping')
  submit = SubmitField('Submit')
