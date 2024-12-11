from wtforms import ValidationError
from application.models import Company
from datetime import datetime


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
        
class ExpiryDateValidator:
    def __init__(self, message: str = None):
        if not message:
            message = "Expiry Date must be in the format YYYY-MM-DD HH:MM:SS."
        self.message = message

    def __call__(self, form, field):
        if not field.data:
            return
        
        # Check if the field data is already a datetime object
        if isinstance(field.data, datetime):
            return
        # Check if the field data is a string and strip whitespace
        if isinstance(field.data, str) and field.data.strip():
            try:
                # Validate the format
                datetime.strptime(field.data, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                # Raise validation error if the format is incorrect
                raise ValidationError(self.message)
        else:
            raise ValidationError(self.message)