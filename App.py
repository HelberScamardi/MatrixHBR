import os
import gradio as gr

# 1. AQUI TEM QUE TER SEU DEMO
demo = gr.Interface(
    fn=lambda x: f"Você digitou: {x}",  # troca pela sua função
    inputs="text",
    title="MatrixHBR"
)

# 2. E AQUI O LAUNCH
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    demo.launch(server_name="0.0.0.0", server_port=port)
