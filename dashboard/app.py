# Importar bibliotecas
from shiny import App, render, ui, reactive
from statsmodels.tsa.seasonal import STL
import pandas as pd
import plotnine as p9

# Importar datos
datos = (
    pd.read_csv(
        filepath_or_buffer="datos_tratados.csv",
        converters={"Date": pd.to_datetime}
    )
    .assign(indice = lambda x: pd.to_datetime(x.Date))
    .set_index("indice")
    .asfreq("MS")
)

# Interfase de usuario
app_ui = ui.page_navbar(
    ui.nav(
        "",
        ui.layout_sidebar(
            ui.panel_sidebar(
                
                ui.markdown(
                "Dashboard analítica para diagnosticar o comportamento" +
                "histórico da inflação brasileira, medida pelos principais" +
                "indicadores de conjuntura econômica. Utilize as opções" +
                "abaixo para customização da análise."
                ),

                ui.input_select(
                    id = "indicador",
                    label = ui.strong("Indicador:"),
                    choices = datos.columns[1:].tolist(),
                    selected = "IPCA",
                    multiple = False    
                ),

                ui.input_date_range(
                    id = "fechas",
                    label = ui.strong("Fecha inicial y final:"),
                    start = datos.Date.astype(str).min(),
                    end = datos.Date.astype(str).max(),
                    min = datos.Date.astype(str).min(),
                    max = datos.Date.astype(str).max(),
                    format = "mm/yyyy",
                    startview = "year",
                    language = "es",
                    separator = " - "
                ),

                ui.input_numeric(
                    id = "anio",
                    label = "Comparador de años:",
                    value = int(datos.Date.dt.year.max()),
                    min = int(datos.Date.dt.year.min()),
                    max = int(datos.Date.dt.year.max()),
                    step = 1
                ),

                ui.input_checkbox_group(
                    id = "componentes",
                    label = ui.strong("Componentes:"),
                    choices = ["% a.m.", "Tendência", "Sazonalidade", "Média"],
                    selected = ["% a.m."]
                ),

                ui.markdown(
                    """
                    Fuente: FGV e IBGE
                    Elaborado por EVRC
                    """
                ),
                width = 3
            ),
            
            ui.panel_main(
                ui.row(ui.output_plot("grafico_estacionalidad")),
                ui.row(ui.output_plot("grafico_componentes"))
            )
        )
    ),
    title = ui.strong("Diagnóstico de la inflación en Brasil"),
    bg = "blue",
    inverse = True
)

# Servidor
def server(input, output, session):

    @reactive.Calc
    def prepara_componentes():

        fecha_inicial = input.fechas()[0].strftime("%Y-%m-%d") 
        fecha_final = input.fechas()[1].strftime("%Y-%m-%d")
        seleccion_componentes = input.componentes()

        df = (
            datos
            .filter(
                items = ["Date", input.indicator()],
                axis = "columns"
            )
            .rename(columns = {input.indicador(): "indicador"})
            .query("Date >= @data_inicial and Date <= @data_final")
            .dropna()  
        )

        modelo = STL(endog = df.indicador, robust = True).fit()

        tabla_componentes = 

        
    
    @output
    @render.plot
    def grafico_componentes():
        grafico = (
            p9.ggplot(datos) +
            p9.aes(x = "Date", y = "IPCA") +
            p9.geom_line()
        )
        return grafico
    
#Dashboard Shiny 
app = App(app_ui, server)
