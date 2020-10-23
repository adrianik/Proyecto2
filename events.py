import var

class Eventos():

    def Saludo():
        try:
            var.ui.IblHola.setText('Has pulsado el Botón')
        except Exception as error:
            print('Error: %s ' % str(error))

    def Salir(self):
        try:
            sys.exit()
            except
