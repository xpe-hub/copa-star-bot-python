#!/bin/bash

# Script para limpiar ramas innecesarias

echo "🧹 Limpiando ramas del repositorio..."

# Configurar git para evitar prompts interactivos
export GIT_TERMINAL_PROMPT=0

# Verificar rama actual
echo "📍 Rama actual:"
git rev-parse --abbrev-ref HEAD

# Eliminar rama master local si existe
echo "🗑️ Eliminando rama master local..."
git branch -d master 2>/dev/null || echo "Rama master local no encontrada o no se pudo eliminar"

# Eliminar rama master remota si existe  
echo "🗑️ Eliminando rama master remota..."
git push origin --delete master 2>/dev/null || echo "Rama master remota no encontrada o no se pudo eliminar"

# Eliminar rama temporal
echo "🗑️ Eliminando rama temporal..."
git branch -d design-fixes-realtrem 2>/dev/null || echo "Rama temporal no encontrada o no se pudo eliminar"

# Mostrar ramas finales
echo "📋 Ramas finales:"
git branch -a

echo "✅ Limpieza completada!"