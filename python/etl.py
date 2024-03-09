# Importar bibliotecas ----
from bcb import sgs

# Importar datos ----
datos_brutos = sgs.get(
    codes = {"IPCA": 433, "INPC": 188, "IGP-M": 189, "IGP-DI": 190, "IPC-BR": 191},
    start = "2000-01-01"
    )

# Tratar datos ----
datos_tratados = datos_brutos.reset_index()
datos_tratados

# Guardar datos ----
datos_tratados.to_csv(path_or_buf = "datos_tratados.csv", index = False)


