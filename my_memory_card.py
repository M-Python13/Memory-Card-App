from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QGroupBox, QHBoxLayout, QLabel, QMessageBox, QPushButton,QRadioButton, QVBoxLayout, QWidget)
from random import shuffle,randint

app = QApplication([])
my_win =QWidget()

my_win.setWindowTitle("Memory Card")

question = QLabel()

RadioGroupBox = QGroupBox("Answer Options")
rtbn1    = QRadioButton()
rtbn2    = QRadioButton()
rtbn3    = QRadioButton()
rtbn4    = QRadioButton()

layout_quest = QHBoxLayout()
layout_quest.addWidget(rtbn1)
layout_quest.addWidget(rtbn2)

layout_quest2 = QHBoxLayout()
layout_quest2.addWidget(rtbn3)
layout_quest2.addWidget(rtbn4)

layout_quest3 = QVBoxLayout()
layout_quest3.addLayout(layout_quest)
layout_quest3.addLayout(layout_quest2)
RadioGroupBox.setLayout(layout_quest3)

button= QPushButton("Answer")

score = QLabel()
score.hide()

layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()

layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
layoutH3.addWidget(button, alignment = Qt.AlignCenter)

layout_v = QVBoxLayout()

layout_v.addLayout(layoutH1)
layout_v.addLayout(layoutH2)
layout_v.addLayout(layoutH3)


RadioGroupBox2 = QGroupBox("Result:")
text = QLabel("Correct or Incorrect") 
correct_ans = QLabel() 

Box2Layout1 = QHBoxLayout()
Box2Layout2 = QHBoxLayout()

Box2Layout1.addWidget(text)
Box2Layout2.addWidget(correct_ans)

Box2LayoutV = QVBoxLayout()

Box2LayoutV.addLayout(Box2Layout1)
Box2LayoutV.addLayout(Box2Layout2)
RadioGroupBox2.setLayout(Box2LayoutV)
 
RadioGroup = QButtonGroup()
RadioGroup.addButton(rtbn1)
RadioGroup.addButton(rtbn2)
RadioGroup.addButton(rtbn3)
RadioGroup.addButton(rtbn4)

layoutH2.addWidget(RadioGroupBox2, alignment = Qt.AlignCenter)

my_win.setLayout(layout_v)

class Question:
    def __init__(self,question,wrong1,wrong2,wrong3,correct_ans):
        self.question = question
        self.correct_ans = correct_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.Appearance = True

questions_list = [Question("Which nationality does not exist?", "Enets","Chylums","Smurfs", "Aleuts"),
Question("Which flag in the world does not feature red, white or blue?", "Senegal", "Vietnam","Hungary", "Jamaica"),
Question("What is the national language of Ivory Coast?", "English", "Ivorian", "German", "French"),
Question("Which is NOT a state in the USA?", "Washington","Kansas", "Ohio", "New York City"),
Question("Which is a mounatin range in Europe?", "Himayalas", "Rocky Mountains", "Atlas", "Alps")
]

cur_question = 0
my_win.que_tot = 0
my_win.que_cor = 0

def show_question():
    RadioGroupBox.show()
    RadioGroupBox2.hide()
    button.setText("Answer")
    question.show()
    RadioGroup.setExclusive(False)
    rtbn1.setChecked(False)
    rtbn2.setChecked(False)
    rtbn3.setChecked(False)
    rtbn4.setChecked(False)

def show_answer():
    RadioGroupBox.hide()
    RadioGroupBox2.show()
    button.setText("Next question")
    question.show()
    RadioGroupBox2.show()

my_win.count_question = -1

answers = [rtbn1, rtbn2, rtbn3, rtbn4]   
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.correct_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    show_question()

def check_answer():
    if answers[0].isChecked():
        res = ("Correct")
        my_win.que_cor +=1
    else:
        res = ("Incorrect")
    show_correct(res)

def next_question():
    my_win.que_tot += 1
    cur_question = randint(0,len(questions_list) - 1)
    q = questions_list[cur_question]
    if my_win.que_tot != 8:
        ask(q)
    else:
        score.show()
        button.hide()
        score.setText("Score is " + str(my_win.que_cor/my_win.que_tot * 100) + "%") 

def click_OK():
    if button.text() == "Answer":
        check_answer()
    else:
        next_question()

def show_correct(res):
    text.setText(res)
    show_answer() 

next_question()                                             

show_question() 

button.clicked.connect(click_OK)
my_win.show()
app.exec_()