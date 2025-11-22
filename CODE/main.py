# ==============================================================================
# Proyecto: Calculadora de Un Solo Dígito con Ciclo de Instrucción (MicroPython)
# Código corregido para usar el LED RGB integrado (Neopixel)
# ==============================================================================

import machine
import utime
import neopixel

# --- 1. Asignación de Pines GPIO ---
# Se mantienen las asignaciones de pines.
# El pin 16 es para el NeoPixel integrado.
# ... (el resto de las asignaciones de pines son las mismas)
PIN_BUTTON_0 = 0
PIN_BUTTON_1 = 1
PIN_BUTTON_2 = 2
PIN_BUTTON_3 = 3
PIN_BUTTON_PLUS = 4
PIN_BUTTON_MINUS = 5
PIN_BUTTON_EQUALS = 6
PIN_LED_FETCH = 7
PIN_LED_DECODE = 8
PIN_LED_EXECUTE = 9
PIN_LED_WRITEBACK = 10
PIN_LED_ZERO = 11
PIN_LED_NEGATIVE = 12
PIN_NEOPIXEL = 16 # Pin del LED NeoPixel

# Pines para el Display de 7 Segmentos (Salidas)
PIN_SEGMENT_A = 13
PIN_SEGMENT_B = 14
PIN_SEGMENT_C = 15
PIN_SEGMENT_D = 26
PIN_SEGMENT_E = 27
PIN_SEGMENT_F = 28
PIN_SEGMENT_G = 29

# --- 2. Mapeo de Dígitos a Segmentos ---
# ... (el diccionario DIGIT_MAP es el mismo)
DIGIT_MAP = {
    0: (True, True, True, True, True, True, False),
    1: (False, True, True, False, False, False, False),
    2: (True, True, False, True, True, False, True),
    3: (True, True, True, True, False, False, True),
    'off': (False, False, False, False, False, False, False)
}

# --- 3. Inicialización del Hardware ---
# ... (la inicialización de botones, LEDs y display es la misma)
btn_0 = machine.Pin(PIN_BUTTON_0, machine.Pin.IN, machine.Pin.PULL_UP)
btn_1 = machine.Pin(PIN_BUTTON_1, machine.Pin.IN, machine.Pin.PULL_UP)
btn_2 = machine.Pin(PIN_BUTTON_2, machine.Pin.IN, machine.Pin.PULL_UP)
btn_3 = machine.Pin(PIN_BUTTON_3, machine.Pin.IN, machine.Pin.PULL_UP)
btn_plus = machine.Pin(PIN_BUTTON_PLUS, machine.Pin.IN, machine.Pin.PULL_UP)
btn_minus = machine.Pin(PIN_BUTTON_MINUS, machine.Pin.IN, machine.Pin.PULL_UP)
btn_equals = machine.Pin(PIN_BUTTON_EQUALS, machine.Pin.IN, machine.Pin.PULL_UP)
led_fetch = machine.Pin(PIN_LED_FETCH, machine.Pin.OUT)
led_decode = machine.Pin(PIN_LED_DECODE, machine.Pin.OUT)
led_execute = machine.Pin(PIN_LED_EXECUTE, machine.Pin.OUT)
led_writeback = machine.Pin(PIN_LED_WRITEBACK, machine.Pin.OUT)
led_zero = machine.Pin(PIN_LED_ZERO, machine.Pin.OUT)
led_negative = machine.Pin(PIN_LED_NEGATIVE, machine.Pin.OUT)

segment_pins = [
    machine.Pin(PIN_SEGMENT_A, machine.Pin.OUT),
    machine.Pin(PIN_SEGMENT_B, machine.Pin.OUT),
    machine.Pin(PIN_SEGMENT_C, machine.Pin.OUT),
    machine.Pin(PIN_SEGMENT_D, machine.Pin.OUT),
    machine.Pin(PIN_SEGMENT_E, machine.Pin.OUT),
    machine.Pin(PIN_SEGMENT_F, machine.Pin.OUT),
    machine.Pin(PIN_SEGMENT_G, machine.Pin.OUT)
]

# Inicialización del NeoPixel (LED integrado)
neopixel_led = neopixel.NeoPixel(machine.Pin(PIN_NEOPIXEL), 1)

# --- 4. Funciones de Ayuda y Lógica del Sistema ---
# ... (las funciones display_digit, read_buttons y wait_for_button_release son las mismas)
def clear_all_outputs():
    """Apaga todos los LEDs y el display, incluyendo el NeoPixel."""
    led_fetch.value(0)
    led_decode.value(0)
    led_execute.value(0)
    led_writeback.value(0)
    led_zero.value(0)
    led_negative.value(0)
    set_overflow_led(False) # Usa la nueva función
    display_digit('off')

