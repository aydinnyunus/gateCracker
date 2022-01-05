import streamlit as st
import pandas as pd
import numpy as np
import requests


url = 'https://intense-beach-04157.herokuapp.com/smartLocks/'
st.title('Smart Locks in Turkey')


lock_models = ["Perkotek","ERD-1120","Efes Digital Panel","Mas","AC 13PX","Burg Wachter","DIP40","Lorex LR-DPH2","M100","MB05-03","MB DYF40","MLŞ 14-70","MLŞ 14-107","MRA 101","Netalsan Obsidian","ONDRIVE ED07","OP705","OP M400","OP M500","Pratik Kart","Desi Steely","Audio","Teknoline","Teknoline IMR18","Desi UTOPIC","WL02","D45","A20 Kapı Kilidi"]
option = st.selectbox(
     'Select your Lock Model',
     lock_models)

st.write('You selected:', option)


i = lock_models.index(option)
i += 1
#st.write(url + str(i))
resp = requests.get(url=url + str(i))
data = resp.json()
st.write(data)
