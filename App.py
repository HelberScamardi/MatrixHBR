import gradio as gr

def ia_matrizhbr(pergunta):
    return f"IA MatrizHBR: Recebi '{pergunta}'. Bora automatizar e escalar! 🚀"

interface = gr.Interface(
    fn=ia_matrizhbr,
    inputs=gr.Textbox(label="Fale com a MatrizHBR"),
    outputs=gr.Textbox(label="Resposta"),
    title="MatrizHBR IA",
    description="Automatize tarefas chatas para escalar e dominar"
)
interface.launch()
