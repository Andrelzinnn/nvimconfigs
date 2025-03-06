import subprocess


def run_script(script_name):
    try:
        print(f"Iniciando a execução do script: {script_name}")
        subprocess.run(["python", script_name], check=True)
        print(f"{script_name} executado com sucesso.")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o script {script_name}: {e}")
    


def main():
    print("Iniciando o setup do Kitty...")
    run_script("kitty_setup.py")
    print("Setup do Kitty concluído.")

    print("Iniciando a instalação das dependências...")
    run_script("dependencies_install.py")
    print("Instalação das dependências concluída.")


if __name__ == "__main__":
    main()
