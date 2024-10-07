import time

def loading_animation(duration, msg):
    """
    Muestra una animación de carga en la consola durante un tiempo específico.

    Parámetros:
    ----------
    duration : int
        Duración de la animación en segundos.
    msg : str
        Mensaje que se mostrará junto a la animación de carga.
    
    Ejemplo:
    --------
    loading_animation(5, "Cargando")
    """
    end_time = time.time() + duration
    loading_text = msg
    
    while time.time() < end_time:
        for i in range(4):  

            dots = '.' * i

            print(f"\r{loading_text}{dots}", end='', flush=True)
            time.sleep(0.5) 
        print("Listo!")