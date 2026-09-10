# AI Text Generator using Streamlit

An AI-powered text generation web application built using Python, Streamlit, Hugging Face Transformers, and GPT-Neo 125M.

## Features

- AI-powered text generation
- Hugging Face pretrained model
- Streamlit web interface
- Adjustable maximum token generation
- Adjustable temperature
- Simple and user-friendly interface
- No API key required

## Technologies Used

- Python
- Streamlit
- Hugging Face Transformers
- PyTorch
- GPT-Neo 125M

## Model

This project uses:

EleutherAI/gpt-neo-125M

The model is loaded using the Hugging Face Transformers pipeline API.

## Project Structure

AI-Text-Generator/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

## Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_LINK

Create a virtual environment:

python -m venv venv

Activate the environment:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Run the Application

streamlit run app.py

## How It Works

User enters a text prompt.

↓

Streamlit receives the prompt.

↓

Hugging Face Transformers processes the prompt.

↓

GPT-Neo generates text.

↓

The generated text is displayed in the Streamlit application.

## Future Enhancements

- Download generated text
- Multiple text generation options
- Improved UI
- Text summarization
- More advanced language models
