# ctrl + shift + P => 커널 설정 

### 모듈 로딩 
from flask import Flask , render_template, Blueprint



### 애프리케이션 팩토리 함수
def create_app():
    myapp=Flask(__name__)

    # bp 등록
    from ..views import main_views
    myapp.register_blueprint(blueprint = main_views.bp)
    
    return myapp




# ### 전역변수
# myapp = Flask(__name__)  # 인스턴스 생성


# ### 사용자 요청 URL 처리 기능 => 라우팅 (Routing)
# ### 형식 : @Flask_instance_name.route(URL문자열)
# ### 웹 서버의 첫 페이지 : http://127.0.0.1:5000
# @myapp.route("/")         # 위의 기본값은 적지 않는다.
# def index_page():
#     # return "<h3><font color = 'green'>My Web Index Page</font></h3>"
#     return render_template("tem.html")


# # http://127.0.0.1:5000/test 이렇게 접속하고자 한다면
# # @myapp.route('/test')      이렇게 적어야하는것 


# ### 사용자마다 페이지 반환
# ### 사용자 페이지 URL : http://127.0.0.1:5000/<username>
# @myapp.route("/<name>")   # 만약 꺽쇠가 없었다? 그러면 변동되는 게 아니라 ㄹㅇ string인 username으로 존재
# def user(name):
#     return f'user: {name}'


# @myapp.route("/<int:number>")
# def show_number(number):
#     return f"select number {number}"


# @myapp.route("/user_info2")
# def user_login2():
#     return myapp.redirect('/')


# ### 실행 제어
# if __name__ == '__main__':
#     # Flask 웹 서버 구동
#     myapp.run(debug = True)              # 서버 구동 시작
