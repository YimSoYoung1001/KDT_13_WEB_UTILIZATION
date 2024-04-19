# -----------------------------------------------------------------------------
# 역할 : 데이터 저장 및 출력 관련 웹 페이지 라우팅 처리 
# URL : /input
#       /input/save
#       /input/delete
#       /input/update
# -----------------------------------------------------------------------------

## 모듈 로딩 
from flask import Blueprint, render_template, request
import os, datetime
from PIL import Image

## BP 인스턴스 생성
data_BP = Blueprint('data', 
                    __name__, 
                    template_folder = 'templates', 
                    url_prefix='/input/') 

## 라우팅 함수들
# 처음 데이터를 입력받는 함수 
@data_BP.route('')
def input_data():
    return render_template(template_name_or_list="input_data.html",
                            action = "/input/save_by_method",
                            method = "POST") 



# get / post 방식에 따라 데이터 저장을 달리 해보기
@data_BP.route('save_by_method', methods = ['POST','GET'])
def save_method_data():
    if request.method == 'POST':
        method = request.method
        # headers = request.headers
        # args = request.args.to_dict()
        # v = request.form['value']
        # m = request.form['text']

        # 이미지 파일 경로 
        dir = './MyWeb/static/img/'
        suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
        file = request.files['file']
        save_dir = os.path.join(dir, file.filename + suffix)

        # 이미지 저장 
        file.save(save_dir)
        
        # 불러올 이미지 경로
        open_dir = '../static/img/' + file.filename + suffix
        img_tag = f"<img src = '{open_dir}'>"

        #return f' save post data <br>method : {method} <br>headers : {headers} <br>args = {args} <br>value = {v} <br>text = {m} <br>file : {file}'
        #return f"file name = {f}"
        return f"file : {file} <br> save_dir : {save_dir} <br> img_tag : {img_tag}"


    else :
        # 요청 데이터 추출
        req_dict = request.args.to_dict()

        # return f'save get data : {req_dict}'
        return render_template('save_data.html', **req_dict)










# get 방식으로 데이터 저장 처리 함수
# 사용자의 요청 즉, request 객체에 데이터 저장되어 있음 
@data_BP.route('save_get')
def save_get_data():
    # 요청 데이터 추출
    req_dict = request.args.to_dict()

    # return f'save get data : {req_dict}'
    return render_template('save_data.html', **req_dict)




# post 방식으로 데이터 저장 처리 함수
@data_BP.route('save_post', methods = ['POST'])
def save_post_data():
    # 요청 데이터 추출
    method = request.method
    headers = request.headers
    args = request.args.to_dict()
    v = request.form['value']
    m = request.form['text']
    return f'save post data <br>method : {method} <br>headers : {headers} <br>args = {args} <br>value = {v} <br> text = {m}'
    



    

