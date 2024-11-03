# Importar bibliotecas ----
from bcb import sgs



# Importar datos ----
dados_brutos = sgs.get(
    codes = {"IPCA": 433, "INPC": 188, "IGP-M": 189, "IGP-DI": 190, "IPC-BR": 191},
    start = "2000-01-01"
    )

# Tratar datos ----
dados_tratados = dados_brutos.reset_index()
dados_tratados

# Guardar datos ----
dados_tratados.to_csv(path_or_buf = "datos_tratados.csv", index = False)


