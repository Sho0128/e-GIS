# e-GIS

### 開発環境
* Python 3.6.5 (virtualenv)
* Django 2.1.3
* PostgreSQL 9.6


### ディレクトリ構成


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


### pythonの環境整備
#### macの場合 (pyenvがインストール済み前提)
python 3.6.5のインストール

```
pyenv install 3.6.5
```

