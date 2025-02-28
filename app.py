import streamlit as st
import time

st.title("Todo List")
# initialize the todo session_state
if 'todo' not in st.session_state:
    st.session_state.todo = []
add = st.session_state.todo

# initialize the edit_index  session_state
if "edit_index" not in st.session_state:
    st.session_state.edit_index = None


# add input for task
task = st.text_input("enter your Item here", key=f"add_task{add}")


# add items
if st.button("Add Items"):
    if task:
        st.session_state.todo.append(task)
        st.rerun()

for idx, i in enumerate(st.session_state.todo):
    col1, col2,col3 = st.columns(3)
    with col1:
        st.write(idx,i)
    # add remove button with items 
    with col2:
        if st.button("❌",key=f"{idx}"):
            st.session_state.todo.pop(idx)
            st.rerun()
    # update items
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

# clear all items

if st.button("Clear All items"):
    st.session_state.todo.clear()
    st.rerun()
    


        


    
       



