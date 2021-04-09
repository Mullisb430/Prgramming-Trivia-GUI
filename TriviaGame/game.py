import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from Questions import Questions_
import random
import time

class Game(QMainWindow):
    def __init__(self):
        super(Game, self).__init__()
        loadUi('StartPage.ui', self)
        self.playButton.clicked.connect(self.loadQuestion)
        self.right = 0
        self.wrong = 0
        self.question_ = Questions_
        

    # Questions are loaded up with their corresponding answers.
    def loadQuestion(self):
        loadUi("QuestionPage.ui", self)
        question = random.choice(self.question_)
        self.question_.remove(question)
        for i in question:
            self.question.setText(question[0])
            self.answer1.setText(question[1][1::])
            self.answer2.setText(question[2][1::])
            self.answer3.setText(question[3][1::])
            self.answer4.setText(question[4][1::])
            if (self.right + self.wrong) == 10:
                self.score_()

        # Each answer in the list 'question_' has either an "A" or a "W". "A" Signifies that the answer is correct, while "W" signifies that the answer is incorrect.
        if question[1].startswith("A"):
            self.answer1.clicked.connect(lambda: self.answer1.setStyleSheet("background-color: rgb(255, 255, 255);" + "color: rgb(93, 255, 65);" + "font: 24pt '.AppleSystemUIFont';" + "border-radius: 15%;" + "border: 4px solid rgb(93, 255, 65);"))
            self.answer1.clicked.connect(self.rightAnswer)
        elif question[1].startswith("W"):
            self.answer1.clicked.connect(lambda: self.answer1.setStyleSheet("background-color: rgb(255, 255, 255);" + "color: rgb(93, 255, 65);" + "font: 24pt '.AppleSystemUIFont';" + "border-radius: 15%;" + "border: 4px solid rgb(93, 255, 65);"))
            self.answer1.clicked.connect(self.wrongAnswer)

        if question[2].startswith("A"):
            self.answer2.clicked.connect(lambda: self.answer2.setStyleSheet("background-color: rgb(255, 255, 255);" + "color: rgb(93, 255, 65);" + "font: 24pt '.AppleSystemUIFont';" + "border-radius: 15%;" + "border: 4px solid rgb(93, 255, 65);"))
            self.answer2.clicked.connect(self.rightAnswer)
        elif question[2].startswith("W"):
            self.answer2.clicked.connect(lambda: self.answer2.setStyleSheet("background-color: rgb(255, 255, 255);" + "color: rgb(93, 255, 65);" + "font: 24pt '.AppleSystemUIFont';" + "border-radius: 15%;" + "border: 4px solid rgb(93, 255, 65);"))
            self.answer2.clicked.connect(self.wrongAnswer)
            
        if question[3].startswith("A"):
            self.answer3.clicked.connect(lambda: self.answer3.setStyleSheet("background-color: rgb(255, 255, 255);" + "color: rgb(93, 255, 65);" + "font: 24pt '.AppleSystemUIFont';" + "border-radius: 15%;" + "border: 4px solid rgb(93, 255, 65);"))
            self.answer3.clicked.connect(self.rightAnswer)
        elif question[3].startswith("W"):
            self.answer3.clicked.connect(lambda: self.answer3.setStyleSheet("background-color: rgb(255, 255, 255);" + "color: rgb(93, 255, 65);" + "font: 24pt '.AppleSystemUIFont';" + "border-radius: 15%;" + "border: 4px solid rgb(93, 255, 65);"))
            self.answer3.clicked.connect(self.wrongAnswer)
            
        if question[4].startswith("A"):
            self.answer4.clicked.connect(lambda: self.answer4.setStyleSheet("background-color: rgb(255, 255, 255);" + "color: rgb(93, 255, 65);" + "font: 24pt '.AppleSystemUIFont';" + "border-radius: 15%;" + "border: 4px solid rgb(93, 255, 65);"))
            self.answer4.clicked.connect(self.rightAnswer)
        elif question[4].startswith("W"):
            self.answer4.clicked.connect(lambda: self.answer4.setStyleSheet("background-color: rgb(255, 255, 255);" + "color: rgb(93, 255, 65);" + "font: 24pt '.AppleSystemUIFont';" + "border-radius: 15%;" + "border: 4px solid rgb(93, 255, 65);"))
            self.answer4.clicked.connect(self.wrongAnswer)

    # Adding to the right answer count, and putting a small delay between clicking the 'answer' button and loading the next question
    def rightAnswer(self):
        self.right += 1
        self.loadQuestion()

    # Adding to the wrong answer count, and putting a small delay between clicking the 'answer' button and loading the next question
    def wrongAnswer(self):
        self.wrong += 1
        self.loadQuestion()

    # Once a total of ten questions have been asked, an 'end of game' screen appears. Your score is calculated, and you are shown how you did.
    def score_(self):
        loadUi("EndPage.ui", self)
        score__ = (self.right / (self.right + self.wrong)) * 100

        # If score is below 70 points, the background of the label displaying your score, changes to the color red.
        if score__ <=70:
            self.score.setStyleSheet("font: 86pt 'BoyzRGross';" +
            "color: rgb(255, 255, 255);" +
            "background-color: rgb(255, 0, 0);" +
            "border-radius: 35px;"
            )

        # If score is above 70 points, the background of the label displaying your score, changes to the color green.
        elif score__ > 70:
            self.score.setStyleSheet("font: 86pt 'BoyzRGross';" +
            "color: rgb(255, 255, 255);" +
            "background-color: rgb(0, 255, 0);" +
            "border-radius: 35px;"
            )
        self.score.setText(str(float(score__)))
        self.right = 0
        self.wrong = 0
        self.playButton.clicked.connect(self.loadQuestion)


app = QApplication(sys.argv)
game = Game()
game.setFixedSize(800, 600)
game.show()
app.exec_()