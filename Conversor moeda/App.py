from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from interface import *
from Coletor import *
import datetime


class Converter(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__(None)
        super().setupUi(self)

        # Fixar o Tamanho
        self.setFixedSize(313, 164)

        # Set
        self.atualizar.clicked.connect(self.atualiza)
        self.data.setText(str(datetime.datetime.now().date().today()))
        self.dinheiro_1.addItems(['Dollar', 'Euro', 'Iene', 'Real'])
        self.dinheiro_2.addItems(['Dollar', 'Euro', 'Iene', 'Real'])
        self.convert.clicked.connect(self.calcular_conversor)

        # Travar a saida do valor_2 para não editavel.
        self.valor_2.setDisabled(True)

        # Formatação CSS
        self.valor_2.setStyleSheet(
            '* {color:#000}'  # Formatação em CSS
        )

        self.convert.setStyleSheet(
            '* {background: #32CD32; color:#000}'  # Formatação em CSS
        )
        self.setStyleSheet(
            '* {background: #E0FFFF; color:#000; font-size: 20px,}'  # Formatação em CSS
        )

        self._coletaD = 5.26
        self._coletaR = 1
        self._coletaI = 0.046
        self._coletaE = 6.14

    def atualiza(self):
        self._coletaD = coletar_dollar()
        self._coletaR = coletar_real()
        self._coletaI = coletar_iene()
        self._coletaE = coletar_euro()

        # Teste
        # self._coletaD = 1
        # self._coletaR = 2
        # self._coletaI = 3
        # self._coletaE = 4

    def calcular_conversor(self):
        dinheiro_input = self.dinheiro_1.currentText()
        dinheiro_resultado = self.dinheiro_2.currentText()

        try:
            # Real
            if dinheiro_input == 'Dollar' and dinheiro_resultado == 'Real':
                calcular = (float(self.valor_1.text()) * self._coletaD)
                calcular = round(calcular, 2)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            elif dinheiro_input == 'Euro' and dinheiro_resultado == 'Real':
                calcular = (float(self.valor_1.text()) * self._coletaE)
                calcular = round(calcular, 2)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            elif dinheiro_input == 'Iene' and dinheiro_resultado == 'Real':
                calcular = (float(self.valor_1.text()) * self._coletaI)
                calcular = round(calcular, 2)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            elif dinheiro_input == 'Real' and dinheiro_resultado == 'Real':
                calcular = (float(self.valor_1.text()) * self._coletaR)
                calcular = round(calcular, 2)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            # Euro
            elif dinheiro_input == 'Real' and dinheiro_resultado == 'Euro':
                calcular = (float(self.valor_1.text()) / self._coletaE)
                calcular = round(calcular, 2)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            elif dinheiro_input == 'Dollar' and dinheiro_resultado == 'Euro':
                calcular = (float(self.valor_1.text()) / self._coletaE * self._coletaD)
                calcular = round(calcular, 2)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            elif dinheiro_input == 'Iene' and dinheiro_resultado == 'Euro':
                calcular = (float(self.valor_1.text()) / self._coletaE * self._coletaI)
                calcular = round(calcular, 4)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            elif dinheiro_input == 'Euro' and dinheiro_resultado == 'Euro':
                calcular = (float(self.valor_1.text()))
                calcular = round(calcular, 4)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            # Dollar
            elif dinheiro_input == 'Iene' and dinheiro_resultado == 'Dollar':
                calcular = (float(self.valor_1.text()) / self._coletaD * self._coletaI)
                calcular = round(calcular, 4)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            elif dinheiro_input == 'Real' and dinheiro_resultado == 'Dollar':
                calcular = (float(self.valor_1.text()) / self._coletaD * self._coletaR)
                calcular = round(calcular, 4)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            elif dinheiro_input == 'Euro' and dinheiro_resultado == 'Dollar':
                calcular = (float(self.valor_1.text()) / self._coletaD * self._coletaE)
                calcular = round(calcular, 4)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            elif dinheiro_input == 'Dollar' and dinheiro_resultado == 'Dollar':
                calcular = (float(self.valor_1.text()))
                calcular = round(calcular, 4)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            # Iene
            elif dinheiro_input == 'Iene' and dinheiro_resultado == 'Iene':
                calcular = (float(self.valor_1.text()))
                calcular = round(calcular, 4)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            elif dinheiro_input == 'Euro' and dinheiro_resultado == 'Iene':
                calcular = (float(self.valor_1.text()) / self._coletaI * self._coletaE)
                calcular = round(calcular, 4)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            elif dinheiro_input == 'Dollar' and dinheiro_resultado == 'Iene':
                calcular = (float(self.valor_1.text()) / self._coletaI * self._coletaD)
                calcular = round(calcular, 4)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))

            elif dinheiro_input == 'Real' and dinheiro_resultado == 'Iene':
                calcular = (float(self.valor_1.text()) / self._coletaI * self._coletaR)
                calcular = round(calcular, 4)
                self.valor_1.setText(str(self.valor_1.text()))
                self.valor_2.setText(str(calcular).replace('.', ','))
                
        except:
            self.valor_1.setText(str(1))
            pass


if __name__ == '__main__':
    aplicativo = QApplication(sys.argv)
    tela = Converter()
    tela.show()
    aplicativo.exec_()
