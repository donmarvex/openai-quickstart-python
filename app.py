import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = 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

# model_engine = "text-davinci-002"


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        query = request.form["query"]
        query = query.strip()
        query += "\n\n###\n\n"  # " ->"
        print(query)
        response = openai.Completion.create(
            model= 'ada:ft-chatbot-test-2023-04-02-22-40-55',
            # 'ada:ft-chatbot-test-2023-04-02-06-46-52',
            # 'ada:ft-brokemenot-llc-2023-03-28-21-30-05',
            # 'ada:ft-brokemenot-llc-2023-03-21-19-49-43',
            # 'curie:ft-brokemenot-llc-2023-03-09-06-12-37',
            # 'ada:ft-brokemenot-llc-2023-03-09-04-15-52',  # 'davinci:ft-brokemenot-llc-2023-03-07-19-46-06',
            prompt=generate_prompt(query),
            temperature=0.0,
            top_p=0.99,
            n=1,
            max_tokens=70,
            stop=["\n"]  # " ###STOP###"
        )
        print(response)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(query):
    return query.capitalize()
