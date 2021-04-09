from . import auth_blueprint
from flask import render_template
#from ..email import send_email
from .forms import RegistrationForm
from ..email import send_celery_email

@auth_blueprint.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():

        
        #send_email(form.email.data)

        message_data = {
            'subject': 'Hi from Flask app',
            'recipients': form.email.data,
            'body': 'This is an email sent from the flask app 2' 
        }
        #send_celery_email.apply_async(args=[message_data], queue='IO')
        send_celery_email.apply_async(args=[message_data])

        return 'Email sent!'
    return render_template('auth/register.html', form=form)