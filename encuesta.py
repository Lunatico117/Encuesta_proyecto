# Creado por Samuel Thomas Vásquez Gerena
# Clase principal: Encuesta
class Encuesta:
    def __init__(self, preguntas):
        # Lista de preguntas de la encuesta
        self.preguntas = preguntas  
        # Diccionario: clave = nombre del estudiante y lista de respuestas
        self.respuestas = {}  

    def agregar_respuesta(self, nombre, respuestas_estudiante):
        
        # Esto guarda las respuestas de un estudiante en el diccionario.
        # nombre: string con el nombre del estudiante
        # respuestas_estudiante: lista con las respuestas
        
        self.respuestas[nombre] = respuestas_estudiante

    def mostrar_resultados(self):
        #Imprime todas las respuestas guardadas
        print("\nResultados completos de la encuesta:")
        # Recorro el diccionario de las respuestas
        for nombre, respuestas in self.respuestas.items():
            print(f"\n Estudiante: {nombre}")
            # Recorro las respuestas enviadas por el estudiante 
            for i, respuesta in enumerate(respuestas):
                #Imprimo la pregunta con la respuesta del estudiante
                print(f"  {self.preguntas[i]} R: {respuesta}")


    def resumen(self):
        print("\n Resumen de respuestas:\n")
        # Recorre las preguntas
        for i, pregunta in enumerate(self.preguntas):
            # Creo el diccionario para contar cuantas respuestas iguales hay en una pregunta
            conteo = {}
            # Recorro respuestas de los estudiantes 
            for respuestas in self.respuestas.values():
                r = respuestas[i]
                conteo[r] = conteo.get(r, 0) + 1
            # Imprime el conteo de las preguntas 
            print(f"{pregunta}")
            for opcion, cantidad in conteo.items():
                print(f"  {opcion}: {cantidad} voto(s)")
           

if __name__ == "__main__":
    # 3 PREGUNTAS
    preguntas = [
        "¿Qué tema prefieres para el proyecto? ",
        "¿Sabes trabajar en equipo? (Sí/No) ",
        "¿Conoces alguna librería de Python? (Sí/No) "
    ]

    encuesta = Encuesta(preguntas)

    print("=== Encuesta de Ideas de Proyecto ===")
    # Recolectar respuestas de al menos 10 estudiantes
    for i in range(2):  
        nombre = input("\nIngresa tu nombre: ")
        respuestas = []
        # Recorre las preguntas 
        for p in preguntas:
            r = input(p)
            respuestas.append(r)
        encuesta.agregar_respuesta(nombre, respuestas)

    encuesta.mostrar_resultados()
    encuesta.resumen()
