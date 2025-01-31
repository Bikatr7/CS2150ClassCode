from itertools import product
from tabulate import tabulate

def bitwise_and(a, b):
    return ''.join('1' if x == '1' and y == '1' else '0' for x, y in zip(a, b))

def bitwise_xor(a, b):
    return ''.join('1' if x != y else '0' for x, y in zip(a, b))

def solve_problem1():
    print("\nProblem 1:")
    ## a) 11000 ∧ 11011
    result_a = bitwise_and('11000', '11011')
    print(f"a) 11000 ∧ 11011 = {result_a}")
    
    ## b) (01010 ⊕ 11011) ⊕ 01000
    temp = bitwise_xor('01010', '11011')
    result_b = bitwise_xor(temp, '01000')
    print(f"b) (01010 ⊕ 11011) ⊕ 01000 = {result_b}")

## 2. Truth table for (p → q) ∧ (¬r ∨ q)
def implication(p, q):
    return (not p) or q

def solve_problem2():
    print("\nProblem 2:")
    headers = ['p', 'q', 'r', '(p → q)', '(¬r ∨ q)', '(p → q) ∧ (¬r ∨ q)']
    rows = []
    
    for p, q, r in product([True, False], repeat=3):
        impl = implication(p, q)
        not_r_or_q = (not r) or q
        result = impl and not_r_or_q
        rows.append([p, q, r, impl, not_r_or_q, result])
    
    print(tabulate(rows, headers=headers, tablefmt='grid'))

## 7. Circuit output and truth table
def circuit_output(p, q):
    not_p = not p
    and_gate = not_p and q
    or_gate = p or and_gate
    final_output = not or_gate
    return final_output

def solve_problem7():
    print("\nProblem 7:")
    print("a) Circuit output with p=True, q=True:")
    result = circuit_output(True, True)
    print(f"Output: {result}")
    
    print("\nb) Truth table for circuit:")
    headers = ['p', 'q', 'Output']
    rows = []
    for p, q in product([True, False], repeat=2):
        output = circuit_output(p, q)
        rows.append([p, q, output])
    
    print(tabulate(rows, headers=headers, tablefmt='grid'))

if(__name__ == "__main__"):
    solve_problem1()
    solve_problem2()
    solve_problem7()