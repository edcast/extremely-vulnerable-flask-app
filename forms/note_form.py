from wtforms import Form, validators, TextAreaField, BooleanField, StringField


class NoteForm(Form):
    title = StringField('Title', [validators.DataRequired()])
    text = TextAreaField('Text', [validators.DataRequired()])
    is_private = BooleanField('Is Private', default=False)
