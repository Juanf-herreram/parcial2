import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

car = pd.read_csv('Datos banrep.csv')

st.title("Graficos Datos Banrep")

fig, ax = plt.subplots(1,1)
ax.plot(car['Tasa de política monetaria(Dato fin de trimestre)'].dropna())
ax.set_title("TPM TRIMESTRE")
ax.axis()
st.pyplot(fig)

fig, ax = plt.subplots(1,1)
ax.plot(car['Producto Interno Bruto (PIB) real, Trimestral, base: 2015, Ajuste estacional(Dato fin de trimestre)'].dropna())
ax.set_title("PIB TRIMESTRAL")
ax.axis()
st.pyplot(fig)

fig, ax = plt.subplots(1,1)
ax.plot(car['Inflación total(Dato fin de mes)'].dropna())
ax.set_title("INFLACION MENSUAL")
ax.axis()
st.pyplot(fig)

fig, ax = plt.subplots(1,1)
ax.plot(car['Tasa de desempleo - total nacional(Dato fin de mes)'].dropna())
ax.set_title("TD MENSUAL")
ax.axis()

st.pyplot(fig)

