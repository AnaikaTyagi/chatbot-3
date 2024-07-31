import streamlit as st
import anthropic

st.write("anthropic_api_key", st.secrets["key"])

# Show title and description.
st.title("Learn More About Your Source")
st.write(
    "Upload a document below! We will extract key points and provide a summary. You can also ask a question about the source for clarification or additional information."
    "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
)
uploaded_file = st.file_uploader("Upload a source", type=("txt","md"))
extracted_data = "extract key data points from this source"
summary = "give me a brief summary of this source"
queston = st.text_input(
    "Ask something about the source",
    disables=not uploaded_file,
)

if uploaded_file:
    article = uploaded_file.read().decode()
    prompt = f"""{anthropic.HUMAN_PROMPT} Here's an article:\n\n<article>
    {article}\n\n</article>\n\n{extracted_data}{anthropic.AI_PROMPT}"""

    client = anthropic.Client(anthropic_api_key)
    response = client.completions.create(
        prompt=prompt,
        stop_sequences=[anthropic.HUMAN_PROMPT],
        model="claude-v3.5",
        max_tokens_to_sample=2,
    )
    st.write("### Answer")
    st.write(response.completion)
    
