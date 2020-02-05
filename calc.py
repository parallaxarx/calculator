"""
Приложение "Калькулятор"

Автор: Ощепков Евгений
"""
import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QMessageBox, QMenuBar, QHBoxLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont

# ---------------------------------Константы -----------------------------------
eNumber = 2,71828182845 #.......................................... Число Эйлера
pNumber = 3,14159265358 #.............................................. Число Пи
size = 80 #............................................................. Масштаб
board = 20 #..................................................... Ширина отступа
hr = 8*size #....................................................... Высота окна
wr = 8*size #....................................................... Ширина окна
#Размерность списков
cntRow = 5 #................................................... Количество строк
cntCol = 5 #................................................ Количество столбцов

cntCharInLabelMn  = 50 #............. Максимальное количество символов в LabelMn
cntCharInLabelMx  = 23 #............. Максимальное количество символов в LabelMx
cntCharInLabelHis = 15 #............ Максимальное количество символов в labelHis

hlhis = hr  - 2*board #..................................... Высота окна истории
wlhis = (wr - 2*board) * 3/8 #.............................. Ширина окна истории

hlmn = (hr-3*board)//8 #................................ Высота маленького Label
wlmn = wr - wlhis -  3*board #.......................... Ширина маленького Label

hlmx = 2*(hr-2*board)//8 #................................ Высота большого Label
wlmx = wr - wlhis -  3*board #............................ Ширина большого Label

hl = hlmx + hlmn #........................................... Высота обоих Label



hb = (hr - hl - 2*board)//cntRow #................................ Высота кнопок
wb = (wr - wlhis - 3*board)//cntCol #............................. Ширина кнопок
# ------------------------------------------------------------------------------

# ---------------------- Полезные функции --------------------------------------
# X-Факториал (х!)
def factor(x):
    if x > 1:
        return(x*factor(x-1))
    else:
        return(1)
# Корень из х
def sqrt(x):
    return(x**(1/2))
# 1/х
def devision(x):
    return(1/x)
# Экспонента
def exp(x):
    return(eNumber**x)
