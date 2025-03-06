import os
import subprocess
import shutil


def is_installed(program):
    return shutil.which(program) is not None


def install_if_missing(program, install_command):
    if is_installed(program):
        print(f"{program} já está instalado.")
    else:
        print(f"Instalando {program}...")
        subprocess.run(install_command, shell=True)


def install_gcc():
    if is_installed("gcc"):
        print("GCC já está instalado.")
    else:
        print("Instalando MSYS2 para obter GCC...")
        subprocess.run("winget install -e --id MSYS2.MSYS2", shell=True)

        msys2_path = r"C:\msys64\usr\bin\mintty.exe"
        if os.path.exists(msys2_path):
            print("Instalando GCC via pacman...")
            subprocess.run(
                f'"{msys2_path}" -i /msys2.ico /usr/bin/bash --login -c "pacman -S --noconfirm mingw-w64-x86_64-gcc"',
                shell=True,
            )
            print("GCC instalado com sucesso.")
        else:
            print("Erro: MSYS2 não foi encontrado. Tente reiniciar o sistema e rodar novamente.")


install_if_missing("fd", "winget install --id Shark. fd")
install_if_missing("rg", "winget install --id BurntSushi.ripgrep")
install_if_missing("fzf", "winget install --id junegunn.fzf")
install_gcc()

