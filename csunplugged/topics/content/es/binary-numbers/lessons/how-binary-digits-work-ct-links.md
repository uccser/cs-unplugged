{panel type="ct-algorithm"}

# Pensamiento algorítmico

En esta clase hemos usado un algoritmo para convertir un número decimal en uno binario. Es un algoritmo porque es un proceso que se realiza paso a paso y el cual siempre proporcionará la solución adecuada para cualquier entrada siempre que se siga fielmente el proceso descrito.

Aquí tenemos un algoritmo escrito en texto para averiguar qué cartas de puntos deberían mostrarse:

- Averigua el número de puntos que se mostrarán. (Nos referiremos a él como el "número de puntos restantes", que inicialmente es el número total que se mostrará.)
- Para cada carta, de izquierda a derecha (es decir, 16, 8, 4, 2 luego 1): 
    - Si el número de puntos en la carta es mayor que el número de puntos restantes: 
        - Ocultar la carta
    - De lo contrario: 
        - Mostrar la carta
        - Resta el número de puntos en la carta del número de puntos restantes

Ten en cuenta que este algoritmo (de derecha a izquierda) funciona muy bien con las cartas, pero si buscas programas de ordenador que hagan esto, puede que encuentres uno diferente que funcione de derecha a izquierda. Es normal tener varios algoritmos que consigan el mismo resultado.

#### Ejemplos de lo que podrías buscar:

¿Qué alumnos son metódicos a la hora de convertir entre decimal y binario? ¿Cuáles comienzan con la carta que está más a la izquierda y mueven una carta a la derecha cada vez, en vez de elegir y voltear cartas de manera aleatoria hasta conseguir el número correcto?

{panel end}

{panel type="ct-abstraction"}

# Abstracción

La representación de números binarios (usando solo 0 y 1) es una abstracción que oculta la complejidad de los componentes electrónicos y el hardware que hay dentro de un ordenador que almacena datos. La abstracción nos ayuda a simplificar las cosas porque nos permite ignorar los detalles que no necesitamos conocer en este preciso momento.

En este caso, los detalles que podemos ignorar incluyen: que los ordenadores usan dispositivos físicos como circuitos electrónicos y voltajes en circuitos para almacenar y mover datos y que existe una gran cantidad de complejas teorías físicas y matemáticas que hacen que todo esto funcione.

No necesitamos entender cómo funcionan estos circuitos para usar datos y representar cosas usando binario. El uso del binario es una abstracción de estos circuitos y nos permite representar números como si estuvieran formados por bits (0 y 1), para entender datos y resolver problemas sin tener que pensar en lo que está sucediendo en el interior del ordenador.

Otro uso de la abstracción es considerar qué se necesita para representar cualquier dígito en binario. La respuesta es que solo se necesitan dos cosas diferentes. ¡Y pueden ser cualquier cosa! Dos colores diferentes, dos animales diferentes, dos símbolos diferentes, etc. Siempre que haya dos y que sean diferentes, puedes usarlas para representar cualquier número, usando binario, de la misma manera que un ordenador usa electricidad para representar datos.

Podemos usar dígitos binarios para representar cualquier tipo de datos almacenados en un ordenador. Cuando representamos otras formas de datos (como letras, imágenes y sonido) también usamos la abstracción porque ocultamos los detalles de todos los números binarios que se encuentran por debajo y solo vemos una porción completa de datos. Todas las formas de datos terminan siendo representadas como números (que en realidad son solo combinaciones de bits) - para el texto tenemos un número para cada letra, para imágenes usamos un número para cada color y así sucesivamente. ¡Usamos varias capas de abstracción! Por ejemplo, una forma familiar de abstracción es que el mes "octubre" se puede representar con el número diez, que en realidad se representa con los bits 01010, y si estos se almacenan como voltajes en la memoria de un ordenador, al final esto para los voltajes es: "bajo, alto, bajo, alto, bajo".

#### Ejemplos de lo que podrías buscar:

Qué alumnos demuestran la conversión y representación de números binarios usando cosas que no sean “1 y 0”, "blanco y negro” y “encendido y apagado" (por ejemplo usando :) y :( o usando gente de pie o sentada). Si eres capaz de intercambiar términos como "blanco" y "negro" con 0 y 1 sin que los alumnos se preocupen por la diferencia, estarán ejercitando la abstracción.

{panel end}

{panel type="ct-decomposition"}

# Descomposición

Un ejemplo de descomposición es separar la conversión del número a binario en pasos de un bit cada vez. Las preguntas "Esto debería ser 1 o 0" para cada una de las cartas de puntos descomponen el problema en una serie de preguntas.

#### Ejemplos de lo que podrías buscar:

¿Qué alumnos reconocen que es importante empezar con la carta más a la izquierda y solo considerar un bit cada vez? ¿Qué alumnos se concentran en un bit individual cada vez, en lugar de agobiarse intentando trabajar con todos ellos de una sola vez?

{panel end}

{panel type="ct-pattern"}

# Generalización y patrones

El reconocimiento de patrones en el funcionamiento del sistema numérico binario nos proporciona un entendimiento más profundo de los conceptos involucrados y nos ayuda a generalizar estos conceptos y patrones para que podamos aplicarlos a otros problemas.

A un nivel sencillo, comenzamos con los números 1, 2 y 4 y los alumnos lo generalizaron a valores dobles. El ejercicio utiliza números de 5 bits, pero los alumnos deberían de ser capaces de generalizarlo a números de 8 bits o más.

