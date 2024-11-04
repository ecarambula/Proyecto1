# Instalar programas
    # pip install shiny
    # python -m pip install statsmodels
    # pip install plotnine
    # pip install python-bcb
 
# Importar bibliotecas
from shiny import App, render, ui
from statsmodels.tsa.seasonal import STL
import pandas as pd
import plotnine as p9

# Importar datos
dados = (pd.read_csv("datos_tratados.csv", converters={"Date": pd.to_datetime})
    .assign(indice = lambda x: pd.to_datetime(x.Date))
    .set_index("indice")
    .asfreq("MS"))

# Interfase de usuario
app_ui = ui.page_navbar(
    ui.nav_panel("Titulo")
)


# Servidor
def server(input, output, session):
    @output
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"

# Dashboard Shiny
app = App(app_ui, server)
