import streamlit as st
from research_agent.manager_agent import manager_agent
from memory.memory_store import get_memory
st.set_page_config(page_title="AI Multi-Agent System")

st.title("🤖 AI Multi-Agent System")
st.write("Research | Startup Validator | Coding Interview Generator")

query = st.text_input("Ask something")

if st.button("Run Agent"):

    if query.strip() == "":
        st.warning("Please enter a query")

    else:
        result = manager_agent(query)

        st.subheader("Response")
        st.write(result)

st.subheader("Conversation Memory")

memory = get_memory()

for m in memory:
    st.write("User:", m["user"])
    st.write("AI:", m["response"])