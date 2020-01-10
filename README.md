# Excel2Data 

## 环境
    python3+

## 安装
```
    easy_install E2D-0.0.1-py3.7.egg
```

## 设置配置文件 config/config.xml

| 字段 | 定义 |
|----|----|
| res | excel 源文件夹路径|
| output | 单一 data 文件路径|
| outputJson | json 文件输出文件夹路径|

## excel文档读取并输出
```
    from E2D import entrance
    entrance.build(arg1, arg2)

    # arg1 : True 单一文件
    # arg2 : True 每个 excel 文档导出 单独 json
```