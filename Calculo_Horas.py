from typing import List, Union

def calcular_y_clasificar_jornadas(matriz_horas: List[List[Union[str, int]]]) -> None:
    # Iteramos sobre cada recurso en la matriz
    for registro in matriz_horas:
        nombre: str = str(registro[0])
        
        # Extraemos solo los valores numéricos (horas) usando slicing y garantizamos que sean enteros
        horas_trabajadas: List[int] = [int(h) for h in registro[1:]] 
        total_horas: int = sum(horas_trabajadas)
        
        # Clasificamos la jornada según el umbral de 40 horas
        estado: str = "Sobretiempo" if total_horas > 40 else "Horario Estándar"
        
        print(f"Recurso: {nombre} | Total: {total_horas}h | Clasificación: {estado}")

def main() -> None:
    # Matriz con 4 recursos y horas trabajadas de lunes a viernes
    matriz_equipo: List[List[Union[str, int]]] = [
        ["Miguel", 8, 8, 8, 8, 8],
        ["Bibiana", 9, 8, 9, 9, 8],
        ["Juan Esteban", 8, 8, 8, 8, 5],
        ["Camilo", 10, 9, 9, 8, 8]
    ]
    
    print("--- Reporte Semanal de Horas ---")
    calcular_y_clasificar_jornadas(matriz_equipo)

if __name__ == "__main__":
    main()