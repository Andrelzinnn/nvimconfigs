import os
import shutil


def move_nvim_to_appdata():
    appdata_nvim_path = os.path.join(os.environ["LOCALAPPDATA"], "nvim")

    current_nvim_path = os.getcwd()

    if os.path.exists(appdata_nvim_path):
        print(f"A pasta {appdata_nvim_path} já existe. Renomeando para nvim.bak...")
        shutil.move(appdata_nvim_path, appdata_nvim_path + ".bak")

    print(f"Criando a pasta {appdata_nvim_path} no AppData...")
    os.makedirs(appdata_nvim_path, exist_ok=True)

    lua_path = os.path.join(current_nvim_path, "lua")
    scripts_path = os.path.join(current_nvim_path, "scripts")

    if os.path.exists(lua_path):
        print(f"Mover {lua_path} para {appdata_nvim_path}...")
        shutil.move(lua_path, os.path.join(appdata_nvim_path, "lua"))
    else:
        print(f"A pasta {lua_path} não foi encontrada.")

    if os.path.exists(scripts_path):
        print(f"Mover {scripts_path} para {appdata_nvim_path}...")
        shutil.move(scripts_path, os.path.join(appdata_nvim_path, "scripts"))
    else:
        print(f"A pasta {scripts_path} não foi encontrada.")

    init_lua_path = os.path.join(current_nvim_path, "init.lua")
    if os.path.exists(init_lua_path):
        print(f"Mover {init_lua_path} para {appdata_nvim_path}...")
        shutil.move(init_lua_path, os.path.join(appdata_nvim_path, "init.lua"))
    else:
        print("O arquivo init.lua não foi encontrado.")

    print("Movimentação concluída.")


def main():
    move_nvim_to_appdata()
    print("Setup de arquivos do Neovim completo.")


if __name__ == "__main__":
    main()
