from wtforms import ValidationError


class NumericValidator(object):
    def __init__(self, message="Field"):
        self.message = message + " must contain only numbers."

    def __call__(self, _, field):
        if field.data and (not str(field.data).isdigit()):
            raise ValidationError(self.message)
        