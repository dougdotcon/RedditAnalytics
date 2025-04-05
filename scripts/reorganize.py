#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def create_directory_structure():
    """Cria a estrutura de diretórios do projeto."""
    directories = [
        # Código fonte
        "src/analysis",
        "src/data",
        "src/visualization",
        "src/utils",
        
        # Testes
        "tests/test_analysis",
        "tests/test_data",
        "tests/test_visualization",
        
        # Dados
        "data/raw",
        "data/processed",
        "data/external",
        
        # Saída
        "output/graphs",
        "output/reports",
        "output/exports",
        
        # Documentação
        "docs/api",
        "docs/guides",
        "docs/examples",
        
        # Outros
        "scripts",
        "requirements",
        ".github/workflows"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        # Cria __init__.py para diretórios Python
        if directory.startswith(("src/", "tests/")):
            init_file = Path(directory) / "__init__.py"
            init_file.touch()

def safe_move(source, dest):
    """Move um arquivo de forma segura, verificando existência e criando diretórios."""
    try:
        if os.path.exists(source):
            dest_dir = os.path.dirname(dest)
            if dest_dir:  # Verifica se o diretório de destino não está vazio
                os.makedirs(dest_dir, exist_ok=True)
            shutil.move(source, dest)
            print(f"Movido: {source} -> {dest}")
        else:
            print(f"Arquivo não encontrado: {source}")
    except Exception as e:
        print(f"Erro ao mover {source}: {str(e)}")

def move_files():
    """Move os arquivos para suas novas localizações."""
    file_mappings = {
        # Arquivos de análise
        "top_subs.py": "src/analysis/top_subs.py",
        "analyze_output.py": "src/analysis/metrics.py",
        
        # Arquivos de dados
        "parseZst.py": "src/data/parser.py",
        "transplant.py": "src/data/cleaner.py",
        
        # Arquivos de visualização
        "graph.py": "src/visualization/graphs.py",
        "image_tools.py": "src/visualization/image_tools.py",
        
        # Utilitários
        "tools.py": "src/utils/tools.py",
        
        # Script principal
        "orchestrator.py": "orchestrator.py"
    }
    
    # Move os arquivos
    for source, dest in file_mappings.items():
        safe_move(source, dest)

def move_data_files():
    """Move arquivos de dados e saída para os diretórios apropriados."""
    try:
        # Move arquivos de comentários
        if os.path.exists("comment_files"):
            for file in os.listdir("comment_files"):
                source = os.path.join("comment_files", file)
                dest = os.path.join("data/raw", file)
                safe_move(source, dest)
            if os.path.exists("comment_files"):
                os.rmdir("comment_files")
            print("Arquivos de comentários movidos para data/raw/")

        # Move arquivos de gráficos
        if os.path.exists("graph_output"):
            for file in os.listdir("graph_output"):
                source = os.path.join("graph_output", file)
                dest = os.path.join("output/graphs", file)
                safe_move(source, dest)
            if os.path.exists("graph_output"):
                os.rmdir("graph_output")
            print("Arquivos de gráficos movidos para output/graphs/")
    except Exception as e:
        print(f"Erro ao mover arquivos de dados: {str(e)}")

def create_requirement_files():
    """Cria arquivos de requisitos separados."""
    requirements = {
        "requirements/base.txt": [
            "lxml",
            "requests",
            "plotly",
            "pandas",
            "Pillow"
        ],
        "requirements/dev.txt": [
            "-r base.txt",
            "pytest",
            "black",
            "flake8",
            "mypy"
        ],
        "requirements/test.txt": [
            "-r base.txt",
            "pytest",
            "pytest-cov"
        ]
    }
    
    try:
        for file_path, packages in requirements.items():
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, "w") as f:
                f.write("\n".join(packages))
            print(f"Criado: {file_path}")

        # Cria link simbólico requirements.txt -> requirements/base.txt
        if os.path.exists("requirements.txt"):
            os.remove("requirements.txt")
        shutil.copy2("requirements/base.txt", "requirements.txt")
        print("requirements.txt atualizado")
    except Exception as e:
        print(f"Erro ao criar arquivos de requisitos: {str(e)}")

def main():
    """Função principal para reorganizar o projeto."""
    try:
        print("Iniciando reorganização do projeto...")
        
        # Cria nova estrutura de diretórios
        create_directory_structure()
        print("Estrutura de diretórios criada.")
        
        # Move os arquivos
        move_files()
        print("Arquivos principais movidos.")
        
        # Move arquivos de dados
        move_data_files()
        print("Arquivos de dados movidos.")
        
        # Cria arquivos de requisitos
        create_requirement_files()
        print("Arquivos de requisitos criados.")
        
        print("\nReorganização concluída!")
        print("\nPróximos passos recomendados:")
        print("1. Verifique se todos os arquivos foram movidos corretamente")
        print("2. Atualize os imports nos arquivos Python")
        print("3. Execute os testes para garantir que tudo continua funcionando")
        print("4. Atualize a documentação conforme necessário")
    except Exception as e:
        print(f"\nErro durante a reorganização: {str(e)}")
        print("Por favor, verifique os logs acima para mais detalhes.")

if __name__ == "__main__":
    main() 