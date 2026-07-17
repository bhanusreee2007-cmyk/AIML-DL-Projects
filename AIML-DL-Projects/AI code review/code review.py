import google.generativeai as genai
import gradio as gr

genai.configure(api_key="")
def review_code(code,input_programming_language,output_programming_languages):
  prompt=f"""
  Review this code from input_programming_language to output_programming_languages.
  provide:
  1.Summary
  2.Bugs
  3.Performance Improvements
  4.Code style
  5.Security issues
  6.Improved code
  7.Rating out of 10
  Code:
  {code}
  Input Programming Language:
  {input_programming_language}
  Output Programming Language:
  {output_programming_languages}
  """
  response=client.models.generate_content(
      model="gemini-2.5-flash",
      contents=prompts
      )
  return response.text
demo=gr.Interface(
    fn=review_code,
    inputs=[
    gr.Textbox(label="Code"),
    gr.Dropdown(
        ["python","java","html","css"],
        label="input_programming_language"
    ),
    gr.Dropdown(
        ["python","java","html","css"],
        label="output_programming_language"
    ),
    ],
    outputs="markdown",
    title=" AI Code Review (Gemini)"
)
demo.launch()
