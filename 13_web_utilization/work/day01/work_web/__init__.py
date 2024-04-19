# ctrl + shift + P => 커널 설정 

### 모듈 로딩 
from flask import Flask , render_template, Blueprint



### 애프리케이션 팩토리 함수
def create_app():
    myapp=Flask(__name__)

    # bp 등록
    from .views import main_views
    myapp.register_blueprint(blueprint = main_views.bp)
    
    return myapp