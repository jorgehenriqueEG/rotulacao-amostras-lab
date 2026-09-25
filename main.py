from datetime import datetime

reagentes = [
    {"nome": "Amoxilina", "validade": "2024-01-15"},
    {"nome": "Salina", "validade": "2025-10-01"},
    {"nome": "Etanol", "validade": "2023-12-31"}
]

hoje = datetime.now()

for ref in reagentes:
    val = datetime.strptime(ref["validade"], "%Y-%m-%d")
    dias = (val - hoje).days
    status = "OK"
    if dias < 0:
        status = "DESCARTAR"
    elif dias < 30:
        status = "CRITICO"
    print(f"{ref['nome']}: {status} ({dias} dias)")