

















import streamlit as st
import pandas as pd
from PIL import Image
st.title("ALPHA TABREZ")
st.title("atomic structure of elements")
st.write('i have design this elements in order and i also provided their atomic structure to know how electron revolve around nucleus  ')
st.image('motivation.png')
st.image('3d.png')
st.image('Atom-Banner.jpg')
st.image('discoveryhydrogen.png')
st.image('world.png')
st.image('body.png')
st.image('good.png')

st.write('alpha tabrez')
st.header("python for elements")
df = pd.read_csv('../Periodic Table of Elements.csv')
st.dataframe(df)
atom_name = st.selectbox("Select Name of element : ", (df.iloc[:,1]))
#atom_name = st.selectbox("which property of elementes you want",('Phase','atomic radius','boiling point','melting point','density',(df.iloc[:,1])))
if (st.button('Show')):
    st.header(atom_name)

    # st.dataframe(df[df['Element'] == atom_name])
    dff = st.dataframe(df[df['Element']== atom_name])
    # c = dff.iloc[:,4].values
    # c = str(c[0])
    # for i in df[df['Element'] == atom_name].iloc[:, 2]:
    #     print(i)
    # st.markdown(f'{i}')
    # st.header(df['AtomicNumber'].values)
    for i in df[df['Element'] == atom_name].iloc[:, -1]:
           print(i)
    image = Image.open(i)
    st.image(image)
st.image('amino.png')
st.image('shielding.png')
st.image('nuclear.png')






