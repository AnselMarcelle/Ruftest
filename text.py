from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.show()

main_win.setWindowTitle('Hello, world!')
main_win.resize(500,500)
text = QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.')
text2 = QLabel('Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                   'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                   'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                   'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                   'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                   'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                   'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.')
button = QPushButton('Начать')
v_line = QVBoxLayout()
v_line.addWidget(text, alignment = Qt.AlignLeft)
v_line.addWidget(text2, alignment = Qt.AlignLeft)
v_line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(v_line)
app.exec_()

