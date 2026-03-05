import string
import os
import re
from collections import Counter

# STOPWORDS

stopwords = [
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

# FUNCION LIMPIAR PANTALLA

def limpiarPantalla():
    os.system("cls" if os.name == "nt" else "clear")

# REDUCIR LETRAS REPETIDAS

def reducir_repeticiones(texto):
    return re.sub(r'(.)\1{2,}', r'\1', texto)

# ELIMINAR EMOJIS Y CARACTERES ESPECIALES

def eliminar_emojis(texto):
    return re.sub(r'[^\w\s]', '', texto)

# MENU

limpiarPantalla()
print("****************************************")
print("        NLP PREPROCESSING PIPELINE")
print("****************************************\n")

print("1. Ingresar texto")
print("2. Usar ejemplo")

opcion = input("\nSeleccione opción: ")

if opcion == "1":
   texto = input("\nIngrese texto: ")
else:
   texto = "Holaaaaa, holaaa!!! Este es un ejemplo 😂😂 de texto para probar el pipeline de Instagram!!!"

texto_original = texto

# 1. MINÚSCULAS

texto = texto.lower()

# 2. REDUCIR LETRAS REPETIDAS

texto = reducir_repeticiones(texto)

# 3. ELIMINAR EMOJIS

texto = eliminar_emojis(texto)

# 4. QUITAR PUNTUACION

texto_sin_puntuacion = "".join(
char for char in texto if char not in string.punctuation
)

# 5. ELIMINAR ESPACIOS EXTRA

texto_sin_puntuacion = " ".join(texto_sin_puntuacion.split())

# 6. TOKENIZACION

tokens = texto_sin_puntuacion.split()

# 7. ELIMINAR STOPWORDS

tokens_limpios = []
for word in tokens:
    if word not in stopwords:
       tokens_limpios.append(word)

# 8. TEXTO FINAL

texto_limpio = " ".join(tokens_limpios)

# 9. TOP 5 PALABRAS MAS FRECUENTES

frecuencias = Counter(tokens_limpios)
top5 = frecuencias.most_common(5)

# RESULTADOS

print("\n________________________________________")
print("TEXTO ORIGINAL")
print("________________________________________")
print(texto_original)

print("\n________________________________________")
print("TEXTO EN MINUSCULA")
print("________________________________________")
print(texto)

print("\n________________________________________")
print("TEXTO SIN PUNTUACION")
print("________________________________________")
print(texto_sin_puntuacion)

print("\n________________________________________")
print("TOKENS")
print("________________________________________")
print(tokens)

print("\n________________________________________")
print("TOKENS SIN STOPWORDS")
print("________________________________________")
print(tokens_limpios)

print("\n________________________________________")
print("TEXTO FINAL LIMPIO")
print("________________________________________")
print(texto_limpio)

print("\n________________________________________")
print("TOP 5 PALABRAS MAS FRECUENTES")
print("________________________________________")

for palabra, freq in top5:
    print(palabra, ":", freq)

print("________________________________________")