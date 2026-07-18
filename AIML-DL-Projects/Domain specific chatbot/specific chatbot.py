!pip -q install -U gradio google-genai
import gradio as gr
from google import genai

# =====================================================
#                GEMINI API CONFIGURATION
# =====================================================

GEMINI_API_KEY = "YOUR_REAL_API_KEY"

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL = "models/gemini-flash-latest"
def medical_assistant(user_query):

    prompt = f"""
You are an AI Medical Assistant.

Rules:
- Provide general health guidance only.
- Do NOT diagnose diseases.
- Do NOT prescribe medicines.
- Suggest healthy lifestyle habits.
- Recommend consulting a doctor for persistent or severe symptoms.
- If symptoms indicate an emergency (such as chest pain, difficulty breathing, severe bleeding, or loss of consciousness), advise immediate emergency medical care.

User Question:
{user_query}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text
    def chat(message, history):

    if history is None:
        history = []

    response = medical_assistant(message)

    history.append({"role": "user", "content": message})
    history.append({"role": "assistant", "content": response})

    return "", history
    with gr.Blocks(title="AI Medical Assistant") as demo:

    gr.Markdown("# 🩺 AI Medical Assistant")
    gr.Markdown("### Your Smart Health Companion powered by Gemini AI")

    chatbot = gr.Chatbot(height=500)

    msg = gr.Textbox(
        placeholder="Ask your health question...",
        label="Your Question"
    )

    with gr.Row():
        send = gr.Button("Send", variant="primary")
        clear = gr.Button("Clear")

    send.click(
        chat,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot]
    )

    msg.submit(
        chat,
        inputs=[msg, chatbot],
        outputs=[msg, chatbot]
    )

    clear.click(
        lambda: ("", []),
        outputs=[msg, chatbot]
    )

    gr.Examples(
        examples=[
            ["I have fever and headache"],
            ["What should I eat during fever?"],
            ["What are the symptoms of diabetes?"],
            ["How to treat a minor burn?"],
            ["What causes high blood pressure?"]
        ],
        inputs=msg
    )

    gr.Markdown(
        """
        ---
        ⚠️ **Disclaimer:** This AI Medical Assistant provides general health information only.
        It does not replace professional medical advice, diagnosis, or treatment.
        """
    )
    demo.launch(share=True)
