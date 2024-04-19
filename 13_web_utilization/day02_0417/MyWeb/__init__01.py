### Application Factory 기반의 Flask Server 구동

## 모듈 로딩 
from flask import Flask, render_template, url_for


### Application Factory 기반의 함수 정의
### 함수명 : create_app 변경 불가
### 반환값 : Flask Server 인스턴스
def create_app():
    ## Flask Server 인스턴스 생성
    app = Flask(__name__)

    ## Blueprint 인스턴스 등록 : 서브 카테고리의 페이지 라우팅 기능
    # app.register_blueprint()
    @app.route('/')
    def index():
        # return "<h1>hello 쿠다사이</h1>"
        return render_template('index.html')
        # 이미 폴더 경로들은 다 정해져있으므로 파일명만 적어주어도 된다. 
        # 그래서 다른 폴더, 다른 폴더명에 하면 못읽어드린다. (설정을 바꾸면 읽을수는 있지만,, 굳이?)
    
    ## 데이터 전송하는 라우팅 => 변수<타입:변수명>
    # http://127.0.0.1:5000/user/000
    @app.route('/user/<name>')
    def user_info(name):
        # return f"<h1>Hello {name}</h1>"
        return render_template('index.html', name = name)

    ## 테스트 기능 (이거는 실제 웹에 적용X, 경로 잡힌게 성공했는지 확인하기 위함)
    with app.test_request_context():
        print(url_for("static", filename =  'css/style_1.css'))
        print(url_for("static", filename =  'img/dog.jpg.css'))

    ## Flask Server 인스턴스 반황
    return app