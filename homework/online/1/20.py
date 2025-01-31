from tabulate import tabulate

## Exactly two trunks contain treasures, we generate all valid assignments
possible_scenarios = [
    (True, True, False),  ## Treasures in T1 & T2, T3 is empty
    (True, False, True),  ## Treasures in T1 & T3, T2 is empty
    (False, True, True),  ## Treasures in T2 & T3, T1 is empty
]


def evaluate_inscriptions(T1, T2):
    ## Inscriptions:
    insc_1 = not T1  ## "This trunk is empty" (True if T1 is actually empty)
    insc_2 = T1  ## "There is a treasure in Trunk 1" (True if T1 has treasure)
    insc_3 = T2  ## "There is a treasure in Trunk 2" (True if T2 has treasure)

    true_count = sum([insc_1, insc_2, insc_3])

    exactly_one_true = (true_count == 1)

    return insc_1, insc_2, insc_3, exactly_one_true


results = []
for T1, T2, T3 in possible_scenarios:
    insc_1, insc_2, insc_3, exactly_one_true = evaluate_inscriptions(
        T1, T2)
    results.append([T1, T2, T3, insc_1, insc_2, insc_3, exactly_one_true])

columns = ["Trunk 1 (T1)", "Trunk 2 (T2)", "Trunk 3 (T3)", "Insc_1 (T1 empty)",
           "Insc_2 (T1 has treasure)", "Insc_3 (T2 has treasure)", "Exactly One True"]

print("Treasure Truth Table")
print(tabulate(results, headers=columns, tablefmt="grid"))
