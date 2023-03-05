FROM python:3.9
WORKDIR /root/chatgpt/chatGPT
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.douban.com/simple/
COPY . .
ENTRYPOINT ["python3"]
CMD ["app.py"]