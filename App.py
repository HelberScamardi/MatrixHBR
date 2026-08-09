import gradio as gr
import os

def calcular(conta):
    try:
        resultado = eval(conta)
        return f"✅ Resultado: {resultado}"
    except:
        return "❌ Erro! Use só números e + - * / ^"

# TEMA MATRIX VERDE
css = """
body {background: #000 !important;}
.gradio-container {background: #000 !important;}
h1, h3, p {color: #00FF00 !important; text-align: center;}
button {background: #00FF00 !important; color: #000 !important; border: none !important;}
button:hover {background: #00CC00 !important;}
textarea, input {background: #0A0A0A !important; color: #00FF00 !important; border: 1px solid #00FF00 !important;}
"""

with gr.Blocks(css=css, theme=gr.themes.Base(), title="MatrixHBR") as demo:
    
    gr.Image("COLE_O_LINK_DA_LOGO_AQUI", show_label=False, height=280)
    
    gr.Markdown("# MATRIXHBR")
    gr.Markdown("### Intelligent Problem Solver")
    gr.Markdown("---")
    
    with gr.Row():
        entrada = gr.Textbox(label="Digite sua conta", placeholder="Ex: 15*4 + 10")
        saida = gr.Textbox(label="Resposta", interactive=False)
    
    with gr.Row():
        btn_calcular = gr.Button("▶ Calcular", variant="primary", size="lg")
        btn_limpar = gr.Button("🗑️ Limpar", size="lg")
    
    gr.Examples(["2 + 2", "10 * 5", "100 / 4"], inputs=entrada)
    
    btn_calcular.click(fn=calcular, inputs=entrada
