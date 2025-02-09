from itertools import product
from typing import Callable, List

def print_truth_table(expression1: Callable, expression2: Callable, vars: List[str]) -> bool:
    """
    Print truth table and compare two logical expressions
    Returns True if expressions are logically equivalent
    """
    ## Create header
    header = " | ".join(vars + ["Expr1", "Expr2", "Equivalent?"])
    print(header)
    print("-" * len(header))
    
    values = list(product([True, False], repeat=len(vars)))
    equivalent = True
    
    for vals in values:
        result1 = expression1(*vals)
        result2 = expression2(*vals)
        row_equiv = result1 == result2
        equivalent &= row_equiv
        
        ## Convert True/False to T/F for cleaner output
        val_str = [str(int(v)) for v in vals]
        print(f"{' | '.join(val_str + [str(int(result1)), str(int(result2)), str(int(row_equiv))])}")
    
    return equivalent

def check_problem1() -> None:
    """
    Check if ¬p → (q → r) and q → (p ∨ r) are logically equivalent
    Show complete truth table
    """
    print("Problem 1: Are ¬p → (q → r) and q → (p ∨ r) logically equivalent?\n")
    
    def expr1(p: bool, q: bool, r: bool) -> bool:
        return (not p) <= (q <= r)
    
    def expr2(p: bool, q: bool, r: bool) -> bool:
        return q <= (p or r)
    
    result = print_truth_table(expr1, expr2, ["p", "q", "r"])
    print(f"\nConclusion: The expressions are{' ' if result else ' not '}logically equivalent")

def show_problem2_steps() -> None:
    """
    Show the step-by-step solution for proving [¬p ∧ (p ∨ q)] → q is a tautology
    """
    print("Problem 2: Show [¬p ∧ (p ∨ q)] → q is a tautology\n")
    
    def expr(p: bool, q: bool) -> bool:
        not_p = not p
        p_or_q = p or q
        left_side = not_p and p_or_q
        result = left_side <= q
        print(f"{int(p)} | {int(q)} | {int(not_p)} | {int(p_or_q)} | {int(left_side)} | {int(result)}")
        return result
    
    print("p | q | ¬p | p∨q | ¬p∧(p∨q) | Result")
    print("-" * 35)
    
    values = list(product([True, False], repeat=2))
    is_tautology = all(expr(*vals) for vals in values)
    
    print(f"\nConclusion: The expression is{' ' if is_tautology else ' not '}a tautology")

def check_biconditional_equivalence() -> None:
    """
    Check which expression is equivalent to p ↔ q with truth tables
    """
    print("Problem 3: Which expression is equivalent to p ↔ q?\n")
    
    def biconditional(p: bool, q: bool) -> bool:
        return p == q
    
    options = [
        ("(p ∨ q) ∧ (¬p ∨ ¬q)", lambda p, q: (p or q) and (not p or not q)),
        ("(p ∧ q) ∨ (¬p ∧ ¬q)", lambda p, q: (p and q) or (not p and not q)),
        ("(p ∧ ¬q) ∨ (¬p ∧ q)", lambda p, q: (p and not q) or (not p and q)),
        ("¬(p ∨ q) ∧ (p ∨ q)", lambda p, q: not(p or q) and (p or q))
    ]
    
    for i, (desc, func) in enumerate(options, 1):
        print(f"\nTesting option {chr(96 + i)}: {desc}")
        result = print_truth_table(biconditional, func, ["p", "q"])
        print(f"Option {chr(96 + i)} is{' ' if result else ' not'} equivalent to p ↔ q")

def predicate_domain_expansion(domain: List[int]) -> None:
    """
    Show expanded quantified expressions for specific domain
    """
    print("Problem 5: Expand the following expressions for domain {1, 2, 3}:\n")
    
    expressions = {
        "∃x P(x,3)": lambda d: " ∨ ".join([f"P({x},3)" for x in d]),
        "∀y P(1,y)": lambda d: " ∧ ".join([f"P(1,{y})" for y in d]),
        "∃y ¬P(2,y)": lambda d: " ∨ ".join([f"¬P(2,{y})" for y in d]),
        "∀x ¬P(x,2)": lambda d: " ∧ ".join([f"¬P({x},2)" for x in d])
    }
    
    for expr, expand_func in expressions.items():
        print(f"{expr} expands to:")
        print(f"{expand_func(domain)}\n")

