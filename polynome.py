def afficher(p):
    """
    Affiche le polynôme p sous la forme 'an X^n + ... + a0'.
    """
    terms = []
    n = len(p) - 1
    for i, coeff in enumerate(p):
        if coeff != 0:
            if i == 0:
                terms.append(f"{coeff}")
            elif i == 1:
                terms.append(f"{coeff}X")
            else:
                terms.append(f"{coeff}X^{i}")
    # Reverse the terms to start with the highest power
    polynomial = " + ".join(reversed(terms))
    print(polynomial)

def get_valeur(p, x):
    """
    Calcule et renvoie la valeur du polynôme p au point x.
    """
    result = 0
    for i, coeff in enumerate(p):
        result += coeff * (x ** i)
    return result

def deriver(p):
    """
    Calcule et retourne le polynôme dérivé de p.
    """
    derived = [i * p[i] for i in range(1, len(p))]
    return derived

# Programme principal 
# Exemple de polynôme : p(x) = 2 + 3x + 4x^2
p = [2, 3, 4]

print("Polynôme:")
afficher(p)

x_value = 2
print(f"\nValeur de p({x_value}): {get_valeur(p, x_value)}")

derived_p = deriver(p)
print("\nDérivée:")
afficher(derived_p)