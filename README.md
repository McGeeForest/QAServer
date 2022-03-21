# QAServer
a server to show the model runing.
项目为前后端分离结构，前端采用Vue搭建，后端基于Flask和Torch等搭建，基于HTTP接口进行通信。

| 前端 | 后端 |
| ------- | ------- |
|     [Vue argon design system](https://github.com/creativetimofficial/vue-argon-design-system)    |    [Flask](https://github.com/pallets/flask)     |
|./frontpage/vue-argon-design-system/ | ./|

## 1.后端
### 1.1 依赖
在系统根目录下运行：

```
pip instll -r requirments.txt
```

requirments.txt
```
pandas==1.1.5
nltk==3.6.6
transformers==4.12.5
torch==1.7.0
urllib3==1.26.7
Flask==2.0.3
Flask-Cors==3.0.10
```
### 1.2 运行

在系统根目录下运行：

```
python Api.py
```

## 2. 前端
### 2.1 依赖
采用npm安装依赖：

```
cd ./frontpage/vue-argon-design-system/
npm run install
```


### 2.2 运行

```
npm run serve
```



