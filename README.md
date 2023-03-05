# chatgpt-sample

A toy project


## Build image

```
docker build -t chatgpt-sample .
docker run -it --rm -p 5000:5000 -e OPENAI_API_KEY=sk-XXX chatgpt-sample
```

## Test with Kubernetes


```
$ echo -n '<Your OpenAI API Key>' | base64
```


Create secret.yaml as following

```
apiVersion: v1
kind: Secret
metadata:
  name: chatgpt-apikey
data:
  apiKey: <Your OpenAI API Key in BASE64>
```

Deploy application

```
$ kubectl apply -f secret.yaml
$ kubectl apply -f deployment.yaml
```

```
$ kubectl get pod -l app=chatgpt-sample
NAME                              READY   STATUS    RESTARTS   AGE
chatgpt-sample-6ccfbb454d-44k7z   1/1     Running   0          8m16s
$ kubectl get service chatgpt-sample
NAME             TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)        AGE
chatgpt-sample   LoadBalancer   172.21.10.39   xx.xx.xx.xx     80:32256/TCP   26m
$ echo $(kubectl get service chatgpt-sample -o jsonpath="{.status.loadBalancer.ingress[*].ip}")
xx.xx.xx.xx
```

Open your browser and play with it

## Thanks


The WebUI is borrowed from
https://www.cnblogs.com/security-guard/p/flask-chatgpt.html