# 贡献指南

首先, **感谢您愿意为此仓库做出贡献**.

## 目录

- 贡献数据
- 贡献代码

## 贡献数据

您有两种方法来提交您的聊天记录文件:

- fork本仓库并提交Pull Request: 推荐使用, 和GitHub集成得很好.
- 向**rpcollector114@gmail.com**发送特定格式的邮件: 如果您不是很熟悉git的使用方法的话.

### 0. 数据格式

本仓库支持的数据格式为sharegpt, 支持的数据文件格式为`json`文件. 请确保您的聊天记录格式**严格符合**[README](./README.md)中展示的sharegpt格式.

### 1. 生成数据

您可以从其他地方获取聊天数据然后转换成sharegpt格式, 但我推荐使用[聊天记录导出插件](https://github.com/Kas1o/SillyTavern-Dataset-Export)从[SillyTavern](https://github.com/SillyTavern/SillyTavern)中导出聊天数据, 因为这样无需任何其它操作即可得到符合要求的聊天记录文件.

要使用[聊天记录导出插件](https://github.com/Kas1o/SillyTavern-Dataset-Export), 请先安装它. 安装方法可以查阅[SillyTavern文档](https://docs.sillytavern.app/#extensions).

在插件安装页面中, 输入该插件的仓库网址:

```html
https://github.com/Kas1o/SillyTavern-Dataset-Export
```

即可安装.

安装完成后, 如果想要导出sharegpt格式的数据, 则请选择`Export as dataset(ShareGPT)`选项.

### 2. 提交数据

一旦您准备好了数据文件, 就可以提交给本仓库. 您可以选择发送邮件或提交Pull Request.

> 请您先检查本仓库的`data`文件夹中的文件名是否和您准备上传的文件名有冲突, 如果有, 请修改之.
>
> 想要快速检查是否有文件名冲突, 您可以将本仓库克隆到本地, 然后尝试将您的数据文件复制到`data`文件夹中. 如果有冲突的话, 系统会提示您的.

#### 发送邮件

请您将您的`json`格式的数据文件作为附件, 发送到**rpcollector114@gmail.com**, 并将邮件主题设置为**rp**. 这样的邮件能被本仓库自动收取并加入到数据集中.

#### 提交PR

1. 请您fork一份本仓库, 如果您之前fork过, 则请先同步您的fork.
2. 将您的`json`格式的数据文件上传到仓库的`data`文件夹中, 请注意避免文件名冲突.
3. 向本仓库的主分支`main`提交Pull Request.

如果一切正常, 您的Pull Request将被自动合并到本仓库中.

## 贡献代码

还没想好写啥呢🤔
