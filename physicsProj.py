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


def main():
    print("*** Please do not use I, E, S, N, C, O, or Q ***")
    input_str = input("Enter the equation (e.g., 'm*g - T = 0'): ")


    equation, symbols = create_equation(input_str)
    variables= [str(symbol) for symbol in equation.free_symbols]
    solutions = solve_equation(equation, variables)
    



    target_variable = input("Enter the variable you're looking for: ")
    if target_variable in solutions:
        print(f"{target_variable} = {solutions[target_variable]}")
    else:
        print("Variable not found in the equation.")

if __name__ == "__main__":
    main()

