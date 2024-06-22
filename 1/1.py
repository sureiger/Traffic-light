import tkinter as tk
from threading import Thread
import time


class TrafficLightApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Управление Светофорами")

        # Настройка меток для отображения животных
        self.head1 = tk.Label(
            root, text='Овцы', font=('Helvetica', 18),)
        self.head1.grid(row=0, column=0)

        self.head2 = tk.Label(
            root, text='Коровы', font=('Helvetica', 18),)
        self.head2.grid(row=1, column=0)
        
        # Настройка меток для отображения состояний светофоров
        self.label1 = tk.Label(
            root, text='Светофор', font=('Helvetica', 18),)
        self.label1.grid(row=0, column=1)

        self.label2 = tk.Label(
            root, text='Светофор', font=('Helvetica', 18))
        self.label2.grid(row=1, column=1)

        # Запуск потока управления светофорами
        self.thread = Thread(target=self.manage_lights)
        self.thread.start()

    def manage_lights(self):
        while True:

            self.label1.config(bg='green')
            self.label2.config(bg='red')
            self.update_gui()
            time.sleep(15)

            self.label1.config(bg='yellow')
            self.update_gui()
            time.sleep(5)

            self.label1.config(bg='red')
            self.label2.config(bg='green')
            self.update_gui()
            time.sleep(15)

            self.label2.config(bg='yellow')
            self.update_gui()
            time.sleep(5)

    def update_gui(self):
        # Обновление GUI
        self.root.update_idletasks()
        self.root.update()


# Создание окна приложения
root = tk.Tk()
app = TrafficLightApp(root)
root.mainloop()
