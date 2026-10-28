import streamlit as st
from nlp_engine import FAQMatcher

st.set_page_config(
    page_title="FAQ Support Assistant",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Customer FAQ Assistant")
st.caption("Ask questions about shipping, returns, business hours, payment methods, or support.")

@st.cache_resource
def load_matcher():
    return FAQMatcher()

matcher = load_matcher()

with st.sidebar:
    st.header("⚡ Quick Actions")
    st.subheader("Frequently Asked")
    sample_queries = [
        "Business hours?",
        "How can I track my order?",
        "What is your return policy?",
        "Accepted payment methods?"
    ]
    
    selected_query = None
    for q in sample_queries:
        if st.button(q, use_container_width=True):
            selected_query = q
            
    st.divider()
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = [
            {"role": "assistant", "content": "Chat history cleared. How can I help you today?"}
        ]
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.chat_input("Type your question here...") or selected_query

if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    bot_reply = matcher.get_response(user_prompt)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
