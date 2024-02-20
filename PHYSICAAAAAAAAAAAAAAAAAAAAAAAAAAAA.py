import tkinter as tk
root = tk.Tk()
root.geometry('800x600')
root.title("PHYSICAAAAAAAAA")
root['bg']='#000'
welcome = tk.Label(root, text="Net Force Simplifier",
                   fg='#fff',
                   bg='#000',
                   font= ('Courier New',25, 'bold'))
welcome.place(relx= 0.5,
              rely= 0.2,
              anchor= 'center')

#func
import sympy as sp


def create_equation(input_str):
    symbols = {**sp.__dict__, **{func: getattr(sp, func) for func in ['sin', 'cos', 'tan', 'csc', 'sec', 'cot']}}
    equation = sp.sympify(input_str.replace('=', '-(') + ')', locals=symbols)  
    return equation, symbols


def solve_equation(equation, variables):
    solutions = {}
    for variable in variables:
        solution = sp.solve(equation, variable)[0]
        solutions[variable] = solution
    return solutions

def trigstuff(input_str, symbols):
    expr = sp.sympify(input_str, locals=symbols)
    simplified_expr = sp.simplify(expr)
    return simplified_expr

from threading import Thread
def main():
    
    input_str = Fx.get()
    equation, symbols = create_equation(input_str)
    variables= [str(symbol) for symbol in equation.free_symbols]

    target_variable = Find.get()
    def thread_func():
        solutions = solve_equation(equation, variables)
        if target_variable in solutions:
            Res.set(f"{target_variable} = {solutions[target_variable]}")
        else:
            Res.set("The variable is not in the equation.")

    thread = Thread(target=thread_func)
    thread.start()

#clear
def clearing():
    FxEn.delete(0, tk.END)
    FindEn.delete(0, tk.END)
    Res.set('')
    
    


#wawalabels adn entries
warn = tk.Label(root, text= "Please do not use C, E, I, N, O, Q, or S",
                fg= '#fff',
                bg='#000',
                font=('Courier New', 10, 'bold'))
warn.place(relx= 0.5,
              rely= 0.28,
              anchor= 'center')
#Fx
FxL = tk.Label(root, text="Enter the equation (e.g., 'm*g - T = 0'): ",
              fg='#fff',
              bg='#000',
              font= ('Courier New', 15,))
FxL.place(relx= 0.52,
              rely= 0.34,
              anchor= 'center')
Fx=tk.StringVar()
FxEn = tk.Entry(root, width=42,
                textvariable=Fx,
                bg= '#fff',
                font=40)
FxEn.place(relx= 0.5,
           rely=0.42,
           anchor='center',
           height=40)

#find
FindL = tk.Label(root, text="Enter the variable you're looking for: ",
              fg='#fff',
              bg='#000',
              font= ('Courier New', 15,))
FindL.place(relx= 0.5,
              rely= 0.5,
              anchor= 'center')
Find=tk.StringVar()
FindEn = tk.Entry(root, width=27,
                  textvariable=Find,
                  font=55)
FindEn.place(relx= 0.4,
           rely=0.59,
           anchor='center',
           height=40)

#result
ResL = tk.Label(root, text="Result: ",
              fg='#fff',
              bg='#000',
              font= ('Courier New', 15,))
ResL.place(relx= 0.5,
              rely= 0.67,
              anchor= 'center')
Res=tk.StringVar()
ResEn = tk.Entry(root, width=27, textvariable=Res,
                 state=tk.DISABLED, font= 55,
                 fg='#000')
ResEn.place(relx= 0.4,
           rely=0.75,
           anchor='center',
            height=40)


#buttons
solve = tk.Button(root, text="Solve", command=main, bg='#c0c4c6', width=12,
                  font= ('Courier New', 15, 'bold'))
solve.place(relx= 0.7,
           rely=0.59,
           anchor='center',
            height=40)

clear = tk.Button(root, text="Clear", command=clearing, bg='#c0c4c6', width=12,
                  font= ('Courier New', 15, 'bold'))
clear.place(relx= 0.7,
           rely=0.75,
           anchor='center',
            height=40)



root.mainloop()
