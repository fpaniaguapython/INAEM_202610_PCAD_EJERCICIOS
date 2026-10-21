# pip install word2num
import word2num

texto_numero = input('Escribe un número en formato texto:')

numero = word2num.word2num(text=texto_numero, language_code='es')

print(numero)