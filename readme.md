# スカウト機能バックエンドリポジトリ

## 概要

TechFUL+の追加機能(Add-On)となる新スカウト機能のバックエンドのソースを管理するリポジトリとなります。
[Github: triple-four/techful-api](https://github.com/triple-four/techful-api)をベースに作成しています。

## ブランチ運用

開発中はシンプルなGithub Flow**っぽいもの**を採用して効率的な開発を、リリース後はgit-flow**っぽいもの**に切り替えて安定運用を目指せればと思います。

![ブランチ運用-Github Flowっぽいもの](/github-branch-strategy.png)

### 作業の流れ

(1) `main` ブランチから作業用のブランチを切る

(2) (1)で切った作業用のブランチで開発を行い、スモークテストを行う

(3) `main` と `development` ブランチに向けたPull Requestを作成する

(4) (3) でPull Requestを作成すると、継続的インテグレーション(Continuous Integration; CI)により自動で単体テストがトリガされる
この単体テストが通った後、チームメンバにレビュを依頼する

(5) (4) のチームメンバによるレビュによりPull RequestがApproveされたら `main` にマージする

(6) `main` ブランチの内容が検証環境にデプロイされるので、同環境内で統合テスト(Integration Testing; IT)およびE2Eテスト(End to End Test; E2E Testing) を行う

`development` ブランチへはPull Requestベースであれば自由にマージできるが、`main` はメンバ1人からのApproveがなければマージできないようになっています。

### Pull Request作成時のルール

Assigneeには基本的に自分を指定してください。また、適切なラベルの設定もお願いします。

## 環境構築

### 前提条件

WindowsおよびmacOSで開発することを想定しています。
Windows・macOS共に[Docker Desktop](https://www.docker.com/products/docker-desktop/)が必要です。
また、Windowsの場合は[Windows Subsystem for Linux 2; WSL2](https://learn.microsoft.com/ja-jp/windows/wsl/install)も必要です。

#### .wslconfigの作成（Windowsのみ）
WSL2のインストールが終わったら、メモリ使用量の制限をすることを強くおすすめします（デフォルトでは搭載メモリの8割まで使おうとする）。

`%USERPROFILE%`配下に`.wslconfig`を **BOM無しUTF-8で作成する (非常に重要)** することで実現できます。

`.wslconfig`の例：

```
[wsl2]
memory=4GB
swap=0
```

### 起動方法

コマンド プロンプト (Windows)もしくはターミナル (Mac)からこのreadme.mdがあるディレクトリまで移動して、

```
docker compose up -d
```

で起動できるはずです。
`docker-compose.yml` に記載されたコンテナが立ち上がって、Docker Desktop上のような表示になったら起動できています。

### ローカルに開発用のデータを投入する方法

```
make localimport
```

で、`app/commands/fixtures/csv` 配下にあるCSVファイルを読み込んで該当するテーブルにデータを投入することができます。

![Docker Desktop](/docker-desktop-successfully-running.png)

### Google Chromeおよび派生ブラウザ(Chromium, Vivaldi, Brave, etc.)をお使いの方へ

[いっしきまさひこBLOG: Google Chromeでlocalhostへアクセスするとhttpsにリダイレクトされてしまう問題の解消方法](https://blog.masahiko.info/entry/2020/03/10/000025)

どうやら初期状態ではlocalhostへの接続が勝手にHTTPSに変換される (HSTS; HTTP Strict-Transport-Security) ので、上記手順で無効化してください。
