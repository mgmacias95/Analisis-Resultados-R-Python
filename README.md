# Analisis-Datos-R-Python
Cómo pasé de analizar resultados con Excel a analizarlos con R+Python

## Cómo empezó todo...

Todo empezó cuando me mandaron hacer una práctica para la univerdad en la que tenía que:

* Desarrollar cuatro algoritmos diferentes.

* Ejecutarlos en 20 casos diferentes, desde tamaño $n = 20$ hasta tamaño $n = 256$.

* Hacer una documentación explicando el problema a resolver, cada algoritmo desarrollado e incluyendo un pseudocódigo de los mismos.

* Incluir en dicha documentación un estudio estadístico de los resultados, valorando cada algoritmo en función de cómo había trabajado con casos grandes ($n$ grande) o casos pequeños ($n$ pequeño) y de cómo de buenos eran los resultados en comparación con el mejor resultado conocido y con los resultados obtenidos por el resto de algoritmos. Además, incluir gráficas que apoyaran tus conclusiones estaba "muy bien visto" (codo, codo, guiño guiño).

y todo esto en unas tres semanas aproximadamente.

### Dormida en los laureles

Empecé con bastante tranquilidad pensando que en dos semanas tendría todo el trabajo hecho y me quedaría otra semana extra para documentar. A la hora de realizar los algoritmos me encontré con algunos fallos y varios quebraderos de cabeza, pero pude tenerlos todos terminados en esas dos semanas. Empecé a hacer mi documentación explicando con todo detalle todo lo que había hecho, centrándome en obtener tanto una buena presentación como una buena redacción y, finalmente, me quedaron dos días para hacer lo más importante: el análisis de los resultados. 

Para hacer el análisis, el profesor nos había dejado preparada una hoja de cálculo _plantilla_ con todos los datos que teníamos que rellenar y calcular. En rellenar la maldita plantilla se me fue media mañana, por no decir la mañana entera, ya que en _Calc_ tienes que introducir los decimales con una coma y _Python_ los devolvía con un punto. A pesar de esto aún no cundía demasiado el pánico pues tenía otro día más. 

Cuando ya calculé con _Calc_ todo lo que había que calcular vino __el problema__: poner todos los datos que había calculado en mi documento de LaTeX. Un amigo me pasó un script que te permite exportar la tabla con sintaxis `tabular` de LaTeX pero, en la hoja de cálculo tenía las tablas que había hecho para todos y cada uno de los algoritmos y en mi documento tenían que ir separadas en secciones. Al final después de pelearme con _Calc_ conseguí separar las tablas e incluirlas en mi documento, pero había perdido un precioso día para documentar y analizar los resultados que había estado __todo el día__ preparando.

### Último día. Kernel panic.

Llegó el último día que, como tenía clase por la tarde, era en realidad _la última mañana_. Decidí que sería una buena idea poner gráficas en mi documentación, pues con las tablas no me había dado como para escribir _todo lo que me hubiese gustado_ y además, le darían a mi documento un extra de "profesionalidad". 

Así que me dispuse a intentar generar un gráfico en la hoja de cálculo que tenía. Intenté todas las combinaciones posibles de datos, tipos de gráficos, colores, leyendas y demás herramientas que proporciona _Calc_ para hacer gráficos y con ninguna obtenía un buen gráfico que realmente reflejase lo que quería. De hecho, lo más decente que pude obtener fueron dos gráficos que no decían absolutamente nada sobre los datos y que no supe ni siquiera etiquetar... supongo que por los nervios de que la entrega se aproximaba y mi análisis daba pena.

Estos son los gráficos que finalmente incluí en la que iba a ser la chachi documentación extra profesional a 5 minutos de que la entrega se cerrase.

![Primer gráfico horrible](img/calc1.png "Primer gráfico horrible")

![Segundo gráfico horrible](img/calc2.png "Segundo gráfico horrible")

¿Podéis sacar alguna conclusión de ellos? Yo no.
