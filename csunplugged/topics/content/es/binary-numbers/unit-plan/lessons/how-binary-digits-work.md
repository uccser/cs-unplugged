# Cómo funcionan los dígitos binarios

## Preguntas clave

- ¿Qué diferentes sistemas numéricos conocemos? (Las respuestas pueden incluir: Números romanos; Marcas de conteo; Bases numéricas como binario, octal y hexadecimal; Sistemas basados en idiomas como el chino o el egipcio antiguo).
- ¿Por qué normalmente usamos 10 dígitos? (Probablemente porque tenemos 10 dedos, además, es una manera bastante eficiente de escribir las cosas en comparación con, digamos, las marcas de conteo).
- ¿Por qué tenemos diferentes sistemas numéricos? (Son prácticos para cosas diferentes, por ejemplo, las marcas de conteo son fáciles si estás contando; los números romanos pueden ser útiles para hacer que un número parezca más misterioso o más difícil de leer).

## Clase inicial

{panel type="video"}

# Ve el ejemplo de clase

{video url="https://vimeo.com/437725275"}

{panel end}

{panel type="general"}

# Nota de los autores

Hemos notado que una vez que los alumnos comprenden cómo funciona el sistema numérico binario, tienen muchas preguntas y les interesa explorar más a fondo los conceptos descritos en esta clase. Hemos añadido mucha información a esta clase, sin embargo, no es nuestra intención que enseñes y cubras todos los conceptos, sino que tengas a tu alcance la información que necesites cuando tus alumnos expresen interés en aprender más.

{panel end}

{panel type="general"}

# Notas sobre los recursos

