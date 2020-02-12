# -- coding: utf-8 --**
# ---------
# Gcode转 MC命令 词法分析
# author：bibibi
# ---------

import ply.lex as lex

# 产生的 Token
# G0   --> 操作码G0
# G1   --> 操作码G1
# POSX   --> X坐标
# POSY   --> Y坐标
# POSZ   --> Z坐标
# POSE   --> E坐标
# SPEED  --> 移动速度
tokens = (
    'G1',
    'G0',
    'POSX',
    'POSY',
    'POSZ',
    'POSE',
    'SPEED',
    't_ignore_COMMENTS'
)

# 定义 Token 对应的正则表达式

def t_G0(t):
    r'G0'
    return t

def t_G1(t):
    r'G1'
    return t


# 整行忽略的内容
t_ignore_COMMENTS = r'(G92|;|M)[^\n]*'

# 处理参数


def t_POSX(t):
    r'X(-?[0-9]+.?[0-9]*)'
    # X 的处理方法为取 1 位小数后减去 23,乘以 10,最终范围为 0~1600 
    # t.value = int((round(float(t.value[1:]), 1) - 23)*10)
    t.value = round(float(t.value[1:])) - 23
    return t


def t_POSY(t):
    r'Y(-?[0-9]+.?[0-9]*)'
    t.value = round(float(t.value[1:])) - 60
    return t


def t_POSZ(t):
    r'Z(-?[0-9]+.?[0-9]*)'
    t.value = int(float(t.value[1:]))
    return t


def t_POSE(t):
    r'E(-?[0-9]+.?[0-9]*)'
    t.value = float(t.value[1:])
    return t


def t_SPEED(t):
    r'F([0-9]+.?[0-9]*)'
    t.value = float(t.value[1:])
    return t

# 换行处理


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    if t.lexer.lineno %1000 == 0:
        print(t.lexer.lineno)


# 忽略的字符
t_ignore = ' \t'

# 错误处理


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# 创建词法分析器
lexer = lex.lex()


if __name__ == "__main__":
    with open("./temp1.txt", 'r', encoding='utf-8') as file:
        data = file.read()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
