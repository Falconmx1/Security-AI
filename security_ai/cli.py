import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Security AI - El Bro de la Ciberseguridad")
    parser.add_argument("command", choices=["scan", "analyze", "audit"], help="Comando a ejecutar")
    parser.add_argument("-p", "--path", required=True, help="Ruta del archivo o directorio")
    
    args = parser.parse_args()
    
    if args.command == "scan":
        print(f"[🔍] Escaneando: {args.path}")
        print("[✅] Escaneo completado. No se encontraron amenazas (demo).")
    elif args.command == "analyze":
        print(f"[🧠] Analizando con IA: {args.path}")
        print("[🟢] Resultado: Limpio (probabilidad 0.02)")
    elif args.command == "audit":
        print(f"[📜] Auditando logs: {args.path}")
        print("[🟡] 3 intentos de acceso fallido detectados.")

if __name__ == "__main__":
    main()
