import streamlit as st

st.title('Level 2')
st.markdown('Acum lucrurile vor deveni mult mai interesante.')
st.write('Numerele pe care le-ai obtinut au o folosinta in viata reala. Formatul lor... ce iti spune? La ce se folosesc? Daca ai nevoie de ajutor, apasa pe butin pentru a primi un hint!')
if st.button('Hint'):
    st.success('Numerele pot reprezenta un numar de telefon... sau poate niste coordonate... Cine stie?')
st.markdown("Numerele obtinute te vor ajuta sa gasesti o persoana. Pentru a trece la urmatorul nivel va trebui sa scrii in caseta de mai jos numele persoanei.")
name = st.text_input('Name of the person')
if st.button('Enter'):
    if name == 'Sherlock Holmes':
        st.markdown("Bravo!")
        
    else:
        st.markdown('Gresit!')