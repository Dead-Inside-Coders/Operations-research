from PyQt5 import uic, QtCore, QtGui, QtWidgets, Qt
import sys


Form, _ = uic.loadUiType("Calculator.ui")


class Ui(QtWidgets.QMainWindow, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.Calc.clicked.connect(self.Calcul)
        self.SaveF.clicked.connect(self.SvFile)

    def SvFile(self):
        f = open("calculator's answer.txt", "w")
        f.write(str(self.Result.toPlainText()))
        f.close()

    def Calcul(self):
        try:
            res = 0.0
            num1 = float(self.InputA.toPlainText())
            num2 = float(self.InputB.toPlainText())
            op = str(self.Operation.toPlainText())
            if op == "+":
                res = num1 + num2
                self.Result.setPlainText(str(res))
            elif op == "-":
                res = num1 - num2
                self.Result.setPlainText(str(res))
            elif op == "*":
                res = num1 * num2
                self.Result.setPlainText(str(res))
            elif op == "pow" or op == "**":
                res = num1 ** num2
                self.Result.setPlainText(str(res))
            elif op == "/":
                res = num1 / num2
                self.Result.setPlainText(str(res))
            elif op == "mod" or op == "%":
                res = num1 % num2
                self.Result.setPlainText(str(res))
            elif op == "div" or op == "//":
                res = num1 // num2
                self.Result.setPlainText(str(res))
            else:
                self.Result.setPlainText(str("Операция не поддерживается в калькуляторе"))
        except ZeroDivisionError:
            self.Result.setPlainText(str("Деление на ноль!"))
        except:
            self.Result.setPlainText(str("Ошибка !"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec_())
