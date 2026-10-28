import json
import os
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
            {"role": "assistant", "content": "Chat history cleared. How can I help you today?", "score": None, "matched": True}
        ]
        st.rerun()

    # Admin view for logged questions
    with st.expander("📊 Admin: Unanswered Queries"):
        if os.path.exists("unanswered_logs.json"):
            with open("unanswered_logs.json", "r", encoding="utf-8") as f:
                logs = json.load(f)
            st.write(f"Total unhandled: {len(logs)}")
            st.json(logs[-5:] if logs else [])
        else:
            st.write("No unhandled queries logged yet.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! How can I help you today?", "score": None, "matched": True}
    ]

# Render chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message.get("score") is not None and message["score"] > 0:
            st.caption(f"🎯 Match confidence: {int(message['score'] * 100)}%")
        if not message.get("matched", True):
            st.info("✉️ Need human assistance? Contact support directly at **support@example.com** or call **1-800-555-0199**.")

user_prompt = st.chat_input("Type your question here...") or selected_query

if user_prompt:
    st.session_state.messages.append({"role": "user", "content": user_prompt, "score": None, "matched": True})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    bot_reply, score, matched = matcher.get_response(user_prompt)

    st.session_state.messages.append({"role": "assistant", "content": bot_reply, "score": score, "matched": matched})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
        if score > 0:
            st.caption(f"🎯 Match confidence: {int(score * 100)}%")
        if not matched:
            st.info("✉️ Need human assistance? Contact support directly at **support@example.com** or call **1-800-555-0199**.")
