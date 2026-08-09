import os
import gradio as gr

def responder(texto):
    return f"Você digitou: {texto}"

demo = gr.Interface(
    fn=responder,
    inputs="text",
    outputs="text",  # ESSA LINHA É A CHAVE
    title="MatrixHBR"
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    demo.launch(server_name="0.0.0.0", server_port=port)
