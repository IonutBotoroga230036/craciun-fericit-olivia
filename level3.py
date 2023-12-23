import streamlit as st



st.subheader('Level 3')
st.markdown('Acum pentru a completa acest nivel, va trebui sa gasesti numele altei persoane. Pentru a gasi numele persoanei potrivite va trebui sa cauti canonul lui Sherlock Holmes .pdf online. Mai departe va trebui sa utilizezi indiciile pe care le-ai descoperit pana acum. Daca ai nevoie de un sfat, sunt aici :smile:.')
name1 = st.text_input('Name of the person from the book')
if st.button('Confirm'):
    if name1 == 'Miss Stoner':
        st.markdown('Bravo!')
        st.link_button('Level 4', url = '')
    else:
        st.markdown('Gresit!')
if st.button('Hint 1'):
    st.markdown('Poate poti sa aflii ceva daca citesti ce scrie pe statueta?')
    if st.button('Hint 2'):
        st.markdown('Poate are de a face cu numarul de pe statuie?')
        if st.button('Hint 3'):
            st.button('Poate numarul de pe statuie reprezinta numarul paginii?')
