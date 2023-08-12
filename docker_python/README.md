# Docker Compose+Pythonで環境構築してみる

# はじめに

今回はDocker Composeを使ってPythonの環境を作っていきたいと思います。  
Dockerのインストールは完了していることを前提に進めていきます。

# 環境

DockerとDocker Composeのバージョンは以下の通りです。

```
Docker version 20.10.22, build 3a2c30b63a
Docker Compose version 2.20.3
```

# Dockerの設定
Dockerを使うことによってローカルやリモートマシン上での環境構築を簡単に自動化することができます。

## ファイル構成
まず、以下のようなファイル構成を作っていきます。
```
docker_python
├── Dockerfile
├── app
│   └── sample.py
└── docker-compose.yml
```

## Dockerfile
Dockerは、Dockerfileを読み込むことで自動的にDocker Imageを作成します。  
Dockerfileは、ユーザーがDocker Imageを作成するために必要なコマンドを記載したテキストファイルです。

Dockerfileは次のように記述していきます。
```docker
FROM python:3.9

WORKDIR /app

COPY . .
```

- FROM python:3.9
  - ベースとなるイメージを指定しており、Dockerfileは*FROM*の命令から始めなければならないというルールがあります。
- WORKDIR /app
  - 作業ディレクトリの指定しています。作業ディレクトリを指定することで、その後のRUN, CMD, ENTRYPOINT, COPY, ADDなどの命令がそのディレクトリで実行されます。
- COPY . .
  - ファイルやディレクトリをコンテナのイメージにコピーしています。  
  - 最初の `.` はビルドコンテキスト(通常はDockerfileがあるディレクトリ)の中の全てのファイルとディレクトリを指します。  
  - 2番目の `.` はコンテナ内の作業ディレクトリを指します。この作業ディレクトリは、WORKDIR命令で指定されたディレクトリです。もしWORKDIRが設定されていなければ、ルートディレクトリを指します。

## docker-compose.yml
docker-compose.ymlは複数のDockerコンテナを一緒に定義・実行するための設定ファイルです。  
YAML形式で記述され、各サービスを個別に定義します。

```yml
version: "3"
services:
  docker_python:
    container_name: python
    build:
      context: .
      dockerfile: Dockerfile
    working_dir: "/app/"
    tty: true
    volumes:
      - .:/app
```

- version: 
  - 使用するdocker-composeファイルフォーマットのバージョンを指定します。
- build: 
  - Dockerfileのあるディレクトリやビルドの指定します。
  - context: .
    - ビルドコンテキストを指定します。. はカレントディレクトリを意味します。
  - dockerfile： Dockerfile
    - イメージのビルドに使用するDockerfileの名前を指定します。この場合、カレントディレクトリにあるDockerfileという名前のファイルを指します。
- working_dir: "/app/"
    - コンテナ内の作業ディレクトリを/app/に設定する。
- tty: true
  - 擬似TTYを割り当てるもので、ターミナルでコンテナとやり取りしたい場合に便利です。
- .:/app
  - ホストのカレントディレクトリをコンテナ内の /app にマッピングします。これによって開発時にホストのappディレクトリで行った変更が即座にコンテナ内に反映されます。


## sample.py
動作を確認するため、sample.pyには以下の一行を記載しておきます。
```python3
print("Hello World!")
```

# Dockerのコンテナのビルドと起動
以下のコマンドでコンテナの作成と起動を行います。
```bash
cd docker_python
docker compose up -d --build
```

# コンテナへの接続とHello World!の出力
まず、コンテナに接続します。
```bash
docker exec -it python bash
```

コンテナに接続した状態で以下を実行すると
```bash
root@57ce8b6f9197:/app# python3 app/sample.py
```

Hello Worldが出力されます。
これで、DockerとPythonで環境構築することができました。
```bash
Hello World!
```

# おわりに
今回はdocker-composeとPythonで環境構築を行ってみました。  
Dockerは非常に便利などで今後も積極的に使っていきたいと思います。

以上です。お疲れ様でした。