También hay una versión interactiva en línea de las cartas binarias [aquí](http://www.csfieldguide.org.nz/en/interactives/binary-cards/index.html?digits=8), de la [Computer Science Field Guide](http://www.csfieldguide.org.nz/), pero es preferible trabajar con las cartas físicas.

{panel end}

1. Sostén las primeras 5 cartas (1, 2, 4, 8 y 16 puntos), pero no dejes que los alumnos vean los puntos. Pide a 5 alumnos que se ofrezcan como voluntarios para ser los “bits” y que se pongan de pie en una fila delante de la clase.

2. Entrega la carta de 1 punto a la persona de la derecha. Explica que ellos son un "bit" (dígito binario) y que pueden estar encendidos o apagados, ser blancos o negros, tener 0 o 1 punto(s). La única regla es que su carta sea completamente visible o no visible (es decir, volteada). Entrega la segunda carta a la segunda persona de la derecha. Remarca que esta carta tiene 2 puntos (visible) o ninguno (boca abajo).

    {image file-path="img/topics/col_binary_2cards.png" alt="2 niños sosteniendo cartas binarias"}

3. Pregunta a la clase cuál será el número de puntos en la siguiente carta. Haz que expliquen sus respuestas.

    {panel type="teaching"}

    # Observaciones didácticas

    Los alumnos normalmente sugieren que debería ser tres. Si sugieren 4, probablemente han hecho la actividad antes (¡o han visto las cartas que tienes de la mano!) Si sugieren el número equivocado, no los corrijas, continúa sin hacer ningún comentario, para que puedan construir la regla por sí mismos.

    {panel end}

4. Entrega en silencio la carta de cuatro puntos y deja que intenten averiguar el patrón.

    {image file-path="img/topics/col_binary_3cards.png" alt="3 niños sosteniendo cartas binarias"}

    {panel type="teaching"}

    # Observaciones didácticas

    Por lo general, algunos alumnos se quejarán de que te has saltado el tres, solo tienes que indicar que no has cometido un error. Esto les da la oportunidad de intentar construir el patrón por sí mismos.

    {panel end}

5. Pregunta cuál es la siguiente carta y por qué.

    {panel type="teaching"}

    # Observaciones didácticas

    Llegado este punto, es común que los alumnos supongan que es 6 (ya que sigue a los números 2 y 4). Sin embargo, si dejas que lo piensen un poco más, algunos generalmente dirán el número 8 y esos estudiantes deberían de ser capaces de convencer a los otros de que están en lo correcto (un alumno puede explicar esto de varias maneras, por ejemplo, que cada carta es el doble de la anterior o que si tomas dos de una carta, obtienes la siguiente)

    {panel end}

6. Los alumnos deberían de poder averiguar la quinta carta (16 puntos) sin ayuda:

    {image file-path="img/topics/col_binary_5cards.png" alt="5 niños sosteniendo cartas binarias"}

7. ¿Cuántos puntos tendría la próxima carta si continuamos hacia la izquierda? (32) ¿La próxima...? (No hay necesidad de que los alumnos sostengan estas cartas, ya que no se usarán en la siguiente parte de la actividad, pero se las puedes mostrar para confirmar que están en lo correcto).

8. Continúa con 64 y 128 puntos.

    {panel type="teaching"}

    # Observaciones didácticas

    Con 128 puntos habría 8 cartas. Esto es 8 bits, que es comúnmente conocido como byte. Mencionar esto en este punto puede suponer una distracción, pero puede que algunos alumnos ya estén familiarizados con la idea de que 8 bits es un byte y hagan esa observación. Sin embargo, mientras tanto trabajaremos con una representación de 5 bits, la cual no es tan útil como un byte entero, pero es un buen tamaño para enseñar. (Un byte es una práctica agrupación de bits y normalmente el almacenamiento de los ordenadores se basa en bytes en lugar de en bits individuales; es igual que que los huevos se vendan en docenas; podrían venderse individualmente, pero los grupos de una docena son generalmente más prácticos para todos los interesados).

    Un error común es entregar las cartas de izquierda a derecha, pero una convención en la representación numérica es que el valor menos significativo esté a la derecha y esta es una idea importante que los alumnos deberían asimilar con esta actividad.

    {panel end}

## Actividades de la lección

1. Recuerda a los alumnos que la regla es que una carta o tiene los puntos completamente visibles o ninguno de ellos es visible. Si podemos encender y apagar las cartas mostrando el anverso y el reverso de la carta, ¿cómo mostraríamos exactamente 9 puntos? Empieza preguntando si quieren la carta 16 (deberían mencionar que tiene demasiados puntos), entonces la carta 8 (probablemente razonarán que sin ella no quedan suficientes puntos), luego 4, 2 y 1. Sin que se les haya dado ninguna otra regla aparte de que cada carta sea visible o no, los alumnos normalmente harán la siguiente representación.

    {image file-path="img/topics/binary-cards-total-9.png" alt="Diagrama mostrando que 2 cartas binarias hacen el número 9"}

    {panel type="math"}

    # Vínculos matemáticos

    Base 10 (nuestro sistema de conteo) tiene 10 dígitos, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Cuando contamos en base 10, contamos de 0 a 9 y entonces nos quedamos sin dígitos. Así que necesitamos añadir otra columna; ponemos un 1 en esa columna y empezamos a contar de nuevo desde 0. Esto forma el número 10, luego repetimos ese proceso hasta que la columna de las decenas es 9 y la columna de las unidades es 9 (haciendo 99); a partir de ahí añadimos otra columna. Por lo tanto, tenemos el familiar sistema de valores posicionales que se puede mostrar de esta forma:

    100.000 | 10.000 | 1.000 | 100 |10 | 1

    *Nota: Utiliza el ejemplo de valor posicional apropiado en base a lo que ya hayas enseñado en tu clase; este es un ejemplo ampliado.*

    Base 2 (binario) sigue la misma lógica, excepto en que se mueve mucho más rápido al "siguiente" valor posicional, ya que solo hay dos dígitos, 0 y 1. Los valores posicionales en binario tienen el siguiente aspecto:

    32 | 16 | 8 | 4 | 2 | 1 |

    A veces, los alumnos confunden el orden de los dígitos en una representación binaria. Para ayudar a los alumnos a comprender el orden correcto de los dígitos binarios, haz esta pregunta: Si yo te diera 435,00$, ¿qué número te interesa más? ¿Es el 4 o el 5? ¿Y eso por qué? Ocurre lo mismo en el código binario, el valor más bajo (el dígito menos significativo) es el que está más a la derecha, mientras que el dígito más significativo es el que está más a la izquierda.

    {panel end}

2. Ahora pregunta: "¿Cómo formaríais el número 21?" (De nuevo, empieza preguntando si quieren la carta 16, luego la carta 8 y así sucesivamente de izquierda a derecha).

3. Se trata de un algoritmo para convertir números a una representación binaria. Pensemos en los pasos a seguir para hacerlo juntos.

    a. Empieza con todos los números encendidos (mostrando los puntos).

    {image file-path="img/topics/lightbulb_series_1.png" alt="5 bombillas encendidas"}

    b. Piensa en la representación del número 10

    c. ¿El 16 cabe en el 10? No, así que apágalo

    {image file-path="img/topics/lightbulb_series_2.png" alt="4 bombillas encendidas"}

    d. ¿El 8 cabe en el 10? Sí, así que déjalo encendido. ¿Cuántos faltan? (2)

    e. ¿El 4 cabe en el 2? No, así que apágalo

    {image file-path="img/topics/lightbulb_series_3.png" alt="3 bombillas encendidas"}

    f. ¿El 2 cabe en el 2? Sí, así que déjalo encendido. ¿Cuántos faltan? (Ninguno)

    g. Apaga el 1.

    {image file-path="img/topics/lightbulb_series_4.png" alt="2 lightbulbs switched on"}

## Aplicación de lo que acabamos de aprender

- Divide a los alumnos en parejas.
- Dale a cada pareja un conjunto de las cartas binarias más pequeñas (5 o 6 cartas, dependiendo del intervalo de números con el que se sientan cómodos).
- Empezando con solo 5 cartas, haz que practiquen el algoritmo (decidiendo sobre cada carta de izquierda a derecha) para números como 20, 15 y 8.

1. Explica a los alumnos que estamos trabajando con solo dos dígitos, por lo que se denominan dígitos binarios. Son tan comunes que tenemos un nombre corto para ellos: escribe "dígito binario" en un pedazo de papel, luego rasga la "bi" del principio de binario y luego la "t" de dígito, colócalos juntos y pregunta cuál es la palabra que se ha formado al combinarlos ("bit"). Este es el nombre corto para un dígito binario, así que las 5 cartas que ellos poseen son en realidad 5 bits.

2. Ahora vamos a contar desde el número más pequeño que podemos formar hasta el número más alto:

    a. ¿Cuál es el número más pequeño? (puede que sugieran el 1, pero luego se darán cuenta de que es el 0).

3. Muestra el número cero en las cartas (es decir, sin que se muestren los puntos).

4. Ahora cuenta 1, 2, 3, 4 … (cada pareja debería resolver estos números entre ellos).

5. Una vez que empiecen a acostumbrarse, pregúntales: ¿con qué frecuencia estamos viendo la carta de 1 punto? (de forma alternada, que es cada número impar)

    a. ¿Qué otros patrones vemos? (algunos pueden observar que la carta de 2 puntos se voltea cada dos veces, la de 4 puntos cada 4 veces y así sucesivamente; ¡por lo que la carta de 16 puntos no hace mucho!)

6. Continúa hasta que todas las cartas estén "encendidas" y hayan contado hasta 31. ¿Y después qué? (Tenemos que añadir una carta nueva). ¿Cuántos puntos tiene? (32) ¿Qué tenemos que hacer con las otras 5 cartas cuando lleguemos a 32? (tenemos que apagarlas todas)

7. Investiguemos esto un poco más ...

    a. Cuando tengo dos bits, ¿puedo formar un máximo de? (3)

    b. Añado otro bit, ¿cuántos puntos tiene? (4)

    c. Apago los dos primeros bits para formar 4, ¿cierto?

    d. Ahora vamos a encender los tres bits, ¿cuántos tenemos ahora? (7)

    e. Añado otro bit, ¿cuántos puntos tiene? (8)

    f. Repítelo hasta que se reconozca el patrón que consiste en que el número de la siguiente carta a la izquierda es una unidad mayor que el número total de puntos en todas las cartas de la derecha (ej. hay 15 puntos en las cartas de 8, 4, 2 y 1, por lo que la siguiente carta a la izquierda es de 16). Esto hace más fácil calcular el número si todos los bits están encendidos - duplica la carta de la izquierda y resta 1.

    g. ¿Cuántos números diferentes puedo formar con dos bits? (4; los alumnos suelen decir 3 porque no han contado el 0)

    h. Añadamos el siguiente bit; ¿cuántos números diferentes podemos formar ahora? (8, de nuevo, a menudo 7 será la primera respuesta)

    i. Repítelo hasta que se reconozca el patrón que consiste en que cada vez que añadimos otro bit podemos representar el doble de números.

{panel type="teaching"}

# Observaciones didácticas

Un concepto con el que puede que los alumnos tengan problemas es que el número de valores es uno más que el valor máximo (p.ej. desde 0 hasta 7, hay 8 números diferentes). La misma observación se presenta con el número de dígitos en los números decimales convencionales; el dígito más grande es el 9, pero hay 10 dígitos posibles (contando el 0). Esto a veces se conoce como el problema del poste (el número de postes de una valla es uno más que el número de espacios entre ellos) y se da mucho en informática.

{panel end}

## Reflexión de la clase

- ¿Funcionaría esta actividad si usamos cartas blancas y cartas color crema? ¿Por qué? ¿Por qué no? (En principio, podrías usarlas, pero no sería una buena idea. La respuesta que buscamos es que no son colores que contrasten, por lo que sería difícil ver si están encendidas o apagadas. Esto nos da una pista de por qué los ordenadores usan representaciones físicas fáciles de distinguir).
- ¿Qué símbolos o formas contrastantes podemos mostrar como encendidos y apagados en binario?

    - (Las ideas podrían incluir sostener las cartas arriba o abajo; simplemente levantando una mano; sentándose o poniéndose de pie; o usando representaciones diferentes tales como luces encendidas o apagadas).

- Los ordenadores son más baratos y más fáciles de fabricar si representan datos con solo dos valores contrastantes, que representamos con los números 0 y 1. ¿Qué otra cosa podemos usar en la escritura para representar dos opuestos? (Tal vez cara o cruz; cara feliz o cara triste; o cualquier otra pareja de símbolos).

- Ampliando esta idea, los números se pueden representar por un voltaje cercano a 5 voltios o a 0 voltios. Los circuitos se montan de forma que cualquier voltaje menor a 2,5 voltios cuente como 0 y cualquier voltaje mayor a 2,5 voltios cuente como 1. Al igual que los colores contrastantes de las cartas, resulta muy fácil reconocer esto. Podríamos haber tenido 10 colores de cartas para representar los dígitos del 0 al 10 y podríamos tener diez rangos de voltaje ( de 0 a 0,5, 0,5 a 1,0 y así sucesivamente), pero es mucho más complicado fabricar circuitos rápidos y precisos así.
