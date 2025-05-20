import streamlit as st

# Set up the page
st.set_page_config(page_title="Our Team Values", layout="centered", page_icon="🤝")

# Custom CSS to style value cards
st.markdown("""
    <style>
    .value-card {
        background-color: #f5f9ff;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
        border-radius: 1rem;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .value-title {
        font-size: 1.4rem;
        font-weight: bold;
        color: #1a73e8;
        margin-bottom: 0.5rem;
    }
    .section-label {
        font-weight: bold;
        margin-top: 0.8rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and intro
st.title("💙 Our Team Values")
st.markdown("Explore what each of our team values means, and how we bring them to life every day. Click to expand a value below:")

# Placeholder values
team_values = [
    {
        "name": "Team Spirit",
        "definition": "Supporting and uplifting each other through collaboration.",
        "do": "Offer help when a teammate is struggling.",
        "dont": "Ignore a teammate’s request for support."
    },
    {
        "name": "Accountability",
        "definition": "Taking ownership of your work and responsibilities.",
        "do": "Own up to your mistakes and fix them.",
        "dont": "Blame others when something goes wrong."
    },
    {
        "name": "Curiosity",
        "definition": "Asking questions and seeking to understand deeply.",
        "do": "Explore new ideas and ask why.",
        "dont": "Dismiss new concepts without trying to learn."
    },
]

# Loop through values and display each as a styled expander
for value in team_values:
    with st.expander(f"🔹 {value['name']}"):
        st.markdown(f"<div class='value-card'>", unsafe_allow_html=True)
        st.markdown(f"<div class='value-title'>{value['name']}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='section-label'>Definition:</div> {value['definition']}", unsafe_allow_html=True)
        st.markdown(f"<div class='section-label'>✅ Do:</div> {value['do']}", unsafe_allow_html=True)
        st.markdown(f"<div class='section-label'>❌ Don't:</div> {value['dont']}", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
