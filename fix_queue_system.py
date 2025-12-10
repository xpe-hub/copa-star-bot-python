# 🔧 SOLUCIÓN PARA SISTEMA DE FILAS INDIVIDUAL
# 
# PROBLEMA ACTUAL: 
# - queues = {} es global para todo el servidor
# - Cuando User A crea fila 2v2, User B no puede crear otra
# - Sistema bloquea filas del mismo modo para usuarios diferentes
#
# SOLUCIÓN:
# - Cada usuario debe tener su propia fila
# - Key: "user_id_game_mode" en lugar de solo "game_mode"
# - Separar completamente por usuario

# CAMBIOS NECESARIOS EN bot.py:

# 1. CAMBIAR la lógica de verificación
# ANTES:
# if game_mode in queues and not queues.get(f'{game_mode}_closed'):

# DESPUÉS:
# user_queue_key = f"{ctx.author.id}_{game_mode}"
# if user_queue_key in queues and not queues.get(f'{user_queue_key}_closed'):

# 2. CAMBIAR la creación de colas
# ANTES:
# queues[game_mode] = {'players': [], 'teams': [[], []]}

# DESPUÉS:
# queues[user_queue_key] = {'players': [], 'teams': [[], []]}

# 3. CAMBIAR la gestión de mensajes
# ANTES:
# queue_messages[game_mode] = queue_message.id

# DESPUÉS:
# queue_messages[user_queue_key] = queue_message.id

# 4. ACTUALIZAR todas las funciones que usan queues para usar user_queue_key

print("✅ Solución definida: Sistema de filas individual por usuario")
print("🎯 Cada usuario puede tener su propia fila 2v2, 1v1, etc.")
print("🔓 No más bloqueos entre usuarios diferentes")