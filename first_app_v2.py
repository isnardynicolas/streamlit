#!/usr/bin/env python
# coding: utf-8

# In[1]:

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit.components.v1 as components


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)

st.markdown("<h1 style='text-align: center;'>Streamlit 🚗 : build and share data apps</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <h3 style='text-align: center;'>Correlation & Distribution Analysis</h3>
    """,
    unsafe_allow_html=True
)

st.sidebar.markdown("**Challenge :**")
st.sidebar.caption("À partir du dataset des voitures, tu afficheras : une analyse de corrélation et de distribution grâce à différents graphiques et des commentaires. des boutons doivent être présents pour pouvoir filtrer les résultats par région (US / Europe / Japon). Cette application doit être disponible sur la plateforme de partage.")

st.write(" ", unsafe_allow_html=True)
st.write(" ", unsafe_allow_html=True)
st.write(" ", unsafe_allow_html=True)

# Image gif

image_url = "https://media.giphy.com/media/o6S51npJYQM48/giphy.gif"
st.sidebar.image(image_url, use_column_width=True)

st.sidebar.write("--------------------")
st.sidebar.markdown("**Filtrez les résultats par région :**  \n(🇺🇸 US / 🇪🇺 Europe / 🇯🇵 Japan)")

# Création de la barre latérale pour filtrer par région
region = st.sidebar.radio("Sélectionnez une région", ('Toutes les régions', 'US', 'Europe', 'Japan'))

# Filtrage du dataframe en fonction de la région sélectionnée
if region == 'Toutes les régions':
    df_filtered_corr = df_car
    df_filtered_dist = df_car
else:
    df_filtered_corr = df_car[df_car['continent'].str.contains(region)]
    df_filtered_dist = df_car[df_car['continent'].str.contains(region)]

'''
---------------------------------------------
'''

# Heatmap 

st.markdown("<h6 style='text-align: center;'>Corrélations entre les différentes variables</h6>", unsafe_allow_html=True)


fig_corr, ax_corr = plt.subplots()
viz_correlation = sns.heatmap(df_filtered_corr.corr(),
                              center=0,
                              cmap=sns.color_palette("vlag", as_cmap=True),
                              ax=ax_corr)

st.pyplot(fig_corr)

'''
---------------------------------------------
'''

# Scatter Plot 

st.markdown("<h6 style='text-align: center;'>Corrélations entre deux variables</h6>", unsafe_allow_html=True)


x_variable = st.selectbox("Variable X", df_filtered_corr.columns)
y_variable = st.selectbox("Variable Y", df_filtered_corr.columns)

fig_scatter, ax_scatter = plt.subplots()
sns.scatterplot(data=df_filtered_corr, x=x_variable, y=y_variable, ax=ax_scatter)

st.pyplot(fig_scatter)

'''
---------------------------------------------
'''

# Subplots

# Convertir la colonne "continent" en type catégoriel
df_filtered_dist['continent'] = df_filtered_dist['continent'].astype('category')

st.markdown("<h6 style='text-align: center;'>Répartition des cylindres par continent</h6>", unsafe_allow_html=True)


fig_dist, ax_dist = plt.subplots()
viz_dist = sns.countplot(data=df_filtered_dist, x="cylinders", hue="continent", ax=ax_dist)

st.pyplot(fig_dist)

'''
---------------------------------------------
'''

# Box Plot

st.markdown("<h6 style='text-align: center;'>Distribution d'une variable</h6>", unsafe_allow_html=True)


variable = st.selectbox("Variable", df_filtered_dist.columns)

fig_box, ax_box = plt.subplots()
sns.boxplot(data=df_filtered_dist, y=variable, ax=ax_box)

st.pyplot(fig_box)


