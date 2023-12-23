import streamlit as st

st.title('Level 4')
st.markdown('''
In continuare, ti-am scris o poezie care are cateva indicii despre urmatorul raspuns:
''')
st.markdown('''
In gradina cu flori, sub soare stralucitor,  
Un mister ascuns, fericit ganditor.  
Printre petale albe, in dansul lor fin,  
Se ascunde lumina catre un viitor mai lin.\n\n
             
Cu rochie alba, ca fulgii de nea,  
Fericita, ea, nu se astepta  
Ca nunta sa fie ceea ce isi dorea,  
Pe langa baiatul ce o acompania.
''')
name1 = st.text_input('Numele florii:')
if st.button('Enter'):
    if name1 == 'Floarea Miresei' or name1 == 'floarea miresei' or name1 == 'Floarea miresei':
        st.markdown('Bravo!')
        st.link_button('Level 5', url = 'https://level5-puiutu-micutu.streamlit.app/')
    else:
        st.markdown('Gresit!')