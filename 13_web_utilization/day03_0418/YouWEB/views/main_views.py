from flask import Blueprint, render_template, request
from YouWEB.model import Question

bp = Blueprint('main',
               __name__,
               template_folder='templates',
               url_prefix = '/')


## 라우팅 함수들

@bp.route('/')
def index() : 
    # Question 테이블에 저장된 데이터 읽어서 출력 
    question_list = Question.query.order_by(Question.create_date.desc())

    # return f"<h3> HI HI </h3> {question_list}"
    return render_template('q_list.html', question_list = question_list)
                                                                                # ㄴ 이 안에는 question 객체가 여러개 들어있는거
                                                                                #    그래서 html에서 for문 돌면서 하나씩 꺼내게끔 한다.



## 새로운 질문 등록 URL
@bp.route('/question/create')
def create_question():
    return render_template(template_name_or_list='q_create.html')


## 등록된 질문 확인 
@bp.route('/new_q_list', methods = ['POST'])
                            # ㄴ 여기서 methods도 반드시 같이 적어주어야 폼에 작성된 것이 받아온다
def new_question_list():
    subject = request.form['subject']
    content = request.form['content']
    return f"subject {subject} <br>content {content}"





# 내가 시도했던 방법 (안된다 ㅂㄷㅂㄷ) -------------------------------------------------------------------------------------------

# # 질문을 입력받는 함수 
# @bp.route('/new_q/')
# def new_question():
#     return render_template(template_name_or_list="new_q.html",
#                             action = "/new_q_list/",
#                             method = "POST") 






# 책에서 본 저장된 질문 보는 code -----------------------------------------------------------------------------------------------
# @bp.route('/')
# def index() : 
#     # Question 테이블에 저장된 데이터 읽어서 출력 
#     question_list = Question.query.order_by(Question.create_date.desc())

#     # return f"<h3> HI HI </h3> {question_list}"
#     return render_template('question/question_list.html', question_list = question_list)


# @bp.route('/detail/<int:question_id>/')
# def detail(question_id):
#     question = Question.query.get(question_id)
#     return render_template('question/question_detail.html', question = question)
# ------------------------------------------------------------------------------------------------------------------------------