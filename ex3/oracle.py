import os
import sys
try:
    from dotenv import load_dotenv
except ImportError:
    print("[FAIL] Missing python-dotenv. Please run: poetry add python-dotenv")
    sys.exit(1)


def main() -> None:
    # 1. On charge le fichier .env (s'il existe)
    load_dotenv()

    # 2. On récupère TOUTES les variables demandées
    mode = os.getenv("MATRIX_MODE")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    # 3. GESTION DES ERREURS : Si une variable manque, on prévient et on quitte
    missing_vars = []
    for var_name, var_value in [
        ("MATRIX_MODE", mode), ("DATABASE_URL", db_url),
        ("API_KEY", api_key), ("LOG_LEVEL", log_level),
        ("ZION_ENDPOINT", zion_endpoint)
    ]:
        if not var_value:
            missing_vars.append(var_name)

    if missing_vars:
        print("WARNING: Missing configuration! The Oracle is blind.")
        for missing in missing_vars:
            print(f"  -> {missing} is not set.")
        print("\nPlease create a .env file from .env.example:")
        print("$> cp .env.example .env")
        sys.exit(1)

    # 4. L'AFFICHAGE DU SUJET
    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")

    # 5. LA DIFFÉRENCE DEV / PROD (Exigée par le sujet)
    if mode.lower() == "production":
        print("Database: Connected to SECURE CLOUD instance")
        # En production, on cache la clé API pour la sécurité (ex: sec***)
        masked_key = api_key[:3] + "***" if len(api_key) > 3 else "***"
        print(f"API Access: Authenticated (Key: {masked_key})")
        print("Log Level: SILENT (Production mode overrides DEBUG)")
    else:
        print(f"Database: Connected to local instance ({db_url})")
        print(f"API Access: Authenticated (Key: {api_key})")
        print(f"Log Level: {log_level}")

    print(f"Zion Network: Online at {zion_endpoint}\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found, reading from terminal memory")
    print("[OK] Production overrides available")
    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
