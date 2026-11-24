# 就业帮扶指标口径与定时报送

样例提供活动、人员、互动、就业结果、指标口径和报送回执数据，全部为本地合成资料。

这是一个可本地运行的分析项目底座。data/schema.json 说明输入记录的最小结构，data/sample.json 只用于检查文件格式和读取路径，不包含业务结论。

## 运行环境

需要 Python 3.11 或更高版本，项目不依赖外部服务。使用标准库执行格式检查和测试。

```sh
python3 -m unittest discover -s tests -v
python3 -m compileall -q src tests
```

后续业务能力应从项目中提供可重复的分析入口，读取新的同结构数据并产生可解释的结果。
