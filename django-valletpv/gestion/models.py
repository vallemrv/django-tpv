# @Author: Manuel Rodriguez <valle>
# @Date:   01-Jan-2018
# @Email:  valle.mrv@gmail.com
# @Last modified by:   valle
# @Last modified time: 04-Jul-2018
# @License: Apache license vesion 2.0


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Arqueocaja(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cierre = models.ForeignKey('Cierrecaja', on_delete=models.CASCADE, db_column='IDCierre')  # Field name made lowercase.
    cambio = models.FloatField(db_column='Cambio')  # Field name made lowercase.
    descuadre = models.FloatField(db_column='Descuadre')  # Field name made lowercase.

    class Meta:
        db_table = 'arqueocaja'


class Camareros(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    apellidos = models.CharField(db_column='Apellidos', max_length=100)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50)  # Field name made lowercase.
    pass_field = models.CharField(db_column='Pass', max_length=100)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    activo = models.IntegerField(db_column='Activo')  # Field name made lowercase.

    class Meta:
        db_table = 'camareros'


class Cierrecaja(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ticketcom = models.IntegerField(db_column='TicketCom')  # Field name made lowercase.
    ticketfinal = models.IntegerField(db_column='TicketFinal')  # Field name made lowercase.
    fecha = models.CharField(db_column='Fecha', max_length=10)  # Field name made lowercase.
    hora = models.CharField(db_column='Hora', max_length=5)  # Field name made lowercase.

    class Meta:
        db_table = 'cierrecaja'


class Colores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=20)  # Field name made lowercase.
    rgb = models.CharField(db_column='RGB', max_length=11)  # Field name made lowercase.

    class Meta:
        db_table = 'colores'


class Efectivo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    arqueo = models.ForeignKey(Arqueocaja,  on_delete=models.CASCADE, db_column='IDArqueo')  # Field name made lowercase.
    can = models.IntegerField(db_column='Can')  # Field name made lowercase.
    moneda = models.DecimalField(db_column='Moneda', max_digits=5, decimal_places=2)  # Field name made lowercase.

    class Meta:
        db_table = 'efectivo'


class Familias(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=40)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=6)  # Field name made lowercase.
    numtapas = models.IntegerField(db_column='NumTapas')  # Field name made lowercase.
    receptor = models.ForeignKey('Receptores',  on_delete=models.CASCADE, db_column='IDReceptor')  # Field name made lowercase.

    class Meta:
        db_table = 'familias'


class Gastos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    arqueo = models.ForeignKey(Arqueocaja,  on_delete=models.CASCADE, db_column='IDArqueo')  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50)  # Field name made lowercase.
    importe = models.DecimalField(db_column='Importe', max_digits=6, decimal_places=2)  # Field name made lowercase.

    class Meta:
        db_table = 'gastos'


class Historialnulos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    lineapedido = models.ForeignKey('Lineaspedido',  on_delete=models.CASCADE, db_column='IDLPedido')  # Field name made lowercase.
    camarero = models.ForeignKey(Camareros,  on_delete=models.CASCADE, db_column='IDCam')  # Field name made lowercase.
    hora = models.CharField(db_column='Hora', max_length=5)  # Field name made lowercase.
    motivo = models.CharField(db_column='Motivo', max_length=100)  # Field name made lowercase.

    class Meta:
        db_table = 'historialnulos'


class HorarioUsr(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora_ini = models.CharField(db_column='Hora_ini', max_length=5)  # Field name made lowercase.
    hora_fin = models.CharField(db_column='Hora_fin', max_length=5)  # Field name made lowercase.
    usurario = models.ForeignKey('Usuarios',  on_delete=models.CASCADE, db_column='IDUsr')  # Field name made lowercase.

    class Meta:
        db_table = 'horario_usr'


class Infmesa(models.Model):
    uid = models.CharField(db_column='UID', primary_key=True, unique=True, max_length=100)  # Field name made lowercase.
    camarero = models.ForeignKey(Camareros,  on_delete=models.CASCADE, db_column='IDCam')  # Field name made lowercase.
    fecha = models.CharField(db_column='Fecha', max_length=10)  # Field name made lowercase.
    hora = models.CharField(db_column='Hora', max_length=5)  # Field name made lowercase.
    ref = models.CharField(db_column='Ref', max_length=50)  # Field name made lowercase.
    numcopias = models.IntegerField(db_column='NumCopias')  # Field name made lowercase.

    class Meta:
        db_table = 'infmesa'


class Lineaspedido(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    pedido = models.ForeignKey('Pedidos',  on_delete=models.CASCADE, db_column='IDPedido')  # Field name made lowercase.
    infmesa = models.ForeignKey(Infmesa, on_delete=models.CASCADE, db_column='UID')  # Field name made lowercase.
    idart = models.IntegerField(db_column='IDArt')  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=1)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=6, decimal_places=2)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=70)  # Field name made lowercase.

    class Meta:
        db_table = 'lineaspedido'


class Mesas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=50)  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden')  # Field name made lowercase.

    class Meta:
        db_table = 'mesas'


class Mesasabiertas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    infmesa = models.ForeignKey(Infmesa, on_delete=models.CASCADE, db_column='UID')  # Field name made lowercase.
    mesa = models.ForeignKey(Mesas, on_delete=models.CASCADE, db_column='IDMesa')  # Field name made lowercase.

    class Meta:
        db_table = 'mesasabiertas'


