# Constantes para las calificaciones
CALIFICACION_SOBRESALIENTE = 9
CALIFICACION_NOTABLE = 7
CALIFICACION_APROBADO = 5


def calcular_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3


def obtener_calificacion(media):
    if media >= CALIFICACION_SOBRESALIENTE:
        return "Sobresaliente"
    elif media >= CALIFICACION_NOTABLE:
        return "Notable"
    elif media >= CALIFICACION_APROBADO:
        return "Aprobado"
    else:
        return "Suspenso"


def mostrar_alumno(nombre, nota1, nota2, nota3):
    print(f"Alumno: {nombre}")
    print(f"Nota 1: {nota1}")
    print(f"Nota 2: {nota2}")
    print(f"Nota 3: {nota3}")

    media = calcular_media(nota1, nota2, nota3)
    calificacion = obtener_calificacion(media)

    print(f"Media: {media:.2f}")
    print(f"Calificación: {calificacion}")
    print("-" * 22)


def main():
    alumnos = [
        ("Ana García", 8, 7, 9),
        ("Luis Pérez", 4, 5, 3),
        ("Marta Gómez", 6, 7, 5)
    ]
    for alumno in alumnos:
        mostrar_alumno(*alumno)


main()