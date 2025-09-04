"""
dichotomy.py
Contient la fonction de simulation du paradoxe de la dichotomie.
"""

def dichotomy(total_distance=8.0, stop=0.000001, max_steps=1000, verbose=True):
    """
    Simule le paradoxe de la dichotomie.
    
    total_distance : distance initiale
    stop       : seuil d'arrêt
    max_steps      : nombre maximum d'étapes
    verbose        : affiche ou non dans la console
    
    Retourne : une liste de tuples (step, position, reste).
    """
    reste = total_distance
    position = 0.0
    step = 0
    history = []

    if verbose:
        print(f"{'step':>1} | {'position':>12} | {'distance restante':>20}")
        print("-" * 44)

    while reste > stop and step < max_steps:
        step += 1
        move = reste / 2.0
        position += move
        reste -= move
        history.append((step, position, reste))

        if verbose:
            print(f"{step:4d} | {position:12.8f} | {reste:20.8f}")

    if verbose:
        print("\nSimulation terminée.")
        print(f"Étapes réalisées : {step}")
        print(f"Position finale approximative : {position:.10f}")
        print(f"Distance restante ≈ {reste:.10f} (stop={stop})")

    return history


# Test rapide
if __name__ == "__main__":
    dichotomy()
