from flask import Flask, render_template, request
from google import genai
import os

app = Flask(__name__)

client = genai.Client(
    api_key=os.environ["GEMINI_API_KEY"]
)

@app.route("/", methods=["GET", "POST"])
def index():

    comment = ""

    if request.method == "POST":

        task = request.form["task"]

        with open(
            "prompts/system_prompt.txt",
            "r",
            encoding="utf-8"
        ) as f:
            prompt_template = f.read()

        prompt = prompt_template.replace(
            "{TASK}",
            task
        )

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        comment = response.text

    return render_template(
        "index.html",
        comment=comment
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)