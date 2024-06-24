import tkinter as tk
from threading import Thread
import time


class TrafficLightApp:
    def init(self, root):
        self.root = root
        self.root.title("Управление Светофорами")
        self.ovci_on = False
        self.cow_on = False

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

        # Инициализация состояний заслонки
        self.state1 = tk.StringVar()
        self.state2 = tk.StringVar()

        # Настройка меток для отображения заслонки
        self.damper1 = tk.Label(root, textvariable=self.state1,
                                font=('Helvetica', 18))
        self.damper1.grid(row=0, column=2)

        self.damper2 = tk.Label(root, textvariable=self.state2,
                                font=('Helvetica', 18))
        self.damper2.grid(row=1, column=2)

        # Инициализация состояний заслонки
        self.stateB1 = tk.StringVar()
        self.stateB2 = tk.StringVar()

        # Настройка кнопок запроса
        def switch_ovci():
            self.ovci_on = True
            self.update_lights()

        def switch_cow():
            self.cow_on = True
            self.update_lights()
        self.btn1 = tk.Button(
            root, textvariable=self.stateB1, font=('Helvetica', 18),
            command=switch_ovci)
        self.btn1.grid(row=0, column=3)

        self.btn2 = tk.Button(
            root, textvariable=self.stateB2, font=('Helvetica', 18),
            command=switch_cow)
        self.btn2.grid(row=1, column=3)

        # Запуск потока управления светофорами
        self.thread = Thread(target=self.manage_lights)
        self.thread.start()

    def update_lights(self):
        if self.ovci_on == True:

            self.stateB1.set("Кнопка нажата")
            self.btn1['state'] = 'disabled'
            self.btn2['state'] = 'normal'
            self.stateB2.set("Кнопка не нажата")

            self.label2.config(bg='yellow')
            self.update_gui()
            time.sleep(5)

            self.state1.set("Заслонка открыта")
            self.state2.set("Заслонка закрыта")

            self.label1.config(bg='green')
            self.label2.config(bg='red')
            self.update_gui()
            # time.sleep(10)

        if self.cow_on == True:

            self.stateB1.set("Кнопка не нажата")
            self.stateB2.set("Кнопка нажата")
            self.btn2['state'] = 'disabled'
            self.btn1['state'] = 'normal'

            self.label1.config(bg='yellow')
            self.update_gui()
            time.sleep(5)

            self.state1.set("Заслонка закрыта")
            self.state2.set("Заслонка открыта")

            self.label1.config(bg='red')
            self.label2.config(bg='green')
            self.update_gui()
            # time.sleep(10)
        # self.ovci_on = self.cow_on = False

    def manage_lights(self):
        while True:

            self.stateB1.set("Кнопка нажата")
            self.btn1['state'] = 'disabled'
            self.btn2['state'] = 'normal'
            self.stateB2.set("Кнопка не нажата")

            self.state1.set("Заслонка открыта")
            self.state2.set("Заслонка закрыта")

            self.label1.config(bg='green')
            self.label2.config(bg='red')
            self.update_gui()
            time.sleep(10)

    def update_gui(self):
        # Обновление GUI
        self.root.update_idletasks()
        self.root.update()


# Создание окна приложения
root = tk.Tk()
app = TrafficLightApp(root)
root.mainloop()
