see: https://www.django-rest-framework.org/tutorial/quickstart/#quickstart

name: admin
email: admin`@example.com
password: password123

### UserSerializeerを作る

シリアライザーとは
- オブジェクトとJSONなどのデータのマッピングやバリデーションを行う




models にあるモデルクラス User をインポートして
UserSerializer の model にセットする
fields にタプル型でセット(要素は使っているフィールド)

リレーションをハイパーリンクで示すかプライマリキーで示すかの違い


UserSerializerはrest_frameworkのserializersを


`HyperlinkedModelSerializer`

```
{
    "url": "http://192.168.33.10:8000/users/1/",
    "username": "user1",
    "email": "user1@example.com",
    "groups": [
        "http://192.168.33.10:8000/groups/1/"
    ]
}
```

`ModelSerializer`

```
{
    "url": "http://192.168.33.10:8000/users/1/",
    "username": "user1",
    "email": "user1@example.com",
    "groups": [
        1
    ]
}
```



### Views.pyのなかでCRUD(クレッド)処理する

出来上がったモデルを

### Viewをルーティングする

urls.py

### Settings

ルーティングされたものをsettingする
