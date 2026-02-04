# 📱 TIKAMITI（チカミチ）

ジム利用者向けの **店舗検索・マシン空き状況確認・運動記録アプリ** です。  
「近くて、空いている店舗を直感的に選べること」と  
「無理なく運動記録を続けられること」を重視して設計しています。

---

## 🔍 アプリ概要

- 現在地から近い店舗を地図風UIで表示
- 店舗ごとの **マシン空き台数** を確認可能
- マシン一覧画面で使用状況を視覚的に把握
- ユーザーごとの **運動時間を日別・月別で記録**
- 同日に複数回の運動も **加算方式で記録可能**
- 会員登録 / ログイン機能あり

---

## 🎯 想定ユーザー

- ジムに入会しているライトユーザー
- 短時間（5〜30分程度）の運動を積み重ねたい人
- 厳密な数値管理より「継続しやすさ」を重視する人

※  
1日に極端な運動時間を入力するようなケースは  
本アプリの主なターゲットではありません。

---

## 🛠 使用技術

### Backend
- Python **3.12.4**
- Django **5.1.2**
- SQLite（開発環境）

### Frontend
- HTML / CSS / JavaScript（Vanilla）
- Material Icons
- スマホ前提のUI


## 🧩 主な機能

###  店舗選択（トップ画面）

- 店舗ピンをタップすると以下を同時に更新
  - 店舗名
  - 徒歩距離
  - マシン空き台数
- SVG + JavaScript による簡易ルート表示

---

###  マシン空き状況

- 店舗ごとにマシン一覧を表示
- 状態別カラー表示
  - 空き：ネオンイエロー
  - 使用中：レッド系
- 管理・検証用として状態切り替え機能を実装

---

### 📝 運動記録

- 日付と分数を入力して記録
- 同日でも **加算方式** で記録可能
- 非同期通信（fetch）を使用
- 記録後は画面遷移せず数値のみアニメーション更新

---

### 👤 認証機能

- Django標準認証をベースに実装
- カスタムUserモデルを使用
- サインアップ後は自動ログイン
- ログイン / ログアウト対応

---

##  セットアップ方法

```bash
# 仮想環境作成
python -m venv venv
source venv/bin/activate

# 依存関係インストール
pip install django python-dotenv

# マイグレーション
python manage.py makemigrations
python manage.py migrate

# ダミーデータ投入
python manage.py dummy_data

# サーバー起動
python manage.py runserver

---

## 📂 ディレクトリ構成（抜粋）
---
techteam2/
├── app/
│   ├── models.py        # Store / Machine / ExerciseLog
│   ├── views.py         # トップ・マシン一覧・運動記録API
│   └── management/
│       └── commands/
│           └── dummy_data.py
│
├── accounts/
│   ├── models.py        # カスタムUserモデル
│   ├── forms.py         # サインアップ / ログインフォーム
│   └── views.py
│
├── templates/
│   ├── top.html
│   ├── machines.html
│   └── accounts/
│       ├── login.html
│       └── signup.html
│
├── static/
│   ├── css/
│   └── img/
└── db.sqlite3


