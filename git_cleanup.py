import subprocess
import os

os.chdir('/workspace')

print("=== LIMPIEZA DE RAMAS ===")
print("Directorio actual:", os.getcwd())

# Verificar estado
try:
    result = subprocess.run(['git', 'rev-parse', '--abbrev-ref', 'HEAD'], capture_output=True, text=True, timeout=10)
    print("Rama actual:", result.stdout.strip())
except Exception as e:
    print("Error obteniendo rama:", e)

# Listar ramas
try:
    result = subprocess.run(['git', 'branch'], capture_output=True, text=True, timeout=10)
    print("Ramas locales:", result.stdout.strip())
except Exception as e:
    print("Error listando ramas:", e)

# Eliminar master local
try:
    result = subprocess.run(['git', 'branch', '-D', 'master'], capture_output=True, text=True, timeout=10)
    print("Eliminar master local:", result.stdout.strip() if result.stdout.strip() else "Sin errores")
except Exception as e:
    print("Error eliminando master local:", e)

# Eliminar master remota
try:
    result = subprocess.run(['git', 'push', 'origin', '--delete', 'master'], capture_output=True, text=True, timeout=10)
    print("Eliminar master remota:", result.stdout.strip() if result.stdout.strip() else "Sin errores")
except Exception as e:
    print("Error eliminando master remota:", e)

# Eliminar rama temporal
try:
    result = subprocess.run(['git', 'branch', '-D', 'design-fixes-realtrem'], capture_output=True, text=True, timeout=10)
    print("Eliminar rama temporal:", result.stdout.strip() if result.stdout.strip() else "Sin errores")
except Exception as e:
    print("Error eliminando rama temporal:", e)

print("=== LIMPIEZA COMPLETADA ===")