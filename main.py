from tqdm import tqdm
tqdm.monitor_interval = 0
from view.launcher_tkinter import LauncherTKInter
from controller.gpoController.gpo_controller import GpoController

def main():
    gpo_controller = GpoController()
    launcher = LauncherTKInter(gpo_controller)
    launcher.janela.mainloop()

if __name__ == "__main__":
    main()
