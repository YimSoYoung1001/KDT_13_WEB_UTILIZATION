def generate_caption(image):
    # 저장된 모델 돌릴 클래스
    import torch.nn
    import torch
    import torchvision.transforms as transforms
    from PIL import Image
    class mymodel(nn.Module):
        pass

    # 모델 인스턴스 생성
    model = mymodel()

    # 저장된 모델 로딩
    model_file = '../static/model/sign_3.pth'
    model.load_state_dict(torch.load(model_file))

    img = '../static/img/sample.jpg'

    # 모델이 학습된 형태의 이미지로 변화 (전처리 같게끔)
    preprocessing = transforms.Compose([
        transforms.Resize((150, 150)),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
    ])
    p_img = preprocessing(img)

    # 모델 시연
    model.eval()

    with torch.no_grad():
        output = model(p_img)
        result = torch.argmax(output, dim=1).item()

    return f"result is {result}"