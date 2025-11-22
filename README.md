# Proyecto-Micro-CPU-2Bits
Micro-CPU 2Bits

Curso: Arquitectura del Computador I
Catedrático: Josué Morataya

👥 Autores

Nombre 1 — ID

Nombre 2 — ID
(Reemplazar con los datos reales del equipo.)

🎯 Objetivo del Proyecto

El proyecto Micro-CPU 2Bits tiene como finalidad construir una CPU simplificada utilizando una RP2040 Zero y simular conceptos fundamentales vistos en el curso:

🔹 Simulaciones Incluidas

Ciclo de instrucción completo:
Fetch → Decode → Execute → Write-Back (por medio de LEDs).

Banderas de Estado:
Zero, Negative y Overflow.

Calculadora básica de 2 bits:
Permite realizar operaciones con valores entre 0 y 3 usando botones físicos como entrada y un display de 7 segmentos como salida.

🧩 Descripción General del Sistema

El sistema funciona como una mini CPU donde:

Los botones representan los operandos y las operaciones (+, -, =).

Los LEDs muestran el estado interno de la CPU.

El display de 7 segmentos muestra el resultado final.

Toda la lógica está programada en MicroPython utilizando máquinas de estado.

🛠️ Hardware Utilizado

RP2040 Zero (MicroPython)

Protoboard

7 botones (4 dígitos +, −, =)

6 LEDs (Ciclo + Banderas)

Resistencias 220–330Ω

Display 7 segmentos (cátodo común)

Jumpers y cable USB-C

(Para detalles completos, revisar COMPONENTES.md.)

▶️ Instrucciones de Uso
1️⃣ Cargar el Código

Conecta la RP2040 Zero por USB-C.

Abre Thonny.

Selecciona el intérprete MicroPython (RP2040).

Abre el archivo main.py.

Haz clic en Run → Run current script on RP2040.

La placa comenzará a ejecutar la simulación.

🔧 Cómo Operar la Calculadora

Presiona un dígito (0–3) → LED del estado avanza a Decode.

Presiona una operación (+ o −).

Presiona el segundo dígito (0–3).

Pulsa ‘=’ para obtener el resultado.

El display mostrará el valor final (0–3).

Los LEDs de Zero, Negative u Overflow se encenderán si aplica.

Ejemplos:
