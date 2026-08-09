import gradio as gr

def calcular(conta):
    try:
        resultado = eval(conta)
        return f"✅ Resultado: {resultado}"
    except:
        return "❌ Erro! Use só números e +-*/"

# LINK DA SUA LOGO AQUI
URL_LOGO = "https://raw.githubusercontent.com/HelberScamardi/MatrixHBR/refs/heads/main/ChatGPT%20Image%207%20de%20ago.%20de%202026%2C%2018_49_29.png"

with gr.Blocks(theme=gr.themes.Default(), css=".gradio-container {background-color: #000000} h1 {color: #00FF00} h2 {color: #00FF00}") as demo:
    
    # AQUI ENTRA A LOGO
    gr.Image(value=URL_LOGO, show_label=False, height=200)
    
    gr.Markdown("<h1 style='text-align: center'>MATRIXHBR</h1>")
    gr.Markdown("<h2 style='text-align: center'>Intelligent Problem Solver</h2>")
    
    with gr.Row():
        input_conta = gr.Textbox(label="Digite sua conta", placeholder="Ex: 15*4 + 10")
        output_resultado = gr.Textbox(label="Resposta", interactive=False)
    
    with gr.Row():
        btn_calcular = gr.Button("▶ Calcular", variant="primary")
        btn_limpar = gr.Button("🧹 Limpar")

    btn_calcular.click(fn=calcular, inputs=input_conta, outputs=output_resultado)
    btn_limpar.click(fn=lambda: ("", ""), inputs=None, outputs=[input_conta, output_resultado])

demo.launch()
