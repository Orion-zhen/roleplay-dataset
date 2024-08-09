# Rolplay Dataset

这是一个为了收集优质角色扮演对话记录的仓库.

如果您有优质的对话记录, 并且愿意提交到本仓库, 请参考[贡献指南](./CONTRIBUTING.md)来提交您的聊天记录.

本仓库将生成sharegpt格式的数据集, 可以直接用于[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)进行SFT训练.

```json
[
    {
        "system": "something",
        "conversations": [
            {
                "from": "human",
                "value": "say something"
            },
            {
                "from": "gpt",
                "value": "reply something"
            }
        ]
    }
]
```

想要生成数据集文件, 只需运行:

```shell
python scripts/release.py
```

这会根据`data`文件夹中的所有内容, 在仓库目录下生成一个名为`dataset.parquet`的数据集文件.

## 致谢

[@Kasio](https://github.com/Kas1o)提供了便捷的数据导出插件
