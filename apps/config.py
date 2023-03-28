from pathlib import Path

basedir=Path(__file__).parent.parent

#Baseconfigクラスを生成
class BaseConfig:
    SECRET_KEY="2ajwjduxodfhpgj223er3red"
    WTF_CSRF_SECRET_KEY="Aucdioskcok0l"

#Baseconfigクラスを継承してlocalConfigクラスを生成
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_ECHO=True

#Baseconfigクラスを継承してTestConfigクラスを生成
class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    WTF_CSRF_ENABLED=False

#config辞書にマッピングする
config={
    "testing":TestingConfig,
    "local":LocalConfig
}
