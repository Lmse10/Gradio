import gradio as gr
gr.close_all()

def greet(name):
  return "Hello, "+ name + "!"

demo = gr.Inteference(
  fn=greet,
  input=[gr.Textbox(label="Name:")],
  outputs=[gr.Textbox()],
)

demo.launch()
