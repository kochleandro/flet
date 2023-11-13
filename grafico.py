import flet as ft
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import seaborn as sns

    
# Carga los datos desde el archivo
df = pd.read_excel('USD_ARSB_Diario_2016_2023_mod.xlsx')

import pandas as pd
import mplfinance as mpf

def plot_candlestick(df, start_date, end_date):
    # Crear un nuevo DataFrame con los nombres de columna adecuados
    df_corrected = df.rename(columns={'Ultimo': 'Close', 'Apertura': 'Open', 'Maximo': 'High', 'Minimo': 'Low'})

    # Convertir la columna 'Fecha' a tipo datetime
    df_corrected['Fecha'] = pd.to_datetime(df_corrected['Fecha'])

    # Seleccionar un rango específico de fechas
    df_selected = df_corrected[(df_corrected['Fecha'] >= start_date) & (df_corrected['Fecha'] <= end_date)]

    df_sorted = df_selected.sort_values('Fecha', ascending=True)
    df_sorted.set_index('Fecha', inplace=True)

    # Crear el gráfico de velas
    ap = [mpf.make_addplot(df_sorted['Close'], color='b')]
    mpf.plot(df_sorted, type='candle', style='yahoo', title='Gráfico de Velas (Octubre 2023)',
             addplot=ap, show_nontrading=True)

# Ejemplo de uso
start_date = '2022-07-01'
end_date = '2023-11-07'
plot_candlestick(df, start_date, end_date)