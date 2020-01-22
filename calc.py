"""
Приложение "Калькулятор"

Автор: Ощепков Евгений
"""
import sys

from PyQt5.QtWidgets import QApplication,QLabel,QWidget, QPushButton,QMessageBox
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont

# ---------------------------------Константы -----------------------------------
eNumber = 2,71828182845 #....................................................... Число Эйлера
pNumber = 3,14159265358 #....................................................... Число Пи
size = 80 #..................................................................... Масштаб
board = 20 #..................................................................... Ширина отступа
hr = 8*size #................................................................... Высота окна
wr = 8*size #................................................................... Ширина окна

cntRow = 5 #.................................................................... Количество строк.......#Размерность списков
cntCol = 5 #.................................................................... Количество столбцов....#

hlhis = hr  - 2*board #.......................................................... Высота окна истории
wlhis = (wr - 2*board) * 3/8 #................................................... Ширина окна истории

hlmn = (hr-3*board)//8 #......................................................... Высота маленького Label
wlmn = wr - wlhis -  3*board #................................................... Ширина маленького Label

hlmx = 2*(hr-2*board)//8 #....................................................... Высота большого Label
wlmx = wr - wlhis -  3*board #................................................... Ширина большого Label

hl = hlmx + hlmn #.............................................................. Высота обоих Label



hb = (hr - hl - 2*board)//cntRow #............................................... Высота кнопок
wb = (wr - wlhis - 3*board)//cntCol #............................................ Ширина кнопок
# ------------------------------------------------------------------------------


def factor(x): # Факториал (х!)
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

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.resize(QSize(wr, hr)) #............................................ Размер окна
        self.setWindowTitle('Калькулятор') #.................................... Заголовок

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
                background-color: #222;
                color: #C0C0C0	;
            }
            #labelMn {
                background-color: #333;
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
            if key == '.':                                                      ##исключение добавить
                if key not in self.labelMn.text():
                    self.labelMx.setText(self.labelMx.text() + key)
            elif key in '1234567890':
                self.labelMx.setText(self.labelMx.text() + key)
        # Основной функционал (работает) ***************************************
        elif key in '+-×/':
            if '=' in textMn:
                self.labelMn.setText(textMx)
                self.labelMx.clear()
            if (textMx != '') or (textMn == ''):
                if '=' not in textMn:
                    if '-' not in textMx:
                        self.labelMn.setText(textMn + textMx + key)
                    else:
                        self.labelMn.setText(textMn + '(' + textMx + ')' + key)
                else:
                    self.labelMn.setText(textMx + key)
                self.labelMx.clear()
        # Счёт (работает) ******************************************************
        elif key == '=':
            if self.labelMx.text() != '' and '=' not in textMn:
                score = textMn + textMx
                score = '*'.join(score.split('×'))
                score = '**'.join(score.split('^'))
                result = eval(score)
                if '-' not in textMx:
                    self.labelMn.setText(textMn + textMx + key) #
#
                else: #
                    self.labelMn.setText(textMn + '(' + textMx + ')' + key) #
                self.labelMx.setText(str(result)) #
                self.labelHis.setText(self.labelHis.text() + self.labelMn.text() + self.labelMx.text() + "\n")
        # Очистка окна (работает) **********************************************
        elif key == 'C':
            self.labelMn.clear()
            self.labelMx.clear()
        # Удаление символа (работает) ******************************************
        elif key == '<':
            self.labelMx.setText(textMx[:-1])
        # Смена знака (работает) ***********************************************
        elif key == '±':
            if '-' not in textMx:
                self.labelMx.setText('-' + textMx)
            else:
                self.labelMx.setText(textMx[1:])
        # Возведение в квадрат (работает) **************************************
        elif key == 'x²':
            self.labelMx.setText(str(eval('(' + textMx +')**2')))
        # Возведение в степень (работает) **************************************
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
        # ОСтаток от деления (Mod) (Работает)***********************************
        elif key == "Mod":
            self.labelMn.setText(textMn + textMx + "%")
            self.labelMx.clear()
        # 10^x (Работает) ******************************************************
        elif key == "10ˣ" and textMx != "":
            self.labelMx.setText(str(10**float(textMx)))
        # Факториал х (x!)  (Работает) *****************************************
        elif key == "x!":
            if (textMx != "") and ("." not in textMx) and ("-" not in textMx):
                try:
                    self.labelMx.setText(str(factor(int(textMx))))
                except Exception as e:
                    raise

        # Дополнительный функционал ********************************************
        elif key == "^":
            key
        ########################################################################

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