def display_digit(digit):
    """
    Muestra un dígito en el display de 7 segmentos.
    :param digit: El número (0-3) o la clave 'off' para apagarlo.
    """
    segments_to_light = DIGIT_MAP.get(digit, DIGIT_MAP['off'])
    for i, state in enumerate(segments_to_light):
        segment_pins[i].value(state)

def read_buttons():
    """
    Lee los botones de dígitos y operaciones.
    Implementa un simple anti-rebote (debouncing).
    :return: El valor del botón presionado o None.
    """
    if btn_0.value() == 0: return 0
    if btn_1.value() == 0: return 1
    if btn_2.value() == 0: return 2
    if btn_3.value() == 0: return 3
    if btn_plus.value() == 0: return '+'
    if btn_minus.value() == 0: return '-'
    if btn_equals.value() == 0: return '='
    return None

def wait_for_button_release():
    """Espera a que todos los botones sean liberados."""
    while read_buttons() is not None:
        utime.sleep_ms(50)

def set_overflow_led(state):
    """
    Controla el LED NeoPixel integrado para la función de Overflow.
    :param state: True para encenderlo en rojo, False para apagarlo.
    """
    if state:
        neopixel_led[0] = (0, 255, 0) # Color rojo para indicar error
    else:
        neopixel_led[0] = (0, 0, 0)   # Apagado
    neopixel_led.write()

# --- 5. Máquina de Estados de la Calculadora ---
# Se mantiene la misma lógica de la máquina de estados.
STATE_INPUT1 = 0
STATE_OPERATION = 1
STATE_INPUT2 = 2
STATE_CALCULATE = 3
STATE_RESULT = 4

calculator_state = STATE_INPUT1
operand1 = None
operation = None
operand2 = None
result = None

clear_all_outputs()

print("Calculadora de Arquitectura de Cómputo iniciada...")
print("Esperando el primer operando (0-3).")

while True:
    button_pressed = read_buttons()
    if button_pressed is not None:
        utime.sleep_ms(200)

        if calculator_state == STATE_INPUT1:
            if isinstance(button_pressed, int) and button_pressed >= 0 and button_pressed <= 3:
                led_fetch.value(1)
                operand1 = button_pressed
                display_digit(operand1)
                print(f"Operando 1: {operand1}")
                calculator_state = STATE_OPERATION
                utime.sleep_ms(500)
                led_fetch.value(0)
        
        elif calculator_state == STATE_OPERATION:
            if button_pressed == '+' or button_pressed == '-':
                led_decode.value(1)
                operation = button_pressed
                print(f"Operación: {operation}")
                calculator_state = STATE_INPUT2
                utime.sleep_ms(500)
                led_decode.value(0)

        elif calculator_state == STATE_INPUT2:
            if isinstance(button_pressed, int) and button_pressed >= 0 and button_pressed <= 3:
                led_fetch.value(1)
                operand2 = button_pressed
                display_digit(operand2)
                print(f"Operando 2: {operand2}")
                calculator_state = STATE_CALCULATE
                utime.sleep_ms(500)
                led_fetch.value(0)
                
        elif calculator_state == STATE_CALCULATE:
            if button_pressed == '=':
                led_execute.value(1) # Simula la fase de EXECUTE (ALU)
                
                # Realiza la operación
                if operation == '+':
                    result = operand1 + operand2
                elif operation == '-':
                    result = operand1 - operand2
                
                # Evalúa las banderas (FLAGS)
                led_zero.value(1) if result == 0 else led_zero.value(0)
                led_negative.value(1) if result < 0 else led_negative.value(0)
                
                # --- Lógica de Overflow Corregida ---
                # Verifica si el resultado excede el rango de nuestra calculadora (0-3).
                if (operation == '+' and result > 3) or (operation == '-' and result < 0):
                    set_overflow_led(True)
                else:
                    set_overflow_led(False)
                
                print(f"Calculando {operand1} {operation} {operand2} = {result}")
                utime.sleep(2)
                led_execute.value(0)
                
                # --- FASE DE WRITE-BACK ---
                led_writeback.value(1)
                
                # Muestra el resultado (si está en el rango válido)
                if result >= 0 and result <= 3:
                    display_digit(result)
                else:
                    display_digit('off') # Apaga el display para indicar overflow
                
                utime.sleep(2)
                led_writeback.value(0)
                
                calculator_state = STATE_RESULT

        elif calculator_state == STATE_RESULT:
            if button_pressed == '=':
                print("Reiniciando...")
                clear_all_outputs()
                operand1 = None
                operation = None
                operand2 = None
                result = None
                calculator_state = STATE_INPUT1
    
    utime.sleep_ms(50)