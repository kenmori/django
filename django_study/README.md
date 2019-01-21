this project is toutorial of udemy

username: morita
mail: kennjimoritata@yahoo.co.jp
password: morita

### EC2 インスタンスへの構築

1.AMI ubuntu
インスタンスタイプ t2.micro
作成
ssh のキーを新規作成
インスタンスを running
「インスタンスへの接続」 4 の F

コピーしておく
`cp コピー元 コピー先`

`cp ~/Desktop/\*\*.pem ~/.ssh/`

パーミッションを確認する
ls -la ~/.ssh/\*\*\*.pem
sudo でしか読み込めない場合がある

以下のコマンドを叩く(コネクトする際に AWS で提示されているもの)
ssh -v -i "pem がある場所" " ubuntu@サーバー名"

5. 接続

キーがあるフォルダを絶対パスで指定して

```
sudo ssh -v -i "/Users/kenjimorita/.ssh/**.pem" ubuntu@ec*-**-***-***-***.ap-northeast-1.compute.amazonaws.com
```

6. 入ったら

ソフトウェアの更新

```
sudo apt-get update
```

必要なパッケージをインストール

```
sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
```

ローカルとの違いは、
ubuntu は python2 と python3 が共存できるので
`python3`と明示的にコマンドをうつ必要がある

`$ python3`

### 49 　 PostgreSQL 設定

デフォルトユーザーで実行する
`sudo -u postgres psql`

コマンド待ち状態になるので

データペースを作成

```
postgres=# CREATE DATABASE myblogapp
postgres-# ;
CREATE DATABASE
postgres=#
```

ユーザーを作成

```
postgres=# CREATE USER mybloguser WITH PASSWORD 'morita';
CREATE ROLE
postgres=#
```

```
postgres=# ALTER ROLE mybloguser SET client_encoding TO 'utf8';
ALTER ROLE
postgres=# ALTER ROLE mybloguser SET default_transaction_isolation TO 'read committed';
ALTER ROLE
```

タイムゾーンの設定

```
postgres=# ALTER ROLE mybloguser SET timezone TO "UTC+9";
ALTER ROLE
```

権限を付与

```
postgres=# GRANT ALL PRIVILEGES ON DATABASE myblogapp TO mybloguser;
GRANT
```

postgres を抜けるときはバックスラッシュ `shift + ¥`

ps aux で postgress が起動していることがわかる
(インストール時に ngix と postgress が起動するから)

50. vertualenv

sudo -H pip3 install --upgrade pip

sudo -H pip3 install virtualenv

環境を作成

virtualenv py36

コマンドラインから ubuntu の Linux で環境を実行するには、まず
activate 用のファイルができているか確認
ls py36/bin

あるのでそれを実行する。
source py36/bin/activate

仮想環境がアクティベートされた
(py36) ubuntu@ip-\\\\\\\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\\\\\\\*-\\\\\\\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\\\\\\*-\\\\\\\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\\\\\\*-\\\\\\\\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\\\\\\*\\\\\\\\\\\\\\\\\\\\*:~\$

これで Django に必要な環境を整えて Django のプロジェクトをアップロードして動かしていく

```
pip install django gunicorn psycopg2
```

・gunicorn(グニコーン)・・・アプリケーションサーバー。python の内臓サー D バではなく負荷に耐えられる本番に近いソフトウェア。最終的には python の内臓サーバで動かしたり、 Ngix と連携して Web サーバを経由してグニコーンを呼ぶ、さらにグニコーンが Django を呼ぶように作る
・psycopg2(サイコ PG2)・・・django と postgres を接続するためのパッケージ

### デプロイ

Django プロジェクトを ubuntu の/home/以下にアップロードして動かす

ローカルから ubuntu の OS にアクセスしてファイルを転送する
(ssh のサーバには SCP のクライアントを使って転送する)

#############

PostgreSQL 接続アダプターの名称変更対応
セクション 4、レクチャー 52
Django でマイグレーションを実行する際にインストール時の構成によっては、PostgreSQL 接続アダプターのエラーが出ることがあります。

その場合は、以下のコマンドを実行して最新のパッケージを追加してみてください。

\$ pip install psycopg2-binary

#############

### Mac からファイルを EC2 インスタンスへ転送する方法

・FileZila

プロトコル : aws の IPv4 パブリック IP
プロトコル : SFTP
ログオンの種類: 鍵タイプ
鍵ファイル: pem を参照するようにする

接続

手動で転送
zip ファイルをそのまま
フォルダ(myblogapp)を作り、その直下に転送
/home/ubuntu/myblogapp/myblogapp.zip

ssh で入って、unzip する

sudo apt-get install unzip
sudo unzip myblogapp.zip

### migrat する

ssh 後、x アクティベートに入って、

画像ファイルを扱うので`pillow`をインストールする必要がある

```
pip install pillow
```

おうふ

```
(py36) ubuntu@ip-***:~/myblogapp/myblogapp/myblogapp$ ls
__init__.py  __pycache__  settings.py  urls.py  wsgi.py
```

settings.py の ALLOWED_HOSTS にサーバーにアクセスできる IP アドレスを追加する

```
ALLOWED_HOSTS = ['13.***.***.***']
```

データベースを sqlite3 から変更する

```
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'myblogapp',
        'USER': 'myblogappuser',
        'PASSWORD': 'morita',
        "HOST": 'localhost',
        'PORT': '',
    }
}
```

python manage.py makemigrations

python3 manage.py migrate

EC2 インスタンスのセキュリティグループをインバウンド 8000 番 0.0.0.0/0 を開ける

python3 manage.py runserver 0.0.0.0:8000

ブラウザからは IP アドレスをコピペしてアクセス
`Invalid HTTP_HOST header: '0.0.0.0:8000'. You may need to add '0.0.0.0' to ALLOWED_HOSTS.`が出たら、
それは IP アドレスでの訪問先間違えか、ホスト許可が必要
settings.py の ALLOWED_HOSTS を変更
インスタンスを再起動すると IP アドレスが変わるのでそこと ssh へのコマンドを変える必要がある

http://52.194.248.106:8000/posts/
