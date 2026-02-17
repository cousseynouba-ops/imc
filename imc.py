import streamlit as st

st.title("IMC")

poids= st.number_input("Veuillez donner le poids du patient :")
taille= st.number_input("Veuillez donner la taille du patient :")
if st.button("CALCUL") :
    imc = poids/(taille**2)

    st.write (imc)

    if imc <18.5:
        st.warning("Maigre")

    elif 18.5<imc<25:
        st.succes("Poids normal")

    elif 25 <imc <30 :
        st.warning("Surpoids")
    elif imc>= 30 :
        st.warning ("Obeise")
    else:

        st.info(" ceci n'est pas un nombre")