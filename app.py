import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="AI Text Generator",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Text Generator")
st.write("Generate text using Hugging Face GPT-Neo")

@st.cache_resource
def load_model():
    generator = pipeline(
        "text-generation",
        model="EleutherAI/gpt-neo-125M"
    )
    return generator

generator = load_model()

prompt = st.text_area(
    "Enter your prompt",
    placeholder="Example: Artificial Intelligence is"
)

max_tokens = st.slider(
    "Maximum New Tokens",
    min_value=20,
    max_value=150,
    value=50,
    step=10
)

temperature = st.slider(
    "Temperature",
    min_value=0.1,
    max_value=1.5,
    value=0.7,
    step=0.1
)

if st.button("Generate Text"):
    if prompt.strip():
        with st.spinner("Generating text..."):
            result = generator(
                prompt,
                max_new_tokens=max_tokens,
                temperature=temperature,
                do_sample=True,
                return_full_text=False
            )

        generated_text = result[0]["generated_text"]

        st.subheader("Generated Text")
        st.write(generated_text)

    else:
        st.warning("Please enter a prompt.")