class Mesaszona(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    zona = models.ForeignKey('Zonas',  on_delete=models.CASCADE, db_column='IDZona')  # Field name made lowercase.
    mesa = models.ForeignKey(Mesas,  on_delete=models.CASCADE, db_column='IDMesa')  # Field name made lowercase.

    class Meta:
        db_table = 'mesaszona'


class Movimientos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idsub = models.IntegerField(db_column='IDSub')  # Field name made lowercase.
    fecha = models.CharField(db_column='Fecha', max_length=10)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    isub_pago = models.IntegerField(db_column='IDSub_pago')  # Field name made lowercase.

    class Meta:
        db_table = 'movimientos'


class Pedidos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hora = models.CharField(db_column='Hora', max_length=5)  # Field name made lowercase.
    infmesa = models.ForeignKey(Infmesa,  on_delete=models.CASCADE, db_column='UID')  # Field name made lowercase.
    camarero_id = models.IntegerField(db_column='IDCam')  # Field name made lowercase.

    class Meta:
        db_table = 'pedidos'


class Receptores(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=40)  # Field name made lowercase.
    nomimp = models.CharField(db_column='nomImp', max_length=40)  # Field name made lowercase.

    class Meta:
        db_table = 'receptores'


class Secciones(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=20)  # Field name made lowercase.
    rgb = models.CharField(db_column='RGB', max_length=11)  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden')  # Field name made lowercase.

    class Meta:
        db_table = 'secciones'


class SeccionesCom(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=11)  # Field name made lowercase.

    class Meta:
        db_table = 'secciones_com'


class Servidos(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    linea = models.ForeignKey(Lineaspedido,  on_delete=models.CASCADE, db_column='IDLinea')  # Field name made lowercase.

    class Meta:
        db_table = 'servidos'


class Subcuentas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    apodo = models.CharField(db_column='Apodo', max_length=100)  # Field name made lowercase.
    idcuenta = models.IntegerField(db_column='IDCuenta')  # Field name made lowercase.
    notas = models.TextField(db_column='Notas')  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=5)  # Field name made lowercase.

    class Meta:
        db_table = 'subcuentas'


class Subteclas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    tecla_id = models.IntegerField(db_column='IDTecla')  # Field name made lowercase.
    incremento = models.DecimalField(db_column='Incremento', max_digits=6, decimal_places=2)  # Field name made lowercase.

    class Meta:
        db_table = 'subteclas'


class Sugerencias(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tecla_id = models.IntegerField(db_column='IDTecla')  # Field name made lowercase.
    sugerencia = models.CharField(db_column='Sugerencia', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'sugerencias'


class Sync(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    modificado = models.CharField(db_column='Modificado', max_length=25)  # Field name made lowercase.
    tabla = models.CharField(db_column='Tabla', max_length=50)  # Field name made lowercase.
    args = models.CharField(max_length=50)

    class Meta:
        db_table = 'sync'


class Teclas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    p1 = models.DecimalField(db_column='P1', max_digits=6, decimal_places=2)  # Field name made lowercase.
    p2 = models.DecimalField(db_column='P2', max_digits=6, decimal_places=2)  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden')  # Field name made lowercase.
    familia = models.ForeignKey(Familias,  on_delete=models.CASCADE, db_column='IDFamilia')  # Field name made lowercase.
    tag = models.CharField(db_column='Tag', max_length=100)  # Field name made lowercase.
    ttf = models.CharField(db_column='TTF', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'teclas'


class Teclascom(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tecla = models.ForeignKey(Teclas,  on_delete=models.CASCADE, db_column='IDTecla')  # Field name made lowercase.
    seccion = models.ForeignKey(SeccionesCom,  on_delete=models.CASCADE, db_column='IDSeccion')  # Field name made lowercase.
    orden = models.IntegerField(db_column='Orden')  # Field name made lowercase.

    class Meta:
        db_table = 'teclascom'


class Teclaseccion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    seccion = models.ForeignKey(Secciones,  on_delete=models.CASCADE, db_column='IDSeccion')  # Field name made lowercase.
    tecla = models.ForeignKey(Teclas,  on_delete=models.CASCADE, db_column='IDTecla')  # Field name made lowercase.

    class Meta:
        db_table = 'teclaseccion'


class Ticket(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    fecha = models.CharField(db_column='Fecha', max_length=10)  # Field name made lowercase.
    camarero_id = models.IntegerField(db_column='IDCam')  # Field name made lowercase.
    hora = models.CharField(db_column='Hora', max_length=5)  # Field name made lowercase.
    entrega = models.DecimalField(db_column='Entrega', max_digits=6, decimal_places=2)  # Field name made lowercase.
    uid = models.CharField(db_column='UID', max_length=100)  # Field name made lowercase.
    mesa = models.CharField(db_column='Mesa', max_length=40)  # Field name made lowercase.

    class Meta:
        db_table = 'ticket'


class Ticketlineas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ticket = models.ForeignKey(Ticket,  on_delete=models.CASCADE, db_column='IDTicket')  # Field name made lowercase.
    linea = models.ForeignKey(Lineaspedido,  on_delete=models.CASCADE, db_column='IDLinea')  # Field name made lowercase.

    class Meta:
        db_table = 'ticketlineas'


class Usuarios(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=50)  # Field name made lowercase.
    email = models.CharField(max_length=100)
    pass_field = models.CharField(db_column='Pass', max_length=11)  # Field name made lowercase. Field renamed because it was a Python reserved word.

    class Meta:
        db_table = 'usuarios'


class Zonas(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=50)  # Field name made lowercase.
    tarifa = models.IntegerField(db_column='Tarifa')  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=50)  # Field name made lowercase.
    rgb = models.CharField(db_column='RGB', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'zonas'
