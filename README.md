# Excel2Data 

## 环境
    python3+

## 安装
```
    easy_install E2D-0.0.2-py3.7.egg
```

## 设置配置文件 config/config.xml

| 字段 | 定义 |
|----|----|
| res | excel 源文件夹路径|
| output | 单一 data 文件路径|
| outputJson | json 文件输出文件夹路径|

## excel文档读取并输出
```
    cd 运行文件目录
    python3 Excel2Data.py [arg]
```
### arg 参数定义

| 字段 | 定义 |
|----|----|
| 1 | 只输出客户端数据|
| 2 |只输出服务器数据|
| 缺省值 | 都输出 |