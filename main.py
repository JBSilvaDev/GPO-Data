from tqdm import tqdm
import os
os.environ["WDM_LOG_LEVEL"] = "0"
os.environ["WDM_HIDE_OUTPUT"] = "true"
tqdm.monitor_interval = 0
from view.launcher_tkinter import LauncherTKInter
from controller.gpoController.gpo_controller import GpoController

def main():
    try:
        gpo_controller = GpoController()
        launcher = LauncherTKInter(gpo_controller)
        launcher.janela.mainloop()
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    main()
