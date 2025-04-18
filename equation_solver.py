from sympy import symbols, Eq, solve, pretty

x = symbols('x')  # Define the variable
equation = input("Enter an equation (e.g. 2*x + 3 = 9): ")

# Split and convert into sympy equation
left, right = equation.split('=')
eq = Eq(eval(left), eval(right))

print("\n📘 Solving Equation:")
print("Equation:", eq)

solution = solve(eq, x)
print("\n✅ Step-by-step:")
print(pretty(eq))
print(f"\nSolution: x = {solution[0]}")