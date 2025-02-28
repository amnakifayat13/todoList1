import streamlit as st
import time

st.title("Todo List")

if 'todo' not in st.session_state:
    st.session_state.todo = []
if "edit_index" not in st.session_state:
    st.session_state.edit_index = None
if "button_disabled" not in st.session_state:
    st.session_state.button_disabled = False

tasks = st.text_input("enter your Item here")


if st.button("Add Items"):
    st.session_state.todo.append(tasks)
    st.session_state.button_disabled = True
    st.rerun()
st.session_state.button_disabled = False
    
         

for idx, i in enumerate(st.session_state.todo):
    col1, col2,col3 = st.columns(3)
    with col1:
        st.write(idx,i)
    with col2:
        if st.button("❌",key=f"{idx}"):
            st.session_state.todo.pop(idx)
            st.rerun()
    with col3:
        if st.button("Update", key=f"update_{idx}"):
            st.session_state.edit_index = idx 
            st.rerun()

if st.session_state.edit_index is not None:
    index = st.session_state.edit_index
    new_task = st.text_input("Update task:", value=st.session_state.todo[index])

    if st.button("OK"):
        st.session_state.todo[index] = new_task
        st.session_state.edit_index = None  
        st.rerun()

if st.button("Clear All items"):
    st.session_state.todo.clear()
    st.rerun()
    


        


    
       



