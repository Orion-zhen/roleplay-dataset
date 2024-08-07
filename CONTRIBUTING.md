# 贡献指南

首先, **感谢您愿意贡献您的对话记录**.

## 文件格式

本仓库支持的聊天记录文件格式为`jsonl`文件, 以下是其内部格式, 其中列出的字段为必需项:

```jsonl
{"user_name": <name>, "character_name": <char>}
{"system": <system>}
{"name": <role name>, "mes": <message>}
{"name": <role name>, "mes": <message>}
...
```

解释:

- 第一行, 必须要有`user_name`和`character_name`字段.
- 第二行, 必须要有`system`字段.
- 第三行及以后, 必需要有`name`和`mes`字段.

## 生成/导出聊天记录文件

您可以将其他地方的优质数据集转化为上文要求的格式然后提交, 但我更推荐使用[SillyTavern](https://github.com/SillyTavern/SillyTavern)导出您的聊天数据为`jsonl`格式的文件, 因为这样只需要对文件做微小的改动即可符合本仓库要求的数据格式.

如果您选择使用[SillyTavern](https://github.com/SillyTavern/SillyTavern)导出的数据, 则请按如下步骤添加`system`字段:

1. 找到这段聊天对应的角色卡.
2. 复制其**角色描述**框中的所有内容, 可能是多行文字.
3. 在本仓库的目录下找到`trans.py`文件, 将其打开.
4. 找到如下字段:

    ```python
    input_text = """
    <将此替换为你复制的角色卡信息>
    <substitute this to character card info which you copied>
    """
    ```

    将您复制的角色描述信息复制到对应的地方.
5. 运行如下命令:

    ```shell
    python trans.py
    ```

6. 您将会在终端中看到转换完成的文本, 将其全部复制.
7. 打开您的聊天记录文件, 新增**第二行**为空行, 插入如下文本:

    ```json
    {"system": "此处替换为您刚刚复制的文本"}
    ```

8. 保存文件并退出

现在, 您已经成功构建了符合要求的聊天记录文件.

## 上传聊天记录文件

请fork一份本仓库到您的名下, 从仓库目录中打开`data`文件夹, 将您的聊天记录文件上传到该文件夹中, 然后向本仓库提交**Pull Request**. 如果您之前fork过本仓库, 请确保在您上传文件**之前同步您的fork**, 以免造成索引错误而无法通过自动检测.

如果一切正常, 您的Pull Request将会自动被合并到本仓库中, 之后您可以安全地删除您创建的fork.

感谢您对本仓库的贡献.
