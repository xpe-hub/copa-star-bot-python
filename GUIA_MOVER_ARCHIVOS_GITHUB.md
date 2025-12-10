# 🎯 GUÍA: Mover Archivos a Raíz del Repositorio

## ✅ Archivos ya copiados a la raíz:
- ✅ `bot.py` (bot principal)
- ✅ `config.py` (configuración RealTREM)
- ✅ `requirements.txt` (dependencias)

## 🚀 Pasos para GitHub:

### Paso 1: Acceder a tu repositorio
1. Ve a: https://github.com/xpe-hub/copa-star-bot-final
2. Haz clic en el archivo `bot.py`

### Paso 2: Mover archivos a raíz
**Para cada archivo (`bot.py`, `config.py`, `requirements.txt`):**

1. **Abrir el archivo** en la carpeta `copa-star-bot-python/`
2. **Seleccionar todo el contenido** (Ctrl+A)
3. **Copiar** (Ctrl+C)
4. **Crear nuevo archivo en la raíz**:
   - Clic en "Add file" → "Create new file"
   - Nombre: `bot.py` (en la raíz, NO en carpeta)
   - Pegar contenido (Ctrl+V)
   - Commit message: "Move bot.py to root"
   - Commit changes

5. **Repetir** para `config.py` y `requirements.txt`

### Paso 3: Eliminar archivos de la subcarpeta (opcional)
1. Entrar a carpeta `copa-star-bot-python/`
2. Eliminar cada archivo (si quieres limpiar)

### Paso 4: Railway se actualiza automáticamente
- Railway detectará los cambios
- Bot se ejecutará desde la raíz: `python bot.py`
- No necesitarás Root Directory

## 🎯 Resultado Final:
```
repositorio-raíz/
├── bot.py          ← AQUÍ
├── config.py       ← AQUÍ  
├── requirements.txt ← AQUÍ
├── README.md
└── copa-star-bot-python/ (carpeta, opcional eliminar)
```

**¿Prefieres que te ayude con algún paso específico de GitHub?**