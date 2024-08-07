def escape_text(text):
    # 替换换行符
    escaped_text = text.replace('\n', '\\n')
    # 替换双引号
    escaped_text = escaped_text.replace('"', '\\"')
    return escaped_text

input_text = """
<将此替换为你复制的角色卡信息>
<substitute this to character card info which you copied>
"""

# 调用函数进行替换
output_text = escape_text(input_text)

# 打印结果
print(output_text)