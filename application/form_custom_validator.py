from wtforms import ValidationError
from application.models import Company


class NumericFieldValidator(object):
    def __init__(self, message=None):
        if not message:
            message = "Field must contain only numbers."
        self.message = message

    def __call__(self, _, field):
        if field.data and (not str(field.data).isdigit()):
            raise ValidationError(self.message)
        

class UniqueFieldValidator(object):
    def __init__(self, message=None):
        if not message:
            message = "Field already exists."
        self.message = message

    def __call__(self, form, field):
        
        field_map = {
            "phone_number": Company.query.filter_by(phone_number=field.data).first(),
            "work_email": Company.query.filter_by(work_email=field.data).first()
        }

        existing_record = field_map.get(field.name)

        if existing_record:
            raise ValidationError(self.message)