## 모듈 로딩
from YouWEB import db

## Question 테이블 클래스
## 컬럼 : id, subject, content, create_date
class Question(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    subject = db.Column(db.String(200), nullable = False)
    content = db.Column(db.Text(),nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)

## Answer 테이블 클래스
## 컬럼 : id, question_id, question, content, create_date
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete = 'CASCADE'))
    question = db.relationship('Question', backref = db.backref('answer_set'))
    content = db.Column(db.Text(), nullable = False)
    create_date = db.Column(db.DateTime(), nullable = False)