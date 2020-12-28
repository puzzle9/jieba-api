# 结巴分词 python docker api

- <https://github.com/fxsjy/jieba>

# docker 部署

```sh
docker-compose -f ./docker-compose.yml up -d --build
```

# 直接部署

```sh
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:5000 app:app
```

# api 使用

## 开始

```sh
curl --location --request GET 'http://127.0.0.1:5000/'
```

```json
{
    "time": "Tue, 22 Dec 2020 13:44:34 GMT"
}
```

## 直接分词

```sh
curl --location --request POST 'http://127.0.0.1:5000/' \
--form 'mode="cut_for_search"' \
--form 'body="陕西西安肉夹馍"' \
--form 'is_cut_all=""'
```

```json
{
    "datas": [
        "陕西",
        "西安",
        "肉夹馍"
    ],
    "mode": "cut_for_search"
}
```

### 参数
- `mode` 分词模式 `cut` `cut_for_search`
- `body` 分词内容
- `is_cut_all` 是否采用全模式

## 词性标注

```sh
curl --location --request POST 'http://127.0.0.1:5000/posseg' \
--form 'body="我爱吃陕西西安肉夹馍,爽"'
```

```json
{
    "datas": {
        "n": [
            "肉夹馍"
        ],
        "nr": [
            "爽"
        ],
        "ns": [
            "陕西",
            "西安"
        ],
        "r": [
            "我"
        ],
        "v": [
            "爱",
            "吃"
        ],
        "x": [
            ","
        ]
    },
    "words": [
        "我",
        "爱",
        "吃",
        "陕西",
        "西安",
        "肉夹馍",
        ",",
        "爽"
    ]
}
```