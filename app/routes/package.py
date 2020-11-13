from flask import Blueprint, render_template, request, redirect
from app.forms.shipping_form import ShippingForm

bp = Blueprint('package', __name__, url_prefix='/package')


@bp.route('/new', methods=['GET', 'POST'])
def new_package():
  form = ShippingForm()
  if form.validate_on_submit():
    print(form.data)
    return redirect('/')
  form = ShippingForm()
  return render_template('shipping_request.html', form=form)
