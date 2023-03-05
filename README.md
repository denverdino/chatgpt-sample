# chatgpt-sample

A toy project

```
docker build -t chatgpt-sample .
docker run -it --rm -p 5000:5000 -e OPENAI_API_KEY=sk-XXX chatgpt-sample
```


The WebUI is borrowed from
https://www.cnblogs.com/security-guard/p/flask-chatgpt.html