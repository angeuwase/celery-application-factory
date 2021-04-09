from flask_mail import Message 
#from . import mail, celery, app
from . import mail, celery
#from flask import current_app


#@celery.task(name='app.email.send_celery_email', bind=True)
#def send_celery_email(self,message_data):

  #  app = current_app._get_current_object()
   # with app.app_context():

    #    message = Message(subject=message_data['subject'], recipients= [message_data['recipients']], body= message_data['body'])
    #    mail.send(message)


#def send_email(email):
   # message_data = {
          #  'subject': 'Hi from Flask app',
          #  'recipients': email,
           # 'body': 'This is an email sent from the flask app' 
        #}
    #send_celery_email.apply_async(args=[message_data], queue='IO')


from flask import current_app



@celery.task(name='app.email.send_celery_email', bind=True)
def send_celery_email(self,message_data):
    app = current_app._get_current_object()

    message = Message(subject=message_data['subject'],sender=app.config['MAIL_DEFAULT_SENDER'],  recipients= [message_data['recipients']], body= message_data['body'])
    mail.send(message)

@celery.task(name='app.email.reverse_name', bind=True)
def reverse_name(self,name):
    #app = current_app._get_current_object()
    return name[::-1]