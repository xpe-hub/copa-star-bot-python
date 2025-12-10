#!/usr/bin/env python3
import subprocess
import sys
import os

def run_command(cmd):
    """Ejecuta un comando y devuelve el resultado"""
    try:
        print(f"🔧 Ejecutando: {cmd}")
        result = subprocess.run(
            cmd, 
            shell=True, 
            capture_output=True, 
            text=True, 
            timeout=30,
            env={**os.environ, 'GIT_TERMINAL_PROMPT': '0'}
        )
        print(f"✅ Salida: {result.stdout.strip()}")
        if result.stderr:
            print(f"⚠️ Error: {result.stderr.strip()}")
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        print(f"⏰ Timeout: {cmd}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("🧹 Iniciando limpieza de ramas...")
    
    # Cambiar al directorio del repositorio
    os.chdir('/workspace')
    
    # 1. Verificar rama actual
    print("\n📍 Verificando rama actual...")
    run_command('git rev-parse --abbrev-ref HEAD')
    
    # 2. Listar todas las ramas
    print("\n📋 Ramas locales:")
    run_command('git branch')
    
    print("\n📋 Ramas remotas:")
    run_command('git branch -r')
    
    # 3. Eliminar rama master local
    print("\n🗑️ Eliminando rama master local...")
    run_command('git branch -D master 2>/dev/null || echo "Master local no encontrada"')
    
    # 4. Eliminar rama master remota
    print("\n🗑️ Eliminando rama master remota...")
    run_command('git push origin --delete master 2>/dev/null || echo "Master remota no encontrada"')
    
    # 5. Eliminar rama temporal
    print("\n🗑️ Eliminando rama temporal...")
    run_command('git branch -D design-fixes-realtrem 2>/dev/null || echo "Rama temporal no encontrada"')
    
    # 6. Verificar estado final
    print("\n✅ Estado final:")
    run_command('git branch -a')
    
    print("\n🎉 Limpieza completada!")

if __name__ == "__main__":
    main()