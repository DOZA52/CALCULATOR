from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QGroupBox
from PyQt5.QtCore import Qt


app = QApplication([])
window = QWidget()
window.setWindowTitle("Калькулятор")
window.resize(100,500)
window.setStyleSheet("""QWidget {
font-family: "Ticker Tape", Times, serif;
font-size: 25px;
background-color: rgb(51, 51, 51);
 color: white; 
 }
                    QPushButton {
    background-color: #4d4d4d;
    border: 3px solid white;
    padding:5px 25px 5px 25px;
    border-radius: 20px;
                    }
                    QPushButton:hover{
    background-color:#1a1a1a;

}
""")
btn_0 = QPushButton('0')
#btn_0.setStyleSheet ("background-color: ; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_1 = QPushButton('1')
#btn_1.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_2 = QPushButton('2')
#btn_2.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_3 = QPushButton('3')
#btn_3.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_4 = QPushButton('4')
#btn_4.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_5 = QPushButton('5')
#btn_5.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_6 = QPushButton('6')
#btn_6.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_7 = QPushButton('7')
#btn_7.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_8 = QPushButton('8')
#btn_8.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_9 = QPushButton('9')
#btn_9.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")


BTN_eq = QPushButton('=')
#BTN_eq.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_clear = QPushButton('c')
#btn_clear.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_back = QPushButton('<-')
#btn_back.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_point = QPushButton('.')
#btn_point.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")

btn_pl = QPushButton("+")
#btn_pl.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_min = QPushButton("-")
#btn_min.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_mul = QPushButton("*")
#btn_mul.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")
btn_div = QPushButton("/")
#btn_div.setStyleSheet ("background-color: grey; border: 3px solid white; padding:5px 25px 5px 25px; border-radius: 20px;")

result = QLabel("0")
line1=QHBoxLayout()
line1.addWidget(BTN_eq,alignment=Qt.AlignCenter)
line1.addWidget(btn_min,alignment=Qt.AlignCenter)
line1.addWidget(btn_back,alignment=Qt.AlignCenter)
line1.addWidget(btn_div,alignment=Qt.AlignCenter)
line1.addWidget(btn_clear,alignment=Qt.AlignCenter)


line3=QHBoxLayout()
line3.addWidget(btn_1,alignment=Qt.AlignCenter)
line3.addWidget(btn_2,alignment=Qt.AlignCenter)
line3.addWidget(btn_3,alignment=Qt.AlignCenter)


line4=QHBoxLayout()
line4.addWidget(btn_4,alignment=Qt.AlignCenter)
line4.addWidget(btn_5,alignment=Qt.AlignCenter)
line4.addWidget(btn_6,alignment=Qt.AlignCenter)


line5=QHBoxLayout()
line5.addWidget(btn_7,alignment=Qt.AlignCenter)
line5.addWidget(btn_8,alignment=Qt.AlignCenter)
line5.addWidget(btn_9,alignment=Qt.AlignCenter)


line7=QHBoxLayout()
line7.addWidget(btn_mul,alignment=Qt.AlignCenter)
line7.addWidget(btn_0,alignment=Qt.AlignCenter)
line7.addWidget(btn_pl,alignment=Qt.AlignCenter)

box1=QGroupBox("РЕЗУЛЬТАТ")
box_line = QHBoxLayout()
box_line.addWidget(result,alignment=Qt.AlignRight)
box1.setLayout(box_line)

main_line = QVBoxLayout()
main_line.addWidget(box1)
main_line.addLayout(line1)
main_line.addLayout(line3)
main_line.addLayout(line4)
main_line.addLayout(line5)
main_line.addLayout(line7)

def add_symbol():
    button = app.sender()
    text= result.text()
    if text[len(text)-1] in "+-/*" and button.text() in "+-/*":
        return
    if text == "0" : 
        text=""
    result.setText(text+button.text())
btn_0.clicked.connect(add_symbol)
btn_1.clicked.connect(add_symbol)
btn_2.clicked.connect(add_symbol)
btn_3.clicked.connect(add_symbol)
btn_4.clicked.connect(add_symbol)
btn_5.clicked.connect(add_symbol)
btn_6.clicked.connect(add_symbol)
btn_7.clicked.connect(add_symbol)
btn_8.clicked.connect(add_symbol)
btn_9.clicked.connect(add_symbol)
btn_back.clicked.connect(add_symbol)
BTN_eq.clicked.connect(add_symbol)
btn_clear.clicked.connect(add_symbol)
btn_point.clicked.connect(add_symbol)
btn_min.clicked.connect(add_symbol)
btn_mul.clicked.connect(add_symbol)
btn_pl.clicked.connect(add_symbol)
btn_div.clicked.connect(add_symbol)


def clear():
    result.setText("0")
btn_clear.clicked.connect(clear)

def back():
    text = result.text()
    text = text[:-1]
    if text == "":
         text="0"
    result.setText(text)
btn_back.clicked.connect(back)
def parseSting(string):
    operatoins -"+-/*"
    element -""
    result =[]
    for symbol in string:
        if it operatoins.find(symbol) !=-1:
            result.append(element)
            result.append(symbol)
            element-""
        else:
            element+=symbol
    result.append(element)
    return result


def calculate(string):
    formula - parseSting(string):
    if formula[0] -- "":
        formula[0] ="0"
    operatoins -["+-/*"]
    for cur_operation in operations:
        i -0
        while i< len(formula)
            if cur_operation.find(formula[i]) !=-1
            operation = formula[i]
            first_number = float(formula[i-1])
            second_number = float(formula[i+1])
            if operation =="+":
                result = first_number+second_number
            if operation =="-":
                result = first_number+second_number
            if operation =="*":
                result = first_number+second_number
            if operation =="/":
                result = first_number+second_number
            del formula [i+1]
            formula[i]= str(result)
            del formula[i-1]
            i=0
        i+=1
    return formula[0]


def equal():
    formula = result.text()
    number = calculate(formula)
    result.setText(str(number))
    BTN_eq.clicked.connect(equal)
window.setLayout(main_line)
window.show()
app.exec_()