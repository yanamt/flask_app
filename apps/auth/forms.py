from flask_wtf import FlaskForm
from wtform import PasswordField, StringField, SubmitField,ValidationError

class SignUpForm(FlaskForm):
    username=StringField("ユーザー名")
    email=StringField("メールアドレス")
    password=PasswordField("パスワード")
    submit=SubmitField("新規登録")

    def validate_name(self,username):
        #usernameのvalidate
        if username.data=="":
            raise ValidationError("ユーザー名を入力してください")
        if len(username.data)>15:
            raise ValidationError("ユーザー名は15字以内にしてください")
    
    def validate_email(self,email):
        #メールアドレスのvalidate
        if email.data=="":
            raise ValidationError("メールアドレスを入力してください")
        if "@" not in email.data:
            raise ValidationError("メールアドレス形式で入力してください")

    def validate_password(self,password):
        if password.data=="":
            raise ValidationError("パスワードを入力してください")
    


