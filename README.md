# TechJam Team-2 Django プロジェクト README


## 環境構築手順

### 1. 仮想環境を作成・有効化

```bash
python3 -m venv venv
source venv/bin/activate
```

※ ターミナルの先頭に `(venv)` が表示されていればOKです。

---

### 2. 依存関係をインストール

```bash
pip install django python-dotenv
```

---

### 3. `.env` ファイルを作成（重要）

プロジェクト直下  
（`manage.py` と同じ階層）に `.env` ファイルを作成してください。

```env
SECRET_KEY=django-insecure-xxxxxxxxxxxxxxxx
DEBUG=True
```

※ `SECRET_KEY` は各自適当な文字列でOK  
※ `.env` は Git 管理しません

---

### 4. 初期マイグレーション（必須）

```bash
python3 manage.py migrate
```

---

### 5. サーバー起動

```bash

python3 manage.py runserver

```

ブラウザで以下にアクセスしてください。

```
http://127.0.0.1:8000/
```

---

## ディレクトリ構成について（チームメンバー向け）

### techteam2/

プロジェクト全体の設定フォルダです。

- settings.py  
- urls.py  
- wsgi.py  
- asgi.py  

🚨 **基本的に触らないでください！**  
編集が必要な場合は、必ず事前に Slack でリーダーに相談してください。

---

### app/

アプリケーション本体のフォルダです。

- views.py：画面の処理を書く  
- urls.py：URLと画面を紐づける  
- models.py：データ構造（必要な場合のみ）  

👉 バックエンド担当は基本ここを触ります。

---

### templates/

HTML（画面）を置くフォルダです。

- top.html  
- route.html（※ 仮名。画面構成確定後に変更予定）

👉 フロント担当・デザイン担当の主な作業場所です。

---

### techteam2/static/

CSS・画像などの見た目用ファイルを置くフォルダです。

```text
static/
├── css/
│   └── style.css
└── img/
```

HTML から CSS を読み込むとき：

```html

{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">

```

---

### db.sqlite3

データベースファイルです。

- SQLite 使用  
- 基本触らなくてOK  
- 削除・編集しないでください  
- Git 管理しません  

---

### manage.py

Django を動かすためのコマンド用ファイルです。

```bash

python3 manage.py runserver

```

---

## 管理画面（スーパーユーザー）

各自ローカル環境で作成してください。

```bash

python3 manage.py createsuperuser

```

管理画面：

```
http://127.0.0.1:8000/admin/
```

※ 共通アカウントは使用しません

---

## Git 運用ルール（重要）

### やること

- clone する  
- ブランチを作る  
- 自分の担当コードを書く  
- commit して push する  

### やらないこと

- main ブランチを直接触る  
- 他人のブランチを merge する  
- 他人のコードを勝手に直す  

※ merge・コンフリクト対応はリーダーが行います。

---

## Git コマンド（コピペ用）

```bash

git clone [githubのURL]
cd [リポジトリ名]
code .

git switch -c feature-[自分の名前 or 機能名]

git add .
git commit -m "作業内容"
git push origin feature-[ブランチ名]

git branch
```

---

## まとめ（超重要）

- HTML → templates/  
- CSS・画像 → static/  
- Python（処理） → app/  
- 設定ファイル → techteam2/techteam2/（触らない）  

---

## 困ったら

- よく分からない  
- 触っていい場所か不安  
- 用語が分からない  

👉 遠慮なく聞いてください。  
質問＝ドキュメント改善なので大歓迎です！
