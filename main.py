import os
import signal
import threading
import tkinter

os.system("call env/Scripts/activate.bat")

class ServerThread(threading.Thread):
    def run(self):
        os.system("python manage.py runserver")

def launch_server():
    server_launcher = ServerThread()
    server_launcher.start()
    os.system("start firefox 127.0.0.1:8000")

def close():
    os.kill(os.getpid(), signal.SIGINT)
    raise KeyboardInterrupt

def main():
    fen = tkinter.Tk()
    fen.title("Locatia")
    fen.resizable(False, False)
    tkinter.Label(fen, text="Bienvenue Sur Locatia. Appuyez\n sur le boutton ci dessous pour\n lancer l'application").pack()
    tkinter.Button(fen, text="Lancer l'application", command=launch_server).pack()
    tkinter.Button(fen, text="Fermer", command=close).pack()
    fen.mainloop()

signal.signal(signal.SIGINT, close)

if __name__ == '__main__':
    main()