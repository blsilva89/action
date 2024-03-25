import os
import sys

def verificar_arquivos_python(diretorio):
    # Lista todos os arquivos no diretório
    arquivos = os.listdir(diretorio)
    
    # Verifica se todos os arquivos são scripts Python
    for arquivo in arquivos:
        if not arquivo.endswith('.py'):
            print(f'O arquivo {arquivo} não é um script Python.')
            return False
    
    return True

if __name__ == "__main__":
    diretorio = '.'  # Diretório atual, você pode modificar conforme necessário
    if not verificar_arquivos_python(diretorio):
        # Se algum arquivo não for um script Python, falha a ação
        sys.exit(1)
