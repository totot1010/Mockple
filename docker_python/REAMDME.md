# Docker+Pythonで環境構築してみる

# はじめに

今回は Docker を使って Python の環境を作っていきたいと思います。  
Docker のインストールは完了していることを前提に進めていきます。

# 環境

Docker と Docker Compose のバージョンは以下の通りです。

```
Docker version 20.10.22, build 3a2c30b63a
Docker Compose version v2.13.0
```

# Dockerの設定

## ファイル構成
まず、以下のようなファイル構成を作ってください。
```
docker_python
├── Dockerfile
├── REAMDME.md
├── app
│   └── sample.py
└── docker-compose.yml
```

## Dockerfile
