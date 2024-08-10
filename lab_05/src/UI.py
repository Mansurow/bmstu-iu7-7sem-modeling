import re

import tkinter as tk
from tkinter import ttk

from InfoSystem import InfoSystem
from Distributions import UniformDistribution

class App(tk.Tk):
    
    spinbox_options = {
        "from_": 1,
        "to": 10_000, 
        "increment": 1,
        "wrap": True, 
        "justify": "center",
    }
    
    label_options = {
        "text": str(),
        "font": ("Verdana", 10),
        "foreground": "black",
        "textvariable": None,
        "wraplength": 550
    }
    
    grid_options = {
        "row": 0,
        "column": 0,
        "rowspan": 1,
        "columnspan": 1,
        "padx": 5,
        "pady": 5,
        "sticky": "w"
    }
    
    def __init__(self) -> None:
        super().__init__()
        
        style = ttk.Style()
        style.configure("Bold.TLabel", font=("Verdana", 12, "bold"))
        
        self.title("Лабораторная работа №5. Моделирование работы информационного центра")
        self.resizable(False, False)
        
        self.result = tk.StringVar()
        
        self.delta_t = tk.DoubleVar(value=0.01)
        self.request_amount = tk.IntVar(value=300)
        
        # for generator
        self.generator_lower_bound = tk.DoubleVar(value=8.00)
        self.generator_upper_bound = tk.DoubleVar(value=12.00)
        
        # for operators
        self.operator_1_lower_bound = tk.DoubleVar(value=15)
        self.operator_1_upper_bound = tk.DoubleVar(value=25)
        self.operator_2_lower_bound = tk.DoubleVar(value=30)
        self.operator_2_upper_bound = tk.DoubleVar(value=50)
        self.operator_3_lower_bound = tk.DoubleVar(value=20)
        self.operator_3_upper_bound = tk.DoubleVar(value=60)
        
        # for computers
        self.computer_1_processing_time = tk.DoubleVar(value=15)
        self.computer_2_processing_time = tk.DoubleVar(value=30)
        
        self.float_key_validation = (self.register(self.is_valid_float), "%P")
        self.positive_int_key_validation = (self.register(self.is_valid_positive_int), "%P")
        
        self.add_main_part()
        
        self.add_generator_label_frame()
        
        self.add_operator_label_frame()

        self.add_computer_label_frame()
        
        self.add_simulate_button()
        
        self.add_result_label()
        
    
    def add_main_part(self) -> None:
        self.entries = []
        labels = ("временной шаг:", "количество заявок:")
        for row, label in enumerate(labels):
            self.grid_options["row"] = row
            self.grid_options["column"] = 0
            self.label_options["text"] = label
            self.add_label(self, self.label_options, self.grid_options)
        
        self.grid_options["row"] = 1
        self.grid_options["column"] = 1
        request_amount_spinbox = ttk.Spinbox(
            self,
            textvariable=self.request_amount,
            validate="key",
            validatecommand=self.positive_int_key_validation,
            **self.spinbox_options
        )
        request_amount_spinbox.grid(self.grid_options)
        
        self.grid_options["row"] = 0
        self.spinbox_options["to"] = 1.00
        self.spinbox_options["from_"] = 0.00
        self.spinbox_options["increment"] = 0.01
        delta_t_spinbox = ttk.Spinbox(
            self,
            textvariable=self.delta_t,
            validate="key",
            validatecommand=self.float_key_validation,
            **self.spinbox_options
        )
        delta_t_spinbox.grid(self.grid_options)
        delta_t_spinbox.focus()


    def add_generator_label_frame(self) -> None:
        self.grid_options["row"] = 0
        self.grid_options["rowspan"] = 3
        self.grid_options["column"] = 2
        
        labelframe = ttk.LabelFrame(self)
        labelframe["labelwidget"] = ttk.Label(text="Параметры генератора", style="Bold.TLabel")
        labelframe.grid(self.grid_options)
        
        self.grid_options["column"] = 0
        self.grid_options["rowspan"] = 1
        self.grid_options["columnspan"] = 2
        self.grid_options["sticky"] = "ns"
        self.label_options["text"] = "равномерное распределение"
        self.add_label(labelframe, self.label_options, self.grid_options)
        
        labels = ("нижняя", "верхняя")
        
        self.grid_options["sticky"] = "w"
        self.grid_options["columnspan"] = 1
        for row, label in enumerate(labels, 1):
            self.grid_options["row"] = row
            self.grid_options["column"] = 0
            self.label_options["text"] = label + " граница:"
            self.add_label(labelframe, self.label_options, self.grid_options)
            
        self.grid_options["row"] = 1
        self.grid_options["column"] = 1
        self.spinbox_options["to"] = 1000
        self.spinbox_options["from_"] = -1000
        lower_bound_spinbox = ttk.Spinbox(
            labelframe,
            textvariable=self.generator_lower_bound,
            validate="key",
            validatecommand=self.float_key_validation,
            **self.spinbox_options
        )
        lower_bound_spinbox.grid(self.grid_options)
        
        self.grid_options["row"] = 2
        upper_bound_spinbox = ttk.Spinbox(
            labelframe,
            textvariable=self.generator_upper_bound,
            validate="key",
            validatecommand=self.float_key_validation,
            **self.spinbox_options
        )
        upper_bound_spinbox.grid(self.grid_options)
       
       
    def add_operator_label_frame(self) -> None:
        bounds = [(self.operator_1_lower_bound, self.operator_1_upper_bound),
                  (self.operator_2_lower_bound, self.operator_2_upper_bound),
                  (self.operator_3_lower_bound, self.operator_3_upper_bound)]
        for index in range(3):
            self.grid_options["row"] = index * 3 
            self.grid_options["rowspan"] = 3
            self.grid_options["column"] = 3
            
            labelframe = ttk.LabelFrame(self)
            labelframe["labelwidget"] = ttk.Label(text=f"Параметры оператора {index + 1}", style="Bold.TLabel") 
            labelframe.grid(self.grid_options)
            
            self.grid_options["row"] = 0
            self.grid_options["column"] = 0
            self.grid_options["rowspan"] = 1
            self.grid_options["columnspan"] = 2
            self.grid_options["sticky"] = "ns"
            self.label_options["text"] = "равномерное распределение"
            self.add_label(labelframe, self.label_options, self.grid_options)
            
            labels = ("нижняя", "верхняя")
            
            self.grid_options["sticky"] = "w"
            self.grid_options["columnspan"] = 1
            for row, label in enumerate(labels, 1):
                self.grid_options["row"] = row
                self.grid_options["column"] = 0
                self.label_options["text"] = label + " граница:"
                self.add_label(labelframe, self.label_options, self.grid_options)
                
            self.grid_options["row"] = 1
            self.grid_options["column"] = 1
            self.spinbox_options["to"] = 1000
            self.spinbox_options["from_"] = -1000
            lower_bound_spinbox = ttk.Spinbox(
                labelframe,
                textvariable=bounds[index][0], 
                validate="key",
                validatecommand=self.float_key_validation,
                **self.spinbox_options
            )
            lower_bound_spinbox.grid(self.grid_options)
            
            self.grid_options["row"] = 2
            upper_bound_spinbox = ttk.Spinbox(
                labelframe,
                textvariable=bounds[index][1], 
                validate="key",
                validatecommand=self.float_key_validation,
                **self.spinbox_options
            )
            upper_bound_spinbox.grid(self.grid_options)
        
        
    def add_computer_label_frame(self) -> None:
        self.grid_options["columnspan"] = 1
        
        bounds = (self.computer_1_processing_time, self.computer_2_processing_time)
        for index in range(2):
            self.grid_options["row"] = 3 + index * 2
            self.grid_options["column"] = 2
            self.grid_options["rowspan"] = 2 if index < 1 else 1
            
            labelframe = ttk.LabelFrame(self)
            labelframe["labelwidget"] = ttk.Label(text=f"Параметры компьютера {index + 1}", style="Bold.TLabel") 
            labelframe.grid(self.grid_options)
            
            self.grid_options["row"] = 0
            self.grid_options["column"] = 0
            self.grid_options["rowspan"] = 1
            self.grid_options["sticky"] = "ns"
            self.label_options["text"] = "Время обработки:"
            self.add_label(labelframe, self.label_options, self.grid_options)
                
            self.grid_options["column"] = 1
            self.spinbox_options["to"] = 1000
            self.spinbox_options["from_"] = -1000
            lower_bound_spinbox = ttk.Spinbox(
                labelframe,
                textvariable=bounds[index],
                validate="key",
                validatecommand=self.float_key_validation,
                **self.spinbox_options
            )
            lower_bound_spinbox.grid(self.grid_options)
        

    def add_simulate_button(self) -> None:
        self.grid_options["row"] = 2
        self.grid_options["column"] = 0
        self.grid_options["sticky"] = "ns"
        self.grid_options["rowspan"] = 1
        self.grid_options["columnspan"] = 2
        button = ttk.Button(
            self,
            text="Смоделировать",
            command=self.simulate
        )
        button.grid(self.grid_options)
    
    
    def add_result_label(self) -> None:
        self.grid_options["row"] = 6
        self.grid_options["column"] = 0
        self.grid_options["columnspan"] = 3
        self.label_options["textvariable"] = self.result
        self.result_label = ttk.Label(self, **self.label_options)
        self.result_label.grid(self.grid_options)
    
    
    def simulate(self) -> None:
        result = str()
        
        try:
            system = InfoSystem(self.request_amount.get(), self.delta_t.get())
            result = system.simulate(
                UniformDistribution(self.generator_lower_bound.get(), self.generator_upper_bound.get()),
                [
                    UniformDistribution(self.operator_1_lower_bound.get(), self.operator_1_upper_bound.get()),
                    UniformDistribution(self.operator_2_lower_bound.get(), self.operator_2_upper_bound.get()),
                    UniformDistribution(self.operator_3_lower_bound.get(), self.operator_3_upper_bound.get())
                ],
                [self.computer_1_processing_time.get(), self.computer_2_processing_time.get()]
            )
            
            tmp = f"{result * 100:.2f}".rstrip("0").rstrip(".")
            result = f"Вероятность отказа в обслуживании равна {tmp}%"
        
        except ValueError as error:
            self.result.set(error)
            return
            
        except Exception as error:
            print(error)
            result = "Недопускается наличие пустых полей!"
            self.result.set(result)
            return
        
        self.result_label["foreground"] = "black"
        self.result.set(result)
    

    def is_valid_positive_int(self, newval: str) -> bool:
        self.result.set(str())
        self.result_label["foreground"] = "red"
        
        if not newval:
            return True
        
        if not newval.isdigit():
            self.result.set(f"Недопустимый символ для положительного целого числа!")
            return False
        
        if newval.startswith("0") and int(newval) != 0 or newval.startswith("00"):
            self.err = True
            self.result.set(f"Недопускается наличие незначащих нулей!")
            return False
        
        return True
    
    
    def is_valid_float(self, newval: str) -> bool:
        self.result.set(str())
        self.result_label["foreground"] = "red"
        
        if not newval:
            return True
        
        if newval.count("-") > 1 or newval.count("-") == 1 and newval[0] != "-":
            self.err = True
            self.result.set(f"Минус может быть только в начале числа!")
            return False
        
        if newval.count(".") > 1:
            self.err = True
            self.result.set(f"Рациональное число может содержать только один символ '.'!")
            return False
    
        if not re.match("^[-]?(0|[1-9]\d*)(\.\d*)?$", newval):
            self.err = True
            self.result.set(f"Недопустимый формат для рационального числа!")
            return False
        
        return True


    @staticmethod
    def add_label(container: ttk.Frame, label_options: dict, grid_options: dict) -> None:
        ttk.Label(container, **label_options).grid(**grid_options)