#-------------------------------------------------------------------------------

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.resize(QSize(wr, hr)) #............................................ Размер окна
        self.setFixedSize(wr, hr)
        self.setWindowTitle('Калькулятор') #.................................... Заголовок

        # Добавление Меню

        # hbox = QHBoxLayout(self)
        # menubar = QMenuBar()
        # menubar.addMenu('&File')
        # hbox.setMenuBar(menubar)

    def initUI(self):

        # -----------------------Список кнопок----------------------------------
        # Массив текста кнопок +++++++++++++++++++++++++++++++++++++++++++++++++
        self.buttonList =   [['+','-','×','÷','C'],
                             ['7','8','9','±','<'],
                             ['4','5','6','(',')'],
                             ['1','2','3','x²','xʸ'],
                             ['.','0','10ˣ','↑','='],]

        self.buttonListAdditional =   [['+','-','×','÷','C'],
                                       ['7','8','9','±','<'],
                                       ['4','5','6','(',')'],
                                       ['1','2','3','√x','⅟ₓ'],
                                       ['.','0','eˣ','↓','='],]
        # Массив кнопок ++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.btn =           [['','','','',''],
                              ['','','','',''],
                              ['','','','',''],
                              ['','','','',''],
                              ['','','','',''],]
        # ------------------------- Стили --------------------------------------
        self.setStyleSheet("""
            QWidget {
                background-color: black;
            }
            QPushButton {
                background-color: gray;
            }
            #labelMx {
                background-color: black;
                color: #C0C0C0	;
            }
            #labelMn {
                background-color: black;
                color: #C0C0C0	;
            }
            #labelHis {
                background-color: black;
                color: #C0C0C0	;
            }
        """)
        # ----------------------------Создание Label----------------------------
        # Маленькое окно *******************************************************
        self.labelMn = QLabel("",self,objectName="labelMn")
        self.labelMn.setFont(QFont('SansSerif',size//8))
        self.labelMn.resize(wlmn,hlmn)
        self.labelMn.move(board,board)
        self.labelMn.show()
        # Большое окно *********************************************************
        self.labelMx = QLabel("",self,objectName="labelMx")
        self.labelMx.setFont(QFont('SansSerif',size//4))
        self.labelMx.resize(wlmx,hlmx)
        self.labelMx.move(board,board+hlmn)
        self.labelMx.show()
        # Окно истории *********************************************************
        self.labelHis = QLabel("",self,objectName="labelHis")
        self.labelHis.setFont(QFont('SansSerif',size//4))
        self.labelHis.resize(wlhis,hlhis)
        self.labelHis.move(2*board + wlmn, board)
        self.labelHis.show()
        # ------------------------Создание кнопок-------------------------------
        for r in range(cntRow):
            for c in range(cntCol):
                self.btn[r][c] = QPushButton(self.buttonList[r][c],self)
                self.btn[r][c].resize(wb,hb)
                self.btn[r][c].move(board + c*(wb), board + hl + r*(hb+1))
                self.btn[r][c].clicked.connect(self.calc)
                self.btn[r][c].setFont(QFont('SansSerif',size//5))
    # ++++++++++++++++++++++++++ Функционал ++++++++++++++++++++++++++++++++++++
    def calc(self):
        sender = self.sender()
        key = sender.text()
        textMn = self.labelMn.text()
        textMx = self.labelMx.text()
        #print(key)
        # Ввод символов ********************************************************
        if key in '1234567890.':
            if '=' in textMn:
                self.labelMn.clear()
                self.labelMx.clear()
            if key == '.':
                if key not in self.labelMn.text():
                    if textMx != '':
                        self.labelMx.setText(self.labelMx.text() + key)
                    else:
                        self.labelMx.setText('0'+ key)
            elif key in '1234567890':
                self.labelMx.setText(self.labelMx.text() + key)
        else:
            if textMx != '':
                if textMx[-1] == '.':
                    textMx = textMx[:-1]
                    self.labelMx.setText(textMx)
                if textMx != '-':
                    if float(textMx)%1 == 0:
                        textMx = str(int(float(textMx)))
                        self.labelMx.setText(textMx)
            # Основной функционал (работает) ***********************************
            if key in '+-×÷':
                if textMx != '':
                    if textMx[-1] == '.':
                        self.labelMx.setText(textMx[:-1])
                # Если уже нажато равно, то выполнять действия над результатом
                if '=' in textMn:
                    self.labelMn.setText(textMx)
                    self.labelMx.clear()
                # Если не пустое поле ввода и там не просто '-'
                if (textMx != '') and (textMx != '-'):
                    if '=' not in textMn:
                        if '-' not in textMx:
                            self.labelMn.setText(textMn + textMx + key)
                        else:
                            self.labelMn.setText(textMn + '(' + textMx + ')' + key)
                    else:
                        self.labelMn.setText(textMx + key)
                    self.labelMx.clear()
                elif textMn != '':
                    if textMn[-1] == ')':
                        self.labelMn.setText(textMn + key)
                elif key == '-':
                    self.labelMx.setText('-')
            # Счёт (работает) **************************************************
            elif key == '=':
                if '=' not in textMn:
                    if textMx != '' or textMn[-1] == ')':
                        if textMn != '':
                            if textMn[-1] == ')' and textMx != '':
                                score = textMn + '×' + textMx
                            else:
                                score = textMn + textMx
                            if (list(score)).count('(')>(list(score)).count(')'):
                                score += ')'*((list(score)).count('(')-(list(score)).count(')'))
                            text = score
                            score = '*'.join(score.split('×'))
                            score = '**'.join(score.split('^'))
                            score = '/'.join(score.split('÷'))
                            result = eval(score)
                            if result%1==0:
                                result = int(result)
                            if '-' not in textMx:
                                self.labelMn.setText(text + key) ##
                            else:
                                if textMn[-1] == ')':
                                    self.labelMn.setText(textMn + '×(' + textMx + ')' + key)
                                else:
                                    self.labelMn.setText(textMn + '(' + textMx + ')' + key)
                            self.labelMx.setText(str(result)) #


                            textHisInput  = text + '=' + str(result) + "\n"
                            textHisOutput = ''
                            c = 0
                            for char in list(textHisInput):
                                textHisOutput += char
                                c += 1
                                if c%cntCharInLabelHis == 0:
                                    textHisOutput += '\n'
                                elif char == '=':
                                    textHisOutput += '\n'
                            self.labelHis.setText(self.labelHis.text() + '----------------------------------------------------------------------------')
                            self.labelHis.setText(textHisOutput + self.labelHis.text() )
                            self.labelHis.setText('----------------------------------------------------------------------------\n'+ self.labelHis.text())

                    # elif textMn[-1] == ')':
                    #     score = textMn + '×' + textMx
            # Очистка окна (работает) ******************************************
            elif key == 'C':
                self.labelMn.clear()
                self.labelMx.clear()
            # Удаление символа (работает) **************************************
            elif key == '<':
                self.labelMx.setText(textMx[:-1])
            # Смена знака (работает) *******************************************
            elif key == '±':
                if ('-' not in textMx) and (textMx != ''):
                    self.labelMx.setText('-' + textMx)
                else:
                    self.labelMx.setText(textMx[1:])
            # Возведение в квадрат (работает) **********************************
            elif key == 'x²':
                self.labelMx.setText(str(eval('(' + textMx +')**2')))
            # Возведение в степень (работает) **********************************
            elif key == 'xʸ':
                if '=' in textMn:
                    self.labelMn.setText(textMx)
                    self.labelMx.clear()
                if (textMx != '') or (textMn == ''):
                    if '=' not in textMn:
                        if '-' not in textMn:
                            self.labelMn.setText(textMn + textMx + '^')
                        else:
                            self.labelMn.setText(textMn + '(' + textMx + ')' + '^')
                    else:
                        self.labelMn.setText(textMx + '^')
                    self.labelMx.clear()
            # ОСтаток от деления (Mod) (Работает)********** убран из функционала
            # elif key == "Mod":
            #     self.labelMn.setText(textMn + textMx + "%")
            #     self.labelMx.clear()
            # 10^x (Работает) **************************************************
            elif key == "10ˣ" and textMx != "":
                self.labelMx.setText(str(10**float(textMx)))
            # Факториал х (x!)  (Работает) *************************************
            elif key == "x!":
                if (textMx != "") and ("." not in textMx) and ("-" not in textMx):
                    try:
                        self.labelMx.setText(str(factor(int(textMx))))
                    except Exception as e:
                        raise
            # Корень (работает) ************************************************
            elif key == "√x":
                self.labelMx.setText(str(sqrt(float(self.labelMx.text()))))
            # 1/х (работает) ***************************************************
            elif key == "⅟ₓ":
                self.labelMx.setText(str(devision(float(self.labelMx.text()))))
            # Экспонента (не работает) **************************************** Исправить ошибку
            elif key == "eˣ":
                self.labelMx.setText(str(exp(float(self.labelMx.text()))))
            # Скобки (работает) ************************************************
            elif key == "(":
                if textMn != '':
                    if textMn[-1] == ')':
                        self.labelMn.setText(textMn + '*(')
                    else:
                        self.labelMn.setText(textMn + '(')
                else:
                    self.labelMn.setText(textMn + '(')
            elif key == ")":
                countOpenBrackets = (list(self.labelMn.text())).count('(')
                countClosedBrackets = (list(self.labelMn.text())).count(')')
                # for i in range(len(textMn)):
                #     if textMn[i] == '(':
                #         countOpenBrackets += 1
                #     elif textMn[i] == ')':
                #         countClosedBrackets += 1
                if self.labelMn.text() != '':
                    if self.labelMn.text()[-1] == '(':
                        self.labelMn.setText(textMn + '0' + ')')
                    elif countClosedBrackets < countOpenBrackets:
                        self.labelMn.setText(textMn + textMx + ')')
                        self.labelMx.setText('')
            # Смена функционала (работает) *************************************
            elif key == "↑":
                for r in range(cntRow):
                    for c in range(cntCol):
                        self.btn[r][c].setText(self.buttonListAdditional[r][c])
            elif key == "↓":
                for r in range(cntRow):
                    for c in range(cntCol):
                        self.btn[r][c].setText(self.buttonList[r][c])
        ########################################################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
