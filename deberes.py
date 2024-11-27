import streamlit as st

# Texto
st.title("Jordan 1")
st.text("Si hablamos de leyendas del baloncesto, es imposible que no se nos venga a la cabeza el nombre de Michael Jordan. Y lo mismo ocurre cuando hablamos de sneakers. Si tenemos que pensar en zapatillas legendarias, seguro que las Air Jordan 1 son de las primeras que mencionamos. No podía ser de otra manera, puesto que Nike se inspiró en el popular jugador de la NBA e incluso tomó su nombre para crear estas deportivas de basket tan míticas. Fue a mediados de los años 80 cuando Nike creó la marca Jordan y, gracias a su buena acogida, siguieron lanzando un nuevo modelo cada temporada con la idea de ir renovando el calzado deportivo de Michael Jordan. Las primeras Air Jordan 1 se crearon a medida para el jugador, pero tiempo después ya se empezaron a fabricar tallas estándar para cualquier persona. unque a día de hoy sigue sorprendiendo esta anécdota, la verdad es que al principio Michael Jordan no quería firmar con Nike. Él era más de adidas. O de Converse, pues eran las únicas zapatillas que se ponía en su época de estudiante. Al jugador de los Chicago Bulls no le convencían demasiado las zapatillas de Nike, a las que incluso criticó diciendo que parecían «zapatillas del diablo». Tampoco le gustaba el grosor de la entresuela, demasiado alto para él, que prefería notar con más precisión el suelo de la cancha. Sin embargo, este comentario fue muy importante ya que llegó a oídos de Nike. Fue entonces cuando el diseñador Peter Moore decidió reducir el tamaño de la mediasuela y marcar un nuevo camino en el calzado de la marca. Como podrás imaginar, al final consiguieron convencerle para crear una línea de zapatillas propia. Las Nike Air Jordan 1 se pusieron a la venta de forma oficial en 1985 y serían las primeras de muchas. Llegaron con un diseño high top muy propio del calzado de baloncesto, es decir, con una caña alta que cubriera el tobillo. También destacaba el logo Swoosh de Nike en el lateral y el primero de los logos de Air Jordan compuesto por un balón de baloncesto con alas. No sería hasta 1987 cuando Nike presentó el famoso logo Jumpman, que consistía en la propia silueta de Michael Jordan saltando por los aires a punto de marcar un mate. Es por eso que la línea Retro de las Air Jordan 1 no están decoradas con este logo, ya que apareció años después. El modelo OG de las Jordan 1 combinaba negro y rojo de una forma muy intensa y llamativa. De hecho, a la NBA no le hicieron mucha gracia y no dudó en criticarlas por no cumplir con la normativa. Por aquel entonces lo habitual era que las zapatillas de los jugadores tuviesen una base blanca y algunos detalles basados en los colores de su equipo. Sin embargo, esta polémica solo consiguió que se hablara mucho de esta zapatilla y que, por lo tanto, se hiciera más popular todavía. En Nike aprovecharon todo este revuelvo para crear la campaña Banned!, que fue todo un éxito. No hay mal que por bien no venga.")

# Botones
if st.button("❄️"):
    st.snow()
if st.button("🎈"):
    st.balloons()

# Imagen con enlace (no va)
# st.markdown(
#     f"""
#     stockx_url = "https://stockx.com/es-es/air-jordan-1-retro-high-og-chicago-reimagined-lost-and-found"
#     image_url = "https://cdn.shopify.com/s/files/1/0094/6307/0798/files/How_To_Spot_Real_vs_Fake_Air_Jordan_1_Lost_Found_1024x1024_73f4a0d3-c097-473d-8b20-5b66494628bd.webp?v=1719399720"

#     <a href="{stockx_url}" target="_blank">
#         <img src="{image_url}" alt="Jordan 1 Lost and Found" style="width:200px;">
#     </a>
#     """)

# Enlaces
st.write("Puedes comprar Jordan 1 en: https://www.nike.com/es/ y https://www.jdsports.es/")

# Alertas
st.toast("Bienvenido a esta web, espero que te guste la historia de las Jordan 1 y la disfrutes")

st.warning("❌ ERROR")
