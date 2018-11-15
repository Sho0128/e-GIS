# e-GIS

## 開発環境
* Python 3.6.5 (virtualenv)
* Django 2.1.3
* PostgreSQL 9.6


## ディレクトリ構成


```
e-GIS
├── README.md
├── apps
│   ├── config
│   ├── manage.py
│   ├── map (マップ機能)
│   ├── static
│   ├── templates
│   └── test_app (djangoの動作確認とかpostgresqlの連携確認とかに使用)
├── python (virtualenvで3.6.5環境を作成
│   ├── bin
│   ├── include
│   ├── lib
│   └── pip-selfcheck.json
└── requirements.txt
```


## pythonの環境整備
### macの場合 (pyenvがインストール済み前提)
python 3.6.5のインストール

```
pyenv install 3.6.5
```

プロジェクトのpython環境を3.6.5に設定

```
pyenv local 3.6.5
```

virtualenvをインストール

```
pip install virtualenv
```

ディレクトリ名を指定してvirtualenvを作成

```
python -m virtualenv <dir(今回はpython)>
```

virtualenvの有効化

```
source ./python/bin/activate
```

virtualenv終了

```
deactivate
```

pipで必要なモジュールをインストール

```
(virtualenvを有効にした状態で)
pip install --upgrade pip
pip install -r requirements.txt
```

## PostgreSQLの設定
./apps/config/settings.py で設定

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mapdb',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

PostgreSQL側ではpostgresユーザを作成

```
createuser -P postgres
```

DBを作成 (とりあえず名前はmapdbにしました)

```
createdb mapdb -O postgres
```

## 参考にしたサイト
### Django
[Python Django 入門](https://qiita.com/kaki_k/items/511611cadac1d0c69c54 "Python Django 入門")　　
[Django Girls](https://tutorial.djangogirls.org/ja/ "Django Girls")

### Django Leaflet
[Easy Webmapping with django-leaflet & django-geojson](https://fle.github.io/easy-webmapping-with-django-leaflet-and-django-geojson.html "Easy Webmapping with django-leaflet & django-geojson")　　

