import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cx_Oracle
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

def guardar_datos(val0,val1):
    try:
        # Realizar la conexion.
        conexion = cx_Oracle.connect('HR/hr@127.0.0.1:1521/xepdb1')
        cursor= conexion.cursor()
        # Pasar valores y definir la sentencia SQL.
        valores = {"CAMPO":val0, "VALOR":val1}
        statement="INSERT INTO GRAFICOS(CAMPO, VALOR) VALUES (:1, :2)"
        cursor.execute(statement,(val0, val1))
        conexion.commit()
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        conexion.close()

class Ui_Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("PIA.ui",self)
        self.Boton_Guardar.clicked.connect(self.Grabar)
        self.Boton_Grafico.clicked.connect(self.Graficar)
        self.Boton_Limpiar.clicked.connect(self.limpiar)

    def Grabar(self):
        i0= str(self.txCam1.toPlainText())
        i1= int(self.txVal1.toPlainText())
        guardar_datos(i0,i1)
        i2= str(self.txCam2.toPlainText())
        i3= int(self.txVal2.toPlainText())
        guardar_datos(i2,i3)
        i4= str(self.txCam3.toPlainText())
        i5= int(self.txVal3.toPlainText())
        guardar_datos(i4,i5)
        i6= str(self.txCam4.toPlainText())
        i7= int(self.txVal4.toPlainText())
        guardar_datos(i6,i7)
        i8= str(self.txCam5.toPlainText())
        i9= int(self.txVal5.toPlainText())
        guardar_datos(i8,i9)
        i10= str(self.txCam6.toPlainText())
        i11= int(self.txVal6.toPlainText())
        guardar_datos(i10,i11)
        self.labelComentario.setText("Se han guardado los datos en una Base de Datos")

    def Graficar(self):
        i0= str(self.txCam1.toPlainText())
        i1= int(self.txVal1.toPlainText())
        i2= str(self.txCam2.toPlainText())
        i3= int(self.txVal2.toPlainText())
        i4= str(self.txCam3.toPlainText())
        i5= int(self.txVal3.toPlainText())
        i6= str(self.txCam4.toPlainText())
        i7= int(self.txVal4.toPlainText())
        i8= str(self.txCam5.toPlainText())
        i9= int(self.txVal5.toPlainText())
        i10= str(self.txCam6.toPlainText())
        i11= int(self.txVal6.toPlainText())
        item1= str(self.txtGraf.toPlainText())
        item2= str(self.textX.toPlainText())
        item3= str(self.textY.toPlainText())
        Campos=[i0,i2,i4,i6,i8,i10]
        Valores=[i1,i3,i5,i7,i9,i11]
        datos={"Campos":Campos, "Valores": Valores}
        df=pd.DataFrame(datos)
        if self.cbMat.isChecked():
            if self.radioBarras.isChecked():
                df.groupby('Campos')['Valores'].sum().plot(kind='bar', legend='Reverse', color="purple")
                plt.xlabel(item2)
                plt.ylabel(item3)
                plt.title(item1)
                self.labelComentario.setText(f"Seleccionaste la Grafica de Barras con Matplotlib\nEn donde se compara {item2} con {item3}.")
                plt.show()
            elif self.radioLineas.isChecked():
                df.groupby('Campos')['Valores'].sum().plot(kind='line', legend='Reverse', color="green")
                plt.xlabel(item2)
                plt.ylabel(item3)
                plt.title(item1)
                self.labelComentario.setText(f"Seleccionaste la Grafica de Lineas con Matplotlib\nEn donde se compara {item2} con {item3}.")
                plt.show()
            elif self.radioPastel.isChecked():
                df.groupby('Campos')['Valores'].sum().plot(kind='pie',autopct="%0.1f %%")
                plt.xlabel("")
                plt.ylabel("")
                plt.title(item1)
                self.labelComentario.setText(f"Seleccionaste la Grafica de Pastel\nEn donde se compara {item2} con {item3}.")
                plt.show()
            else:
                print("Seleccione un tipo de grafico.")
        if self.cbSea.isChecked():
            if self.radioBarras.isChecked():
                sns.barplot(x="Campos",y="Valores",data=datos)
                plt.xlabel(item2)
                plt.ylabel(item3)
                plt.title(item1)
                self.labelComentario.setText(f"Seleccionaste la Grafica de Barras con Seaborn\nEn donde se compara {item2} con {item3}.")
                plt.show()
            elif self.radioLineas.isChecked():
                sns.relplot(x="Campos",y="Valores",data=datos,kind="line",color="#00da9d")
                plt.xlabel(item2)
                plt.ylabel(item3)
                plt.title(item1)
                self.labelComentario.setText(f"Seleccionaste la Grafica de Lineas con Seaborn\nEn donde se compara {item2} con {item3}.")
                plt.show()
            elif self.radioPastel.isChecked():
                df.groupby('Campos')['Valores'].sum().plot(kind='pie',cmap="Spectral",autopct="%0.1f %%")
                plt.xlabel("")
                plt.ylabel("")
                plt.title(item1)
                self.labelComentario.setText(f"Seleccionaste la Grafica de Pastel\nEn donde se compara {item2} con {item3}.")
                plt.show()
            else:
                print("Selecciona un tipo de grafico.")

    def limpiar(self):
        for line in [self.txtGraf,self.textX,self.textY,self.txCam1,self.txCam2,self.txCam3,self.txCam4,self.txCam5,self.txVal1,self.txVal2,self.txVal3,self.txVal4,self.txVal5]: line.clear()
        for box in [self.cbMat,self.cbSea]:box.setChecked(False)
        self.labelComentario.clear()
        for buttn in [self.radioBarras, self.radioLineas, self.radioPastel]:
            buttn.setAutoExclusive(False)
            buttn.setChecked(False)
            buttn.repaint()
            buttn.setAutoExclusive(True)

app=QApplication(sys.argv)
dialogo = Ui_Dialog()
dialogo.show()
app.exec_()