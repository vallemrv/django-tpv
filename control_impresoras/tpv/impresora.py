# -*- coding: utf-8 -*-
# @Author: Manuel Rodriguez <valle>
# @Date:   10-May-2017
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 12-Jul-2018
# @License: Apache license vesion 2.0

from __future__ import unicode_literals
from datetime import datetime

from escpos.printer import Network
from escpos.escpos import EscposIO
from escpos import escpos
import locale

import sys

locale.setlocale(locale.LC_TIME, "es_ES.UTF-8")

ip_caja = '192.168.1.8'

class DocPrint():

    def __init__(self, ip_caja):
        self.ip_caja = ip_caja

    def abrir_cajon(self,  *args):
        try:
            printer = Network(self.ip_caja, timeout=1)
            printer.cashdraw(2)
        except Exception as e:
            print("[ERROR  ] %s" % e)

    def printDesglose(self, fecha, lineas):

        if type(fecha) is datetime:
            fecha = fecha.strftime("%d/%m/%Y %H:%M:%S")
        else:
            fecha = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S.%f")
            fecha = fecha.strftime("%d/%m/%Y %H:%M:%S")


        try:
            printer = Network(self.ip_caja, timeout=1)


            with EscposIO(printer) as p:
                p.printer.codepage = 'cp858'
                p.writelines("Cierre de caja", align='center', width=2, height=2)

                p.writelines(fecha, align='center', width=2, height=2)
                p.writelines("------------------------------------------",
                              align='center')
                p.writelines("")
                for linea in lineas:
                    can = linea["can"]
                    texto_tipo = linea["texto_tipo"]
                    tipo = linea["tipo"]
                    p.writelines("Retirar {0: >5} {1} de {2}".format(can, texto_tipo,
                                                                     tipo),height=2,align='center')

                p.writelines("")
                p.writelines("")
        except Exception as e:
            print("[ERROR  ] %s" % e)

    def imprimirTicket(self, num, camarero,  fecha, mesa, total, efectivo, cambio, lineas):

        if type(fecha) is datetime:
            fecha = fecha.strftime("El %a %d-%B a las (%H:%M)")
        else:
            fecha = datetime.strptime(fecha, "%Y/%m/%d %H:%M")
            fecha = fecha.strftime("El %a %d-%B a las (%H:%M)")

        try:

            printer = Network(self.ip_caja, timeout=1)


            with EscposIO(printer) as p:
                p.printer.codepage = 'cp858'
                p.printer._raw(escpos.CHARCODE_PC852)
                p.printer.image("logo.png")
                p.writelines('')
                p.writelines('Calle San Pablo, 10', font='a', align='center')
                p.writelines('18013 Granada', font='a', align='center')
                p.writelines('NIF: 74680606C', font='b', align='center')
                p.writelines('')
                p.writelines('------------------------------------------', align='center')
                p.writelines('FECHA', height=2, width=2, font='a', align='center')
                p.writelines(fecha, height=2, width=1, font='b', align='center')
                p.writelines("Num Ticket: %d" % num,font='a', align='center')
                p.writelines("Camarero: %s" % camarero,  font='a', align='center')
                p.writelines("Mesa: %s" % mesa,  font='a', align='center')
                p.writelines('------------------------------------------', align='center')


                for ln in lineas:
                    p.writelines("{0: >3} {1: <20} {2:5.2f} € {3:6.2f} €".format(ln['can'], ln['nombre'],
                                  float(ln['precio']), float(ln['totallinea'])), align='center', font="a")


                p.writelines("")
                p.writelines("Total: {0:0.2f} €".format(float(total)),
                              align='right', height=2)
                p.writelines("Efectivo: {0:0.2f} €".format(float(efectivo)),
                              align='right')
                p.writelines("Cambio: {0:0.2f} €".format(float(cambio)),
                              align='right', )


                p.writelines("")
                p.writelines("Factura simplificada",  text_type='bold', height=2, align='center')
                p.writelines("Iva incluido",  text_type='bold', height=2, align='center')
                p.writelines("")
                p.writelines("Gracias por su visita",  height=2, align='center')
                p.writelines("")
                p.writelines("")
        except Exception as e:
            print("[ERROR  ] %s" % e)

    def imprimirPedido(self, camarero, mesa, hora, lineas):

        try:
            printer = Network(self.ip_caja, timeout=1)

            with EscposIO(printer) as p:
                p.printer.set(align='center')
                p.writelines("")
                p.writelines('------------------------------------------', align='center')
                p.writelines('HORA: %s' % hora, height=2, width=2, font='b', align='center')
                p.writelines("Mesa: %s" % mesa, height=2, width=2, font='a', align='center')
                p.writelines(camarero, height=2, width=2, font='a', align='center')
                p.writelines('------------------------------------------', align='center')

                p.writelines("")
                for ln in lineas:
                    p.writelines("{0: >3} {1: <25} {2:0.2f}".format(ln['can'], ln['nombre'],
                                  float(ln["precio"])), height=2, align='center' )


                p.writelines("")
                p.writelines("")
        except Exception as e:
            print("[ERROR  ] %s" % e)

    def imprimirUrgente(self, camarero, mesa, hora, lineas):
        try:
            printer = Network(self.ip_caja, timeout=1)

            with EscposIO(printer) as p:
                p.printer.codepage = 'cp858'
                p.printer.set(align='center')
                p.writelines("")
                p.writelines('URGENTE!!', height=2, width=2, font='a', align='center')
                p.writelines('------------------------------------------', align='center')
                p.writelines('HORA: %s' % hora, height=2, width=2, font='b', align='center')
                p.writelines("Mesa: %s" % mesa, height=2, width=2, font='a', align='center')
                p.writelines(camarero, height=2, width=2, font='a', align='center')
                p.writelines('------------------------------------------', align='center')

                p.writelines("")
                for ln in lineas:
                    p.writelines("{0: >3} {1: <25} {2:0.2f}".format(ln['can'], ln['nombre'],
                                  float(ln["precio"])), height=2, align='center' )


                p.writelines("")
                p.writelines("")
        except Exception as e:
            print("[ERROR  ] %s" % e)

    def imprimirPreTicket(self, camarero, numcopias, fecha, mesa, lineas, total):

        if type(fecha) is datetime:
            fecha = fecha.strftime("El %a %d-%B a las (%H:%M)")
        else:
            fecha = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S.%f")
            fecha = fecha.strftime("El %a %d-%B a las (%H:%M)")

        try:
            printer = Network(self.ip_caja, timeout=1)
            with EscposIO(printer) as p:
                p.printer.codepage = 'cp858'
                p.printer.set(align='center')
                p.printer._raw(escpos.CHARCODE_PC852)
                p.writelines('PRETICKET', font='a', height=2, align='center')
                p.writelines('')
                p.writelines('------------------------------------------', align='center')
                p.writelines('FECHA', height=2, width=2, font='a', align='center')
                p.writelines(fecha, height=2, width=1, font='b', align='center')
                p.writelines("Num copias: %d" % numcopias, font='a', align='center')
                p.writelines("Mesa: %s" % mesa,  font='a', align='center')
                p.writelines('------------------------------------------', align='center')

                for ln in lineas:
                    p.writelines("{0: >3} {1: <20} {2:5.2f} € {3:6.2f} €".format(ln['can'], ln['nombre'],
                                  float(ln['precio']), float(ln['totallinea'])), align='center', font="a")

                p.writelines("")
                p.writelines("Total: {0:0.2f} €".format(float(total)),
                              align='right', height=2)
                p.writelines("")
                p.writelines("No olvide pedir su ticket",  text_type='bold', height=2, align='center')
                p.writelines(camarero, text_type='bold', font='a', align='center')

                p.writelines("")
                p.writelines("")
        except Exception as e:
            print("[ERROR  ] %s" % e)

    def test_print(self):
        print("Test print console")

if __name__ == '__main__':
    import sys
    import os
    import locale
    locale.setlocale(locale.LC_TIME, "es_ES.UTF-8") # swedish

    with EscposIO(Network('192.168.1.8', port=9100)) as p:
        p.printer.codepage = 'cp858'
        p.printer._raw(escpos.CHARCODE_PC852)
        p.writelines("ñññññ€", height=2, width=2)
