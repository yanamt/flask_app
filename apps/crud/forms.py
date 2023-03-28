from flask_wtf import FlaskForm 
from wtforms import PasswordField,StringField,SubmitField
from wtforms.validators import DataRequired,Email,length

#ユーザー新規作成とユーザー編集フォームクラス
class UserForm(FlaskForm):
    #ユーザーフォームのusername属性のラベルとバリデーターを設定
    username=StringField(
        "ユーザー名",
        validators=[
            DataRequired(message="ユーザー名は必須です"),
            length(max=30,message="30文字以内でお願いします"),
        ],
    )
    #ユーザーフォームのemail属性のラベルとバリデーターを設定
    email=StringField(
        "メールアドレス",
        validators=[
            DataRequired(message="メールアドレスは必須です"),
            Email(message="メールアドレスの形式で入力してください"),
        ],
    )
    #ユーザーフォームのpassword属性のラベルとバリデーターを設定
    password=PasswordField(
        "パスワード",
        validators=[
            DataRequired(message="パスワードは必須です")
        ]
    )
    #submit部分
    submit=SubmitField("新規登録")