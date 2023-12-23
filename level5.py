import streamlit as st

st.title('Level 5')
st.markdown('Acesta este ultimul nivel, sper ca ti-a placut si ca te-ai distrat pana acum!')
st.markdown('Ca sa ajungi la finalul jocului, va trebui sa enumeri 5 tari si capitalele acestora, inafara de Romania, din Europa. In casuta vei scrie in formatul urmator:')
st.markdown('tara1 - capitala1, tara2 - capitala2, tara3 - capitala3, tara4 - capitala4, tara5 - capitala5')
tari = {
    "Albania": "Tirana",
    "Austria": "Viena",
    "Belgia": "Bruxelles",
    "Bosnia și Herțegovina": "Sarajevo",
    "Bulgaria": "Sofia",
    "Cehia": "Praga",
    "Croația": "Zagreb",
    "Danemarca": "Copenhaga",
    "Elveția": "Berna",
    "Estonia": "Tallinn",
    "Finlanda": "Helsinki",
    "Franța": "Paris",
    "Germania": "Berlin",
    "Grecia": "Atena",
    "Ungaria": "Budapesta",
    "Irlanda": "Dublin",
    "Italia": "Roma",
    "Kosovo": "Priština",
    "Letonia": "Riga",
    "Lituania": "Vilnius",
    "Luxemburg": "Luxemburg",
    "Macedonia de Nord": "Skopje",
    "Malta": "Valletta",
    "Muntenegru": "Podgorica",
    "Olanda": "Amsterdam",
    "Norvegia": "Oslo",
    "Polonia": "Varșovia",
    "Portugalia": "Lisabona",
    "România": "București",
    "Serbia": "Belgrad",
    "Slovacia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spania": "Madrid",
    "Suedia": "Stockholm",
    "Turcia": "Ankara",
    "Ucraina": "Kiev",
    "Regatul Unit": "Londra"
}
cnt = 0

raspuns = st.text_input('Answer', placeholder='Tara - Capitala')
answer = raspuns.split(', ')
for i in answer:
    if i.split(' - ')[0] in tari and tari[i.split(' - ')[0]] == i.split(' - ')[1]:
        cnt +=1
if st.button('Submit'):
    if cnt<5:
        st.markdown('Gresit!')
    elif cnt == 5:
        st.markdown('Felicitari! Ai trecut de cele 5 probe! Poti sa iti deschizi cadoul acum!')
        st.link_button('Gift!', url= '')
    else:
        st.markdown('YOU GET A N-WORD PASS, NIGGA!')
        st.link_button('Gift!', url= '')