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
ssh -v -i "pem がある場所" "サーバー@フル url"

5. 接続

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
