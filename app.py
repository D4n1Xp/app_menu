# importando principales librerias
from pywebio.input import *
from pywebio.output import *
from pywebio.platform import *
import pywebio
import time

# Configuracion tema para toda la app
@config(theme="minty")
def main():
    # Popup de bienvenida y toma de datos
    @popup('Bienvenido')
    def show_popup():
        put_text('Por favor introduce la informacion basica solicitada')
        data = input_group('Información Basica', [
            input('Introduce tu nombre: ',
                  name='nombre', required=True),
            input('Introduce tu apellido: ',
                  name='apellido', required=True)
        ])

    show_popup()

    # titulo
    put_html('<h1>ELIGE TU MENÚ</h1>')
    put_markdown('**Te mostramos las pizzas disponibles**')

    # Tablas con ingredientes y complementos
    put_table([
        ['Pizza', 'Precio', 'Ingredientes'],
        ['Hawaina', 10, 'Queso, tomate, Piña'],
        ['Carbonara', 15, 'Salsa Carbonara, Queso, Jamón, Bacon'],
        ['Barbacoa', 15.50, 'Salsa Barbacoa, Queso, Carne, Bacon'],
        ['4 Quesos', 8, 'Mezcla de quesos']
    ])

    put_markdown('**Complementos disponibles**')
    put_table([
        ['Complemento', 'Precio'],
        ['Agua', 3],
        ['Helado', 6],
        ['Alitas de pollo', 9]
    ])

    # Funcion, al pulsar en click podemos realizar el pedido
    def funcion_click(pedido):

        # Logica: Si al pulsar el boton empezar pedido, mostrar opciones a elegir
        if pedido == 'Empezar pedido':
            opciones = {
                'Pizza': ['Hawaina', 'Carbonara', 'Barbacoa', '4 Quesos'],
                'Complementos': ['Agua', 'Helado', 'Alitas de pollo']
            }
            eleccion = list(opciones.keys())
            pedido1 = input_group("Realiza tu pedido: ", [
                select('Que deseas pedir: ', options=eleccion, name='opcion_1',
                       onchange=lambda c: input_update('opcion_2', options=opciones[c])),
                select(
                    'Opciones', options=opciones[eleccion[0]], name='opcion_2'),
            ])
            # Mostrando pedido realizado
            put_markdown('**Este es tu pedido:**')

            # barra de progreso
            put_processbar('bar')
            for i in range(1, 11):
                set_processbar('bar', i / 10)
                time.sleep(0.1)

            put_text(f'Gracias: {pedido1}')

    # Boton que ejecutara la funcion de pedido
    put_buttons(['Empezar pedido'], onclick=funcion_click)

    pywebio.session.hold()


# inicio de app y puerto de conexion
# http://192.168.161.56:8080
start_server(main, port=8080)
