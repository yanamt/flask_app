from pathlib import Path
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from apps.config import config

#SQLAlchemyをインスタンス化する
db=SQLAlchemy()
csrf=CSRFProtect()

#create_app関数の作成
def create_app(config_key):
    #Flaskインスタンス生成
    app=Flask(__name__)
    #config_keyに対応する環境のconfigクラスを読み込む
    app.config.from_object(config[config_key])
    #アプリのコンフィグ設定
    """
    app.config.from_mapping(
        SECRET_KEY="2ajwjduxodfhpgj223er3red",
        SQLALCHEMY_DATABASE_URI=f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        #SQLをコンソールに出力する
        SQLALCHEMY_ECHO=True,
        WTF_CSRF_SECRET_KEY="Aucdioskcok0l"
    )
    """
    #SQLAlchemyとappを連携
    db.init_app(app)
    csrf.init_app(app)
    #Migrateとappを連携
    Migrate(app,db)
    #crudアプリからviewsをimportする
    from apps.crud import views as crud_views
    #register_blueprintでcrudをアプリに登録
    app.register_blueprint(crud_views.crud,url_prefix="/crud")

    #authアプリからviewsをインポート
    from apps.auth import views as auth_views
    #blueprintを追加
    app.register_blueprint(auth_views.auth,url_prefix="/auth")

    return app

