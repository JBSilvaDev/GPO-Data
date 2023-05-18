from tqdm import tqdm
import os
os.environ["WDM_LOG_LEVEL"] = "0"
os.environ["WDM_HIDE_OUTPUT"] = "true"
tqdm.monitor_interval = 0
import traceback
from view.launcher_tkinter import LauncherTKInter
from controller.gpoController.gpo_controller import GpoController

def main():
    try:
        gpo_controller = GpoController()
        launcher = LauncherTKInter(gpo_controller)
        launcher.janela.mainloop()
    except Exception:
        with open("error_log.txt", "w") as f:
          traceback.print_exc(file=f)

if __name__ == "__main__":
    
    main()
