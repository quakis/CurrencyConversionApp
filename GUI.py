from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import currencies
import conversions

class window(QMainWindow):
	def __init__(this):
		super(QMainWindow, this).__init__()
		this.setGeometry(200, 200, 300, 240)
		this.setWindowTitle("Quick Converter")
		this.initUI()

	def initUI(this):
		this.title = QtWidgets.QLabel(this)
		this.title.setText("Quick Converter")
		this.title.move(80, 20)
		this.title.setFont(QtGui.QFont('Arial', 20))
		this.title.adjustSize()

		this.pointer = QtWidgets.QLabel(this)
		this.pointer.setText("-->")
		this.pointer.move(140,117.5)

		this.output = QtWidgets.QLabel(this)
		this.output.setText("")
		this.output.move(70,205)

		this.amount = QtWidgets.QLineEdit(this)
		this.amount.move(100,70)

		this.leftCombo = QtWidgets.QComboBox(this)
		this.leftCombo.move(40,120)

		this.rightCombo = QtWidgets.QComboBox(this)
		this.rightCombo.move(160,120)

		currencyList = []
		for i in currencies.getCurrencies():
			currencyList.append(i)
		for i in currencies.getCryptocurrencies():
			currencyList.append(i)
		for i in sorted(currencyList):
			this.leftCombo.addItem(i)
			this.rightCombo.addItem(i)

		this.convertBtn = QtWidgets.QPushButton(this)
		this.convertBtn.setText("Convert")
		this.convertBtn.clicked.connect(this.test)
		this.convertBtn.move(102.5, 162.5)

	def test(this):
		current = str(this.leftCombo.currentText()).upper().strip()
		amount = float(str(this.amount.text()).strip().replace("$", "").replace(",", ""))
		target = str(this.rightCombo.currentText()).upper().strip()
		data = conversions.convert(current, target, amount)
		this.output.setText(str(data) + " " + str(target))
		this.update()

	def update(this):
		this.output.adjustSize()
		this.output.setAlignment(QtCore.Qt.AlignCenter)


def mainWindow():
	app = QApplication(sys.argv)
	win = window()


	win.show()
	sys.exit(app.exec_())

mainWindow()

