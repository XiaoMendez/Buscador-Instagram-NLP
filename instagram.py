import string
import os

stopwords = [
# BASICAS
    'de','la','que','el','en','y','a','los','del','se','las','por','un','una',
    'para','con','no','lo','como','más','o','pero','su','este','ese','esto','eso',
    'mi','mis','tu','tus','sus','ya','si','sin','sobre','entre','también','muy',
    'hay','donde','cuando','quien','quienes','cual','cuales',

# INSTAGRAM
    'usuario','usuarios','perfil','perfiles','reel','reels','post','posts',
    'publicacion','publicaciones','historia','historias','destacado','destacados',
    'feed','seguir','seguidores','siguiendo','like','likes','comentario',
    'comentarios','video','videos','foto','fotos','imagen','imagenes',
    'cuenta','cuentas','bio','link','dm','live','story','stories','explore'
]

malas_palabras = [
    'puta','puto','putas','putos','mierda','mierdas','joder','jodido','jodida','jodidos','jodidas',
    'coño','coños','carajo','carajos','cabrón','cabron','cabrones','cabrona','cabronas',
    'pendejo','pendeja','pendejos','pendejas','idiota','idiotas','imbecil','imbécil','imbeciles','imbéciles',
    'estupido','estúpido','estupida','estúpida','estupidos','estúpidos','estupidas','estúpidas',
    'tonto','tonta','tontos','tontas','tarado','tarada','tarados','taradas',
    'gilipollas','gilipolla','capullo','capullos','mamón','mamon','mamones','mamona','mamonas',
    'zorra','zorras','zorro','zorros','perra','perras','perro','perros',
    'maldito','maldita','malditos','malditas','malparido','malparida','malparidos','malparidas',
    'hijueputa','hijueputas','hijo de puta','hija de puta','hijoputa','hijoputas','culero','culera','culeros','culeras',
    'culo','culos','culiao','culiada','culiaos','culiadas','chingar','chingado','chingada','chingados','chingadas',
    'pinche','pinches','verga','vergas','mierdero','cabrear','cabreado','cabreada','maricon','maricón','maricones',
    'marica','maricas','marimacha','pelotudo','pelotuda','pelotudos','pelotudas','boludo','boluda','boludos','boludas',
    'concha','conchas','putiza','cagada','cagado','cagados','cagadas','cagar','cagarse','vete a la mierda',
    'vete al carajo','vete a la verga','chingas a tu madre','hdp'
]

# FUNCION LIMPIAR PANTALLA
def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")
limpiarPantalla()

# INICIO
limpiarPantalla()
print("________________________________________")
print("        BUSCADOR")
print("________________________________________\n")

texto = input("Ingrese texto: ")
texto_original = texto
texto = texto.lower()

# Quitar puntuación
texto_sin_puntuacion = "".join(
    char for char in texto if char not in string.punctuation
)

tokens = texto_sin_puntuacion.split()

# CENSURA MALAS PALABRAS
tokens_censurados = []

for palabra in tokens:
    if palabra in malas_palabras:
        censura = "*" * len(palabra)
        tokens_censurados.append(censura)
    else:
        tokens_censurados.append(palabra)

texto_censurado = " ".join(tokens_censurados)

# LIMPIEZA PARA BUSCADOR
tokens_limpios = []

for word in tokens:
    if word not in stopwords and word not in malas_palabras:
        tokens_limpios.append(word)

texto_limpio = " ".join(tokens_limpios)

# RESULTADOS
print("\n________________________________________")
print("TEXTO")
print("________________________________________")
print(texto_censurado)
print("________________________________________")
print("TEXTO LIMPIO PARA BUSCADOR")
print("________________________________________")
print(texto_limpio)
print("\n________________________________________")