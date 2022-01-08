import streamlit as st
import streamlit.components.v1 as stc

# Load EDA
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel


# load dataset
def load_data(data):
    df = pd.read_csv(data)
    return df
# Fxn
# Vectorize + Cosine Similarity Matrix


def vectorize_text_to_cossine_mat(data):
    count_vect = CountVectorizer()
    cv_mat = count_vect.fit_transform(data)
    # get the cosine
    cosine_sim_mat = cosine_similarity(cv_mat)
    return cosine_sim_mat


def main():
    st.title("Aplikacija za ponudu tečaja by Josip Požega, prof.")

    menu = ["Početna", "Preporuke", "O aplikaciji"]
    choice = st.sidebar.selectbox("Izbornik", menu)

    # making data frame
    df = load_data(udemy_course_data.csv)

    if choice == "Početna":
        st.subheader('Početna')
        st.dataframe(df.head(10))

    elif choice == "Preporuke":
        st.subheader == "Preporuka tečajeva"
        search_term = st.text_input("Traži")
        num_of_rec = st-sidebar_input("Number", 4, 30, 7)
        if st.button("Preporuke"):
            if search_term is not None:
                pass

    else:
        st.subheader("O aplikaciji")
        st.text("Aplikacija by Josip Požega, prof.")
        st.text("Napravljeno sa Streamlitom & Pandom")


if __name__ == '__main__':
    main()
