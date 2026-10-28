"""
Crear la clase Encuesta.
Los atributos son:
- Valoración del curso: int [0-9]
- Valoración del material: int [0-9]
- Valoración de las instalaciones: int [0-9]

Los métodos son:
- Obtención de la media de valoraciones
- Obtención de la valoración del curso

Crear un objeto Encuesta con los valores que se quieran
e invocar a los métodos de cálculo de medias y de obtención
de la valoración del curso.

"""
class Encuesta:
    def __init__(self, 
                 valoracion_curso: int, 
                 valoracion_material: int, 
                 valoracion_instalaciones:int):
        self.__validar_valores(valoracion_curso, valoracion_material, valoracion_instalaciones)
        self.valoracion_curso = valoracion_curso
        self.valoracion_material = valoracion_material
        self.valoracion_instalaciones = valoracion_instalaciones

    def __validar_valores(self, valoracion_curso, valoracion_material, valoracion_instalaciones):
        if valoracion_curso<0 or valoracion_curso>9:
            raise ValueError('La valoración del curso debe estar en el rango [0-9]')
        if valoracion_material<0 or valoracion_material>9:
            raise ValueError('La valoración del material debe estar en el rango [0-9]')
        if valoracion_instalaciones<0 or valoracion_instalaciones>9:
            raise ValueError('La valoración de las instlaciones debe estar en el rango [0-9]')

    def get_media(self):
        media = (self.valoracion_curso + 
                 self.valoracion_material + 
                 self.valoracion_instalaciones) / 3
        return media

    def get_valoracion_curso(self):
        return self.valoracion_curso


encuesta_angel = Encuesta(valoracion_curso=9, valoracion_material=8, valoracion_instalaciones=9)
valoracion_promedio = encuesta_angel.get_media()
print(f'La valoración promedio es {valoracion_promedio}')