def negate_inequality_statement(statement: str) -> None:
    """
    Problem 6: Express negation of inequality statements without using negation symbol
    """
    print("Problem 6: Express negations without using negation symbol\n")
    
    def negate_bounds(lower: float, upper: float, strict: bool = True) -> str:
        ## For strict inequalities (-2 < x < 3), use ≤,≥ in negation
        ## For non-strict inequalities (-4 ≤ x ≤ 1), use <,> in negation
        if(strict):
            return f"x ≤ {lower} or x ≥ {upper}"
        else:
            return f"x < {lower} or x > {upper}"
    
    statements = {
        "∀x (-2 < x < 3)": (-2, 3, True),
        "∃x (-4 ≤ x ≤ 1)": (-4, 1, False)  # Note: non-strict inequalities
    }
    
    for stmt, (lower, upper, strict) in statements.items():
        print(f"Original: {stmt}")
        if stmt.startswith("∀"):
            print(f"Negation: ∃x ({negate_bounds(lower, upper, strict)})")
        else:
            print(f"Negation: ∀x ({negate_bounds(lower, upper, not strict)})")
        print()

def translate_duck_statements() -> None:
    """
    Problem 7: Translate statements about ducks, officers, and waltzing into predicate logic
    Using:
    P(x): x is a duck
    Q(x): x is one of my poultry
    R(x): x is an officer
    S(x): x is willing to waltz
    """
    print("Problem 7: Translate statements into predicate logic\n")
    
    statements = {
        "No ducks are willing to waltz": 
            "∀x (P(x) → ¬S(x))",
        "No officers ever decline to waltz": 
            "∀x (R(x) → S(x))",
        "All my poultry are ducks": 
            "∀x (Q(x) → P(x))",
        "My poultry are not officers": 
            "∀x (Q(x) → ¬R(x))"
    }
    
    print("Given statements in predicate logic:")
    for eng, logic in statements.items():
        print(f"{eng}:")
        print(f"{logic}\n")
    
    ## Check if conclusion follows from premises
    print("Analysis of whether (d) follows from (a), (b), and (c):")
    print("1. From (c): All my poultry are ducks: ∀x (Q(x) → P(x))")
    print("2. From (a): No ducks waltz: ∀x (P(x) → ¬S(x))")
    print("3. From (b): All officers waltz: ∀x (R(x) → S(x))")
    print("4. From 1 and 2: All my poultry don't waltz: ∀x (Q(x) → ¬S(x))")
    print("5. From 3: If something doesn't waltz, it's not an officer: ∀x (¬S(x) → ¬R(x))")
    print("6. From 4 and 5: No poultry can be officers: ∀x (Q(x) → ¬R(x))")
    print("\nConclusion: Yes, (d) follows logically from (a), (b), and (c)")

def check_student_exam_negation() -> None:
    """
    Problem 8: Find correct negation of "All students passed the exam"
    """
    print("Problem 8: Negation of 'All students passed the exam'\n")
    
    original = "∀x(S(x) → P(x))"
    print(f"Original statement: {original}")
    
    steps = [
        ("¬∀x(S(x) → P(x))", "Add negation"),
        ("∃x¬(S(x) → P(x))", "Negation of universal quantifier"),
        ("∃x¬(¬S(x) ∨ P(x))", "Implication to disjunction"),
        ("∃x(S(x) ∧ ¬P(x))", "De Morgan's Law")
    ]
    
    print("\nNegation steps:")
    for step, explanation in steps:
        print(f"{step:<30} ({explanation})")
    
    options = {
        'a': "¬∀x(S(x) → P(x))",
        'b': "∃x(S(x) ∧ ¬P(x))",
        'c': "¬∃x(S(x) ∧ P(x))",
        'd': "∀x(S(x) ∧ ¬P(x))"
    }
    
    print("\nAnalysis of options:")
    for letter, expr in options.items():
        is_correct = expr == steps[-1][0]
        print(f"Option {letter}: {expr}")
        if(is_correct):
            print("✓ Correct - This is the proper negation obtained through our steps")
        else:
            if(letter == 'a'):
                print("✗ Incorrect - This is an intermediate step, not the final negation")
            elif(letter == 'c'):
                print("✗ Incorrect - This negates 'Some students passed' not 'All students passed'")
            elif(letter == 'd'):
                print("✗ Incorrect - This states all students failed, which is stronger than needed")

