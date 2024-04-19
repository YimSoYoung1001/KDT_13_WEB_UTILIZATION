## 모듈 로딩 
from flask import Blueprint, render_template, request
import os, datetime, torch
import cgi, sys, codecs, datetime
from PIL import Image
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms


## BP 인스턴스 생성 -----------------------------------------------------------------------------
data_BP = Blueprint('data', 
                    __name__, 
                    template_folder = 'templates', 
                    url_prefix='/') 



## 라우팅 함수 -----------------------------------------------------

# 데이터 입력 받음
@data_BP.route('')
def input_data():
    return render_template(template_name_or_list='index.html')


# get/post 방식에 따른 데이터 return 
@data_BP.route('save_show', methods = ['POST', 'GET'])
def save_show():
    headers = request.headers
    args = request.args.to_dict()

    if request.method == 'POST':
        # 서버로 들어오는 이미지 저장할 경로
        dir = './work_web/static/img/'
        suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
        file = request.files['img_file']
        save_dir = os.path.join(dir, suffix + file.filename)
        
        # 이미지를 로컬에 저장
        file.save(save_dir)

        # 로컬에서 불러올 이미지 경로 및 부르기
        open_dir = '../static/img/' + suffix + file.filename
        img_tag = f"<img src='{open_dir}'>"
        
        ## 모델 돌릴 준비 -------------------------------------------------------------------------------
        # 모델 돌릴 클래스 
        class my_model(nn.Module):
            def __init__(self):
                super(my_model, self).__init__()
                self.conv1 = nn.Conv2d(in_channels=3, out_channels=8, kernel_size=3, padding=1)
                # 채널 수          커널수         커널 사이즈,
                self.conv2 = nn.Conv2d(in_channels=8, out_channels=16, kernel_size=3, padding=1)
                self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
                self.fc1 = nn.Linear(8 * 8 * 16, 64)
                self.fc2 = nn.Linear(64, 32)
                self.fc3 = nn.Linear(32, 8)  # class는 총 8개

            def forward(self, x):
                x = self.conv1(x)
                x = F.relu(x)
                x = self.pool(x)
                x = self.conv2(x)
                x = F.relu(x)
                x = self.pool(x)

                x = x.view(-1, 8 * 8 * 16)  # 차원을 변경함
                x = self.fc1(x)
                x = F.relu(x)
                x = self.fc2(x)
                x = F.relu(x)
                x = self.fc3(x)
                x = F.log_softmax(x)
                return x

        # 모델 로딩
        model = my_model()

        model_file = '../static/img/mood_400.pth'
        print(model_file)
        model.load_state_dict(torch.load(model_file))
        print('model 로딩 완료')

        # 모델이 학습된 형태의 이미지로 변환 
        preprocessing = transforms.Compose([
            transforms.Resize(size = (32, 32)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])

        # 이미지 전처리 
        img = Image.open(open_dir)
        p_img = preprocessing(img)

        # 모델 시연
        model.eval()

        with torch.no_grad():
            output = model(p_img)
            result = torch.argmax(output, dim = 1).item()

        # 분석된 결과에 따라 어떤 분위기/감정인지 알려주기
        mood_dict = {'0':'angry', '1':'anxiety', '2':'depressed', '3':'dynamic', '4':'happy', '5':'peaceful', '6':'tired', '7':'withered'}
        mood = mood_dict[f"{result}"]
        print(f"<h2>your image has <span style='color:blue;'>{mood}</span> mood</h2><br><hr>")

        # 노래 추천 
        song_mood = {'angry':'1', 'anxiety':'2', 'depressed':'3', 'dynamic':'4', 'happy':'5', 'peaceful':'6', 'tired':'7', 'withered':'8'}
        song_opposite = {'angry':'6', 'anxiety':'5', 'depressed':'5', 'dynamic':'6', 'happy':'6', 'peaceful':'6', 'tired':'5', 'withered':'5'}
        
        # explain mood
        song_num = song_mood[f'{mood}']
        mp3_path = f'song_0{song_num}'
        print(f'<h2> this song will <span style = "color: orange;">EXPLAIN</span> your mood.</h2>')
        print(f"<h4>(song number is {song_num})</h4><br>")

        # change mood
        song_num2 = song_opposite[f'{mood}']
        mp3_path2 = f'song_0{song_num2}'
        print(f'<h2> but, this song will <span style = "color: orange;">CHANGE</span> your mood.</h2>')
        print(f"<h4>(song number is {song_num2})</h4>")


        return f"headers : {headers} <br>args : {args} <br>img : {img_tag} <br>mood : {mood} <br>explain num : {song_num}"

    else : 
        # 서버로 들어오는 이미지 저장할 경로
        dir = './work_web/static/img/'
        suffix = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
        file = request.files['img_file']
        save_dir = os.path.join(dir, file.filename + suffix)
        
        # 이미지를 로컬에 저장
        file.save(save_dir)

        # 로컬에서 불러올 이미지 경로
        open_dir = '../static/img/' + file.filename + suffix
        img_tag = f"<img src='{open_dir}'>"

        return f"headers : {headers} <br>args : {args} <br>img<br>{img_tag}"