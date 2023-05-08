import streamlit as st
import functions


todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.add_todos(todos)
    st.session_state["new_todo"] = ""


st.title("Mussukoiden lista")
st.subheader("Pyllykki.")
st.write("Mussukaa")

#takas
for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=i)
    if checkbox:
        todos.pop(i)
        functions.add_todos(todos)
        del st.session_state[i]
        st.experimental_rerun()


st.text_input(label="", placeholder="Lisää listalle...",
              on_change=add_todo, key="new_todo")


