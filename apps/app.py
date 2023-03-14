from flask import Flask

#create_app関数の作成
def create_app():
    #Flaskインスタンス生成
    app=Flask(__name__)
    #crudアプリからviewsをimportする
    from apps.crud import views as crud_views
    #register_blueprintでcrudをアプリに登録
    app.register_blueprint(crud_views.crud,url_prefix="/crud")

    return app
