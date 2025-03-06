import os
import urllib.request
import zipfile
import shutil

# Nome da fonte
font_name = "0xProto"
nerd_font_url = f"https://github.com/ryanoasis/nerd-fonts/releases/download/v3.3.0/{font_name}.zip"

# Diretórios
fonts_dir = os.path.join(os.environ["WINDIR"], "Fonts")
home = os.path.expanduser("~")
download_dir = os.path.join(home, "Downloads")
kitty_config_dir = os.path.join(home, ".config", "kitty")
kitty_conf_path = os.path.join(kitty_config_dir, "kitty.conf")

# Caminho do arquivo ZIP da fonte
font_zip_path = os.path.join(download_dir, f"{font_name}.zip")

# Baixando a fonte
print(f"Baixando fonte: {font_name}")
urllib.request.urlretrieve(nerd_font_url, font_zip_path)

# Extraindo a fonte
print("Extraindo a fonte...")
with zipfile.ZipFile(font_zip_path, "r") as zip_ref:
    zip_ref.extractall(download_dir)

# Movendo a fonte para a pasta de fontes do Windows
extracted_dir = os.path.join(download_dir, font_name)
for file in os.listdir(extracted_dir):
    if file.endswith(".ttf"):
        font_path = os.path.join(extracted_dir, file)
        shutil.move(font_path, os.path.join(fonts_dir, file))

# Configuração do Kitty
kitty_config = f"""# Configuração do Kitty
font_family                 {font_name} Nerd Font
font_size                   12
bold_font                   auto
italic_font                 auto
bold_italic_font            auto
remember_window_size        no
initial_window_width        950
initial_window_height       500
cursor_blink_interval       0.5
cursor_stop_blinking_after  1
scrollback_lines            2000
wheel_scroll_min_lines      1
enable_audio_bell           no
window_padding_width        10
hide_window_decorations     yes
background_opacity          0.7
dynamic_background_opacity  yes
confirm_os_window_close     0
selection_foreground        none
selection_background        none
"""

# Criando diretório do Kitty se não existir
os.makedirs(kitty_config_dir, exist_ok=True)

# Escrevendo o arquivo de configuração do Kitty
with open(kitty_conf_path, "w") as conf_file:
    conf_file.write(kitty_config)

print(f"Configuração do Kitty aplicada em: {kitty_conf_path}")

