import sys


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    # 1. LE PIÈGE : On essaie d'importer les paquets externes
    try:
        import pandas as pd
        import numpy as np
        import matplotlib
        import matplotlib.pyplot as plt
    except ImportError as e:
        # Si ça échoue, on attrape l'erreur sans planter le programme
        print(f"[FAIL] Missing dependency: {e.name}")
        print("\nSYSTEM ALERT: Cannot load programs into the Matrix.")
        print("Please install the required dependencies:")
        print("  -> With pip: pip install -r requirements.txt")
        print("  -> With Poetry: poetry install")
        print("                  poetry run python loading.py")
        sys.exit(1)

    # 2. SI TOUT VA BIEN : On affiche les versions installées
    print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
    print(f"[OK] matplotlib ({matplotlib.__version__}) - Visualization ready")

    # 3. L'ANALYSE : Simulation des données de la Matrice
    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    # On génère 1000 nombres aléatoires avec Numpy
    np.random.seed(42)  # Pour avoir toujours le même graphique
    matrix_signals = np.random.rand(1000) * 100

    # On met ces données dans une structure Pandas (DataFrame)
    df = pd.DataFrame({'Signal Strength': matrix_signals})

    # 4. LA VISUALISATION : On crée le graphique
    print("Generating visualization...")
    plt.figure(figsize=(10, 5))
    # On trace les points en vert façon "code de la matrice"
    plt.plot(df.index, df['Signal Strength'], color="#00FF41", linewidth=0.5)

    # On ajoute un fond noir et un titre
    plt.gca().set_facecolor('black')
    plt.title('Matrix Code Stream Analysis', color='#00FF41')
    plt.xlabel('Time Cycle')
    plt.ylabel('Signal Strength')

    # On sauvegarde l'image au lieu de l'afficher à l'écran
    plt.savefig('matrix_analysis.png')

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
