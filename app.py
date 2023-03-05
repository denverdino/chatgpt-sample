# -*- coding:utf-8 -*-
# !/usr/bin/python3
import json
import time
import os
import openai
import requests
from flask import Flask, render_template, request, flash, jsonify


app = Flask(__name__)
app.secret_key = 'security-guard'
openai.api_key = os.getenv("OPENAI_API_KEY")

messages=[
            {"role": "system", "content": "You are a helpful assistant."}
        ] 

# Answer the last piece of information
def answer_meg(question):
    messages.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    an_info = response.choices[0].message.content
    return an_info
 
# 路由
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip_req = request.form.get('requestivr')
        print(ip_req)
        try:
            shell = answer_meg(question=ip_req)
            print(shell)
            shell = list(shell)
            resultsh = "".join(shell)
            flash(u'Q: %s\t' % ip_req)
            flash(u'%s\n' % resultsh)
        except Exception as e:
            flash(u'Q: %s\t\t' % ip_req)
            flash(u'\t抱歉，ChatGPT负载过高,请稍后重试\t%s' % e)
 
    return render_template('send.html')
 
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
