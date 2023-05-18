from view.launcher_tkinter import LauncherTKInter
from controller.gpoController.gpo_controller import GpoController

def main():
    gpo_controller = GpoController()
    launcher = LauncherTKInter(gpo_controller)
    launcher.run()

if __name__ == "__main__":
    main()
