class InvalidUserModel(Exception):
    """The member model you provided is invalid"""
    pass


class EmailTemplateNotFound(Exception):
    """No email template found"""
    pass


class NotAllFieldCompiled(Exception):
    """Compile all the fields in the settings"""
    pass