def verify_logical_equivalences() -> None:
    """
    Problem 4: Check which is not a valid propositional equivalence
    """
    print("Problem 4: Verify propositional equivalences\n")
    
    def check_equivalence(name: str, expr1: Callable, expr2: Callable, vars: List[str]) -> bool:
        print(f"\nTesting {name}:")
        return print_truth_table(expr1, expr2, vars)
    
    ## Test each equivalence
    equivalences = [
        ("De Morgan's Law", 
         lambda p, q: not (p and q), 
         lambda p, q: (not p) or (not q),
         ["p", "q"]),
        
        ("Conditional-Disjunction", 
         lambda p, q: p <= q, 
         lambda p, q: (not p) or q,
         ["p", "q"]),
        
        ("Biconditional", 
         lambda p, q: p == q, 
         lambda p, q: (p and q) or (not p and not q),
         ["p", "q"]),
        
        ("Distributive", 
         lambda p, q, r: p or (q and r), 
         lambda p, q, r: (p or q) and (p or r),
         ["p", "q", "r"])
    ]
    
    results = {}
    for name, expr1, expr2, vars in equivalences:
        results[name] = check_equivalence(name, expr1, expr2, vars)
    
    print("\nConclusions:")
    for name, is_equiv in results.items():
        if(not is_equiv):
            print(f"{name}: Invalid equivalence")
            break
        print(f"{name}: Valid equivalence")

