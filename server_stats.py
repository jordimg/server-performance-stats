import psutil
import platform
import time

def get_system_info():
    """Obtiene información básica del sistema"""
    info = {
        "Sistema Operativo": platform.system(),
        "Versión": platform.version(),
        "Arquitectura": platform.architecture()[0],
        "Procesador": platform.processor(),
        "Núcleos físicos": psutil.cpu_count(logical=False),
        "Núcleos lógicos": psutil.cpu_count(logical=True),
    }
    return info

def get_cpu_usage():
    """Obtiene el uso de CPU en porcentaje"""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Obtiene el uso de memoria RAM"""
    mem = psutil.virtual_memory()
    return {
        "Total": f"{mem.total / (1024**3):.2f} GB",
        "Disponible": f"{mem.available / (1024**3):.2f} GB",
        "Uso": f"{mem.percent}%",
    }

def get_disk_usage():
    """Obtiene el uso de disco"""
    disk = psutil.disk_usage("/")
    return {
        "Total": f"{disk.total / (1024**3):.2f} GB",
        "Usado": f"{disk.used / (1024**3):.2f} GB",
        "Libre": f"{disk.free / (1024**3):.2f} GB",
        "Uso": f"{disk.percent}%",
    }

def main():
    """Función principal para mostrar las estadísticas"""
    print("\n--- Información del Sistema ---")
    for key, value in get_system_info().items():
        print(f"{key}: {value}")
    
    print("\n--- Estadísticas del Servidor ---")
    print(f"Uso de CPU: {get_cpu_usage()}%")
    
    print("\n--- Memoria RAM ---")
    for key, value in get_memory_usage().items():
        print(f"{key}: {value}")

    print("\n--- Disco ---")
    for key, value in get_disk_usage().items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    while True:
        main()
        print("\nActualizando en 5 segundos...\n")
        time.sleep(5)
