import gradio as gr
from runner import gen


demo = gr.Interface(fn=gen, inputs="text", outputs="text")

demo.launch() 