import tkinter as tk

class LauncherTKInter:
    def __init__(self, gpo_controller):
        self.icon = r"C:\Users\julianobs\Desktop\gestao_porto\icon\portoPNG.ico"
        self.gpo_controller = gpo_controller
        self.janela = tk.Tk()
        self.janela.maxsize(900, 600)
        self.janela.title("Consulta GPO")
        self.janela.iconbitmap(self.icon)
        
        self.labelPec = tk.Label(self.janela, text="Informe a PEC aqui!", font='Arial 10')
        self.labelPec.grid(row=0, column=1, padx=5, pady=10)
        self.pecNum = tk.Entry(self.janela, width=20, font='Arial 15', justify='center')
        self.pecNum.grid(row=1, column=1)
        
        self.textInfoPrVao = tk.StringVar()
        self.textInfoPrVao.set("Informe a PEC para consulta")
        
        self.updateText = tk.Entry(self.janela, textvariable=self.textInfoPrVao, width=30, font='Arial 15', justify='center', state='readonly')
        self.updateText.grid(row=5, column=1, padx=5, pady=10)
        
        self.btn = tk.Button(self.janela, text="Buscar PR/Vão", command=self.sendPecToGPO, bd=5, height=2, width=20, font='Arial 10')
        self.btn.grid(row=7, column=1, padx=5, pady=10)
        
        self.janela.mainloop()
        self.gpo_controller.killChrome()
        
    def sendPecToGPO(self):
        self.gpo_controller.getPrVao(self.pecNum.get(), self.textInfoPrVao)
