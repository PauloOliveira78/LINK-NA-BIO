#!/usr/bin/env python
"""Utilitário de linha de comando do Django para tarefas administrativas."""
import os
import sys

def main():
    """Executa tarefas administrativas."""
    # Define a variável de ambiente para as configurações do Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        # Importa e executa o comando de linha de comando do Django
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # Levanta um erro se o Django não estiver instalado ou se o ambiente virtual não estiver ativado
        raise ImportError(
            "Não foi possível importar o Django. Você tem certeza de que ele está instalado e "
            "disponível na sua variável de ambiente PYTHONPATH? Você ativou o ambiente virtual?"
        ) from exc
    # Executa o comando de linha de comando do Django com os argumentos fornecidos
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    # Chama a função main se o script for executado diretamente
    main()
