import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(page_title="Titanic EDA Dashboard", layout="wide")
st.title("🚢 Titanic Dataset - Exploratory Data Analysis (EDA)")

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'train.csv')

@st.cache_data
def load_data(file_source):
    df = pd.read_csv(file_source)
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df['Cabin'] = df['Cabin'].fillna("Unknown")
    df['Embarked'] = df['Embarked'].fillna("Unknown")
    return df

df = None

if os.path.exists(csv_path):
    df = load_data(csv_path)
    st.success("Data successfully loaded!")
elif os.path.exists('train.csv'):
    df = load_data('train.csv')
    st.success("Data successfully loaded!")
else:
    uploaded_file = st.file_uploader("Upload train.csv file", type=['csv'])
    if uploaded_file is not None:
        df = load_data(uploaded_file)
        st.success("File successfully uploaded!")

if df is not None:
    tab1, tab2, tab3 = st.tabs(["📊 Data Overview", "📈 Data Analysis", "🎨 Visualizations"])

    with tab1:
        st.subheader("Raw Data & Basic Info")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**First 5 Rows (Head)**")
            st.dataframe(df.head())
        with col2:
            st.write("**Last 5 Rows (Tail)**")
            st.dataframe(df.tail())

        st.subheader("Dataset Summary")
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Rows", df.shape[0])
        c2.metric("Total Columns", df.shape[1])
        c3.metric("Duplicate Rows", df.duplicated().sum())

        st.write("**Statistical Summary (Describe)**")
        st.dataframe(df.describe().T)

        st.write("**Correlation Heatmap**")
        numericdf = df.select_dtypes(include=['number'])
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.heatmap(numericdf.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

    with tab2:
        st.subheader("Grouped Data Summaries")
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Survived Count by Gender**")
            st.dataframe(df.groupby('Sex')['Survived'].value_counts())

            st.write("**Survival Rate by Pclass**")
            st.dataframe(df.groupby('Pclass')['Survived'].mean())

            st.write("**Survival Rate by Gender**")
            st.dataframe(df.groupby('Sex')['Survived'].mean())

        with col2:
            st.write("**SibSp Count by Gender**")
            st.dataframe(df.groupby('Sex')['SibSp'].value_counts())

            st.write("**Parch Mean Percentage by Gender**")
            st.dataframe(df.groupby('Sex')['Parch'].mean() * 100)

            st.write("**Survived Count by Embarked**")
            st.dataframe(df.groupby('Embarked')['Survived'].value_counts())

    with tab3:
        st.subheader("Exploratory Charts")

        col1, col2 = st.columns(2)
        with col1:
            st.write("**Survived by Gender**")
            fig, ax = plt.subplots()
            sns.countplot(x='Sex', hue='Survived', data=df, ax=ax)
            st.pyplot(fig)

        with col2:
            st.write("**Passenger Class Distribution**")
            fig, ax = plt.subplots()
            df['Pclass'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax)
            st.pyplot(fig)

        col3, col4 = st.columns(2)
        with col3:
            st.write("**Survival by Pclass**")
            fig, ax = plt.subplots()
            sns.countplot(x='Pclass', hue='Survived', data=df, ax=ax)
            st.pyplot(fig)

        with col4:
            st.write("**Survived by Embarked & Gender**")
            fig, ax = plt.subplots()
            sns.barplot(x='Embarked', y='Survived', hue='Sex', data=df, ax=ax)
            st.pyplot(fig)

        col5, col6 = st.columns(2)
        with col5:
            st.write("**Age by Pclass and Survived**")
            fig, ax = plt.subplots()
            sns.violinplot(x='Pclass', y='Age', hue='Survived', data=df, split=True, inner='quartile', ax=ax)
            st.pyplot(fig)

        with col6:
            st.write("**Fare Distribution by Pclass**")
            fig, ax = plt.subplots()
            sns.boxplot(x='Pclass', y='Fare', hue='Survived', data=df, ax=ax)
            st.pyplot(fig)

        col7, col8 = st.columns(2)
        with col7:
            st.write("**Scatter Plot: Age vs Fare**")
            fig, ax = plt.subplots()
            sns.scatterplot(x='Age', y='Fare', hue='Survived', data=df, ax=ax)
            st.pyplot(fig)

        with col8:
            st.write("**Age Histogram by Survived**")
            fig, ax = plt.subplots()
            sns.histplot(data=df, x='Age', hue='Survived', ax=ax)
            st.pyplot(fig)

        st.write("**Swarmplot: Pclass vs Age by Survival**")
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.swarmplot(x='Pclass', y='Age', hue='Survived', data=df, size=4, palette='Set1', ax=ax)
        st.pyplot(fig)

        st.write("**Pairplot**")
        pairplot_fig = sns.pairplot(df)
        st.pyplot(pairplot_fig)