def print_final_answers():
    """
    Print just the answers without work, using computed results
    """
    print("\n" + "="*50)
    print("FINAL ANSWERS SUMMARY")
    print("="*50 + "\n")
    
    ## Problem 1
    def expr1(p: bool, q: bool, r: bool) -> bool:
        return (not p) <= (q <= r)
    def expr2(p: bool, q: bool, r: bool) -> bool:
        return q <= (p or r)
    prob1_result = all(expr1(*vals) == expr2(*vals) 
                      for vals in product([True, False], repeat=3))
    print("1. Are ¬p → (q → r) and q → (p ∨ r) logically equivalent?")
    print(f"   {'Yes' if prob1_result else 'No'}\n")
    
    ## Problem 2
    def tautology_expr(p: bool, q: bool) -> bool:
        return (not p and (p or q)) <= q
    prob2_result = all(tautology_expr(*vals) 
                      for vals in product([True, False], repeat=2))
    print("2. Is [¬p ∧ (p ∨ q)] → q a tautology?")
    print(f"   {'Yes' if prob2_result else 'No'}\n")
    
    ## Problem 3
    def biconditional(p: bool, q: bool) -> bool:
        return p == q
    options = [
        lambda p, q: (p or q) and (not p or not q),
        lambda p, q: (p and q) or (not p and not q),
        lambda p, q: (p and not q) or (not p and q),
        lambda p, q: not(p or q) and (p or q)
    ]
    results = [all(biconditional(p, q) == opt(p, q) 
                  for p, q in product([True, False], repeat=2))
               for opt in options]
    correct_option = chr(97 + results.index(True))  ## 'a' + index of True
    print("3. Which expression is equivalent to p ↔ q?")
    print(f"   {correct_option}) Given option {correct_option}\n")
    
    ## Problem 4
    equivalences = [
        ("De Morgan's Law", 
         lambda p, q: not (p and q), 
         lambda p, q: (not p) or (not q),
         ["p", "q"]),
        ("Conditional-Disjunction", 
         lambda p, q: p <= q, 
         lambda p, q: (not p) or q,
         ["p", "q"]),
        ("Biconditional", 
         lambda p, q: p == q, 
         lambda p, q: (p and q) or (not p and not q),
         ["p", "q"]),
        ("Distributive", 
         lambda p, q, r: p or (q and r), 
         lambda p, q, r: (p or q) and (p or r),
         ["p", "q", "r"])
    ]
    invalid_equiv = None
    for name, expr1, expr2, vars in equivalences:
        values = list(product([True, False], repeat=len(vars)))
        if(not all(expr1(*vals) == expr2(*vals) for vals in values)):
            invalid_equiv = name
            break
    print("4. Which is not a valid propositional equivalence?")
    if(invalid_equiv):
        print(f"   The {invalid_equiv} equivalence is invalid")
    else:
        print("   All equivalences are valid")
    
    ## Problem 5
    domain = [1, 2, 3]
    expressions = {
        "∃x P(x,3)": " ∨ ".join([f"P({x},3)" for x in domain]),
        "∀y P(1,y)": " ∧ ".join([f"P(1,{y})" for y in domain]),
        "∃y ¬P(2,y)": " ∨ ".join([f"¬P(2,{y})" for y in domain]),
        "∀x ¬P(x,2)": " ∧ ".join([f"¬P({x},2)" for x in domain])
    }
    print("5. Expanded predicates for domain {1, 2, 3}:")
    for expr, expansion in expressions.items():
        print(f"   {expr}: {expansion}")
    print()
    
    ## Problem 6
    def negate_bounds(lower: float, upper: float, strict: bool = True) -> str:
        return f"x ≤ {lower} or x ≥ {upper}" if strict else f"x < {lower} or x > {upper}"
    
    print("6. Negations of inequality statements:")
    print(f"   ∀x (-2 < x < 3) → ∃x ({negate_bounds(-2, 3, True)})")
    print(f"   ∃x (-4 ≤ x ≤ 1) → ∀x ({negate_bounds(-4, 1, False)})\n")
    
    ## Problem 7
    statements = {
        "a": "∀x (P(x) → ¬S(x))",
        "b": "∀x (R(x) → S(x))",
        "c": "∀x (Q(x) → P(x))",
        "d": "∀x (Q(x) → ¬R(x))"
    }
    print("7. Duck statements in predicate logic:")
    for letter, stmt in statements.items():
        print(f"   {letter}) {stmt}")
    print("   e) Yes, (d) follows from (a), (b), and (c)\n")
    
    # Problem 8
    steps = [
        ("¬∀x(S(x) → P(x))", "Add negation"),
        ("∃x¬(S(x) → P(x))", "Negation of universal quantifier"),
        ("∃x¬(¬S(x) ∨ P(x))", "Implication to disjunction"),
        ("∃x(S(x) ∧ ¬P(x))", "De Morgan's Law")
    ]
    final_negation = steps[-1][0]
    options = {
        'a': "¬∀x(S(x) → P(x))",
        'b': "∃x(S(x) ∧ ¬P(x))",
        'c': "¬∃x(S(x) ∧ P(x))",
        'd': "∀x(S(x) ∧ ¬P(x))"
    }
    correct_answer = next(letter for letter, expr in options.items() 
                         if expr == final_negation)
    print("8. Negation of 'All students passed the exam':")
    print(f"   {correct_answer}) {options[correct_answer]}")

def main():
    check_problem1()
    print("\n" + "="*50 + "\n")
    
    show_problem2_steps()
    print("\n" + "="*50 + "\n")
    
    check_biconditional_equivalence()
    print("\n" + "="*50 + "\n")
    
    verify_logical_equivalences()
    print("\n" + "="*50 + "\n")
    
    predicate_domain_expansion([1, 2, 3])
    print("\n" + "="*50 + "\n")
    
    negate_inequality_statement("")
    print("\n" + "="*50 + "\n")
    
    translate_duck_statements()
    print("\n" + "="*50 + "\n")
    
    check_student_exam_negation()
    
    print_final_answers()

if(__name__ == "__main__"):
    main()