El algoritmo para convertir un número decimal a un número binario sigue un patrón que se puede generalizar para resolver el problema de la devolución de cambio cuando alguien paga en efectivo. Para los números binarios, empieza con el bit más grande, siempre puedes activar un bit si lo necesitas, igual que cuando devuelves cambio empiezas con la denominación más grande y luego siempre usas una moneda (o billete) cuando lo necesitas. Nota sobre la jerga: Este algoritmo se conoce como voraz - ¡toma todo lo que puede cada vez!

{panel type="math"}

# Vínculos matemáticos

Pregúntale a los alumnos qué tiene de especial la conversión de decimal a binario, en contraste con el algoritmo general de devolución de cambio y hazles observar que en el caso general puede ser necesario dar más de una moneda de la misma denominación, mientras que en la conversión binaria siempre hay una (o ninguna) de cada.

{panel end}

Al contar de forma ascendente en binario, existe un patrón para la frecuencia con la que se voltean cartas concretas. El primer bit (con 1 punto) se voltea todas las veces, el segundo (con 2 puntos) se voltea cada dos números, el tercero (con 4 puntos) se voltea cada cuatro... ¿Existe un patrón similar al contar en números decimales?

{image file-path="img/topics/col_binary_counting_pattern.png" alt="Binary counting pattern"}

Si tienes 5 cartas y todas son visibles, tendrás el número 31, que es 1 menos que el valor de la siguiente carta, 32. ¿Es este patrón siempre verdadero?

La cantidad de números que puedes representar con un cierto número de bits es la misma que el valor del siguiente bit que se pueda añadir. Por ejemplo, usando 4 cartas (1, 2, 4, 8) puedes representar 16 números diferentes (0-15) y la siguiente carta en la secuencia es el número 16. Cada vez que añadimos la siguiente carta, también duplicamos la cantidad de números diferentes que podemos representar.

Trabajar con estos patrones es valioso para calcular la relación entre el número de bits que están siendo usados y la potencia de lo que pueden representar.

Explica uno o más de los siguientes patrones:

- Que con un cierto número de cartas puedes formar la misma cantidad de números diferentes que el número de puntos que habría en la siguiente carta que se añadirá a la izquierda (recuerda que 0 es un número).
- Al contar en orden ascendente: la primera carta (1 punto) se voltea cada vez, la segunda carta (2 puntos) se voltea cada dos veces, la tercera (4 puntos), cada cuatro veces y la cuarta (8 puntos), cada ocho veces...
- Que cuando todas las cartas que tienes sean visibles, sumarán el número de la siguiente carta binaria menos 1.

#### Ejemplos de lo que podrías buscar:

¿Qué alumnos reconocieron rápidamente que cada carta estaba duplicando el número de puntos? ¿Pueden los alumnos ver las similitudes entre esto y la multiplicación de los valores posicionales por 10 cuando usan el sistema decimal?

¿Qué alumnos entienden fácilmente los patrones de volteo de las cartas al contar con números binarios?

{panel end}

{panel type="ct-logic"}

# Lógica

El pensamiento lógico consiste en usar reglas que ya conoces y usar la lógica para deducir más reglas e información a partir de estas. Una vez que sabemos el número que representa cada carta binaria, podemos usar este conocimiento para averiguar cómo representar otros números con las cartas. Si memorizas cómo representar los números que podemos formar con 5 cartas, ¿significa esto que entiendes cómo representar cualquier número con cualquier número de bits? No, pero puedes entender cómo hacerlo si entiendes la lógica tras la formación de estos números con las 5 cartas.

Un buen ejemplo de pensamiento lógico en números binarios es el razonamiento que explica por qué cada bit "tiene" que tener un valor particular (ej. tiene que ser 1 o tiene que ser 0) para representar un número dado. Esto a su vez lleva a entender que solo hay una representación para cada número.

#### Ejemplos de lo que podrías buscar:

¿Explican los alumnos explícitamente que el bit más a la derecha tiene que ser un uno porque es el único número impar y por lo tanto es necesario para que podamos formar todos los números impares? Sin él solo podríamos formar números pares.

¿Son los alumnos capaces de explicar que cada carta "tiene" que estar en la forma que está para un número dado, por ejemplo, la carta de 16 puntos es necesaria para el número 19 porque sin ella solo hay 15 puntos restantes a su derecha (no son suficientes); pero la carta 16 no es necesaria para el número 9 porque proporcionaría demasiados puntos?

{panel end}

{panel type="ct-evaluation"}

# Evaluación

Un ejemplo de evaluación consiste en averiguar cuántos valores diferentes se pueden representar con un número dado de bits (p.ej. 5 bits pueden representar 32 valores diferentes) y viceversa (para representar 1000 valores diferentes, necesitas al menos 10 bits).

#### Ejemplos de lo que podrías buscar:

¿Puede un alumno averiguar el intervalo posible con 4 bits? (16)

¿6 bits? (64)

¿8 bits? (256)

Si añadimos un bit más a una representación, ¿cuánto aumenta el intervalo? (lo duplica)

Si añadimos dos bits más a una representación, ¿cuánto aumenta esto el intervalo? (se cuadriplica)

¿Cuántos bits necesitamos para representar 1000 valores diferentes? (10 es suficiente)

{panel end}