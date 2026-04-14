import sys
import os
import site


def main() -> None:
    # On joue les détectives (Concept 2)
    lieu_actuel: str = sys.prefix
    lieu_naissance: str = sys.base_prefix
    panneau_venv: str | None = os.environ.get('VIRTUAL_ENV')

    # La condition : est-ce que l'adresse a changé,
    #  ou est-ce que le panneau est allumé ?
    is_in_matrix: bool = (lieu_actuel != lieu_naissance) or (panneau_venv is not None)

    if is_in_matrix:
        # --- SCÉNARIO 1 : ON EST DANS L'ENVIRONNEMENT VIRTUEL ---
        print("\nMATRIX STATUS: Welcome to the construct\n")
        # sys.executable donne le chemin exact du binaire python utilisé en ce moment
        print(f"Current Python: {sys.executable}")

        # On récupère juste le nom du dossier à la fin du chemin
        # 1. On prépare notre variable (avec son annotation de type)
        venv_name: str = ""

        # 2. On fait un if / else classique et facile à lire
        if panneau_venv is not None:
            venv_name = os.path.basename(panneau_venv)
        else:
            venv_name = "Unknown"
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {lieu_actuel}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting\nthe global system.")
        print()
        print("Package installation path:")

        packages_paths: list[str] = site.getsitepackages()
        print(packages_paths[0])

    else:
        # --- SCÉNARIO 2 : ON EST DANS LE SYSTÈME GLOBAL ---
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")


if __name__ == "__main__":
    main()
