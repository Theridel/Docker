import os

# Leggiamo un nome da una variabile d'ambiente, altrimenti usiamo 'User'
nome = os.getenv("USER_NAME", "User")

print(f"--- Agente AI Avviato ---")
print(f"Ciao {nome}! Sto girando dentro un container isolato.")
print(f"Questo è il primo passo per il tuo sistema multi-agente.")
