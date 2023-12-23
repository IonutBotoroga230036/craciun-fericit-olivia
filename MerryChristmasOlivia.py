import streamlit as st

def calculate(num1, num2, operation):
    if operation == 'Add':
        result = num1 + num2
    elif operation == 'Subtract':
        result = num1 - num2
    elif operation == 'Multiply':
        result = num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    else:
        result = None
    return result

st.title('Merry Christmas, Olivia!')
st.write('Ti-am pregatit un mic joc, sper sa iti placa!')
st.write('Scopul jocului e sa completezi quest-urile ca la final sa gasesti cadoul. Ready? Set.. Go!')
st.subheader("Level 1")
st.write('Pentru inceput... o sa facem putina matematica elementara. E simplu, stiu ca nu iti place matematica!')
# 51.5225373348999, -0.15659163682120436    
# 75761.26866745, 49921.7041815894
st.write('Ca si prim task, vei primi urmatoarele 2 numere:')
st.write('75761.26866745, 49921.7041815894')
st.write('Pentru fiecare dintre aceste 2 numere va trebui sa faci urmatoarele operatii:')
st.write('Din fiecare numar va trebui sa imparti 1000, dupa aceea scazi 50, iar dupa ce ai facut scaderea inmulteste cu 2. Simplu, nu? Ti-am facut un mic calculator ca sa iti vina mai usor! Noteaza rezultatele undeva pentru a folosi numerele mai tarziu, in viitor.')

st.subheader('Calculator')

# User input for the numbers and operation
num1 = st.number_input('Enter the first number:', value=0.0, format='%f')
num2 = st.number_input('Enter the second number:', value=0.0, format='%f')
operation = st.radio('Select operation:', ['Add', 'Subtract', 'Multiply', 'Divide'])

# Button to trigger the calculation
if st.button('Calculate'):
    result = calculate(num1, num2, operation)
    st.success(f'Result: {result}')

# Additional styling for a simple calculator-like appearance
st.markdown("""
<style>
    .st-eb {
        background-color: #f0f0f0;
        padding: 1rem;
        border-radius: 0.5rem;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        margin-top: 1rem;
    }

    .stButton button {
        color: white;
    }
</style>
""", unsafe_allow_html=True)



st.markdown("Pentru a trece la urmatorul nivel, pune numerele in casutele de mai jos:")
nr1 = st.number_input('Enter first number', value=0.0, format = '%f')
nr2 = st.number_input('Enter second number', value=0.0, format = '%f')
st.markdown("Ca sa verifici daca ai numerele potrivite, apasa butonul de jos:")
if st.button('Verifica'):
    if nr1 == 51.522537334899994:
        if nr2 == -0.15659163682120436:
            st.markdown('Bravo, mergi la nivelul urmator!')
            st.link_button('Level 2', url = "https://level-2.streamlit.app/")
        else:
            st.markdown("Al doilea numar este gresit!")    
    else:
        st.markdown('Primul numar este gresit!')