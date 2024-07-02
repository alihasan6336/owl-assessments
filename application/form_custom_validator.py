from wtforms import ValidationError
from application.models import Companies


class NumericFieldValidator(object):
    def __init__(self, message="Field"):
        self.message = message + " must contain only numbers."

    def __call__(self, _, field):
        if field.data and (not str(field.data).isdigit()):
            raise ValidationError(self.message)
        

class UniqueFieldValidator(object):
    def __init__(self, message="Some data you entered is"):
        self.message = message + " already exists."

    def __call__(self, form, field):
        existing_record = None

        if field.name == "phone_number":
            existing_record = Companies.query.filter_by(phone_number=field.data).first()
        if field.name == "work_email":
           existing_record = Companies.query.filter_by(work_email=field.data).first()
        
        if existing_record:
            raise ValidationError(self.message)