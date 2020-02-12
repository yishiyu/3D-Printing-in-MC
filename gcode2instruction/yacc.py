# coding:utf-8
# ---------
# Gcode转 MC命令 语法分析
# author：bibibi
# ---------

from lexer import lexer, tokens
import ply.yacc as yacc

# operation --> 一个操作/之前的所有操作
# parameter --> 一个操作的参数,参数之间的合并有最高的优先级

# 操作合并


def p_instrutions_1(p):
    'instrucions : instrucions instrucion'
    p[0] = p[1] + p[2]


def p_instrutions_2(p):
    'instrucions : instrucion instrucion'
    p[0] = p[1] + p[2]

# 合成操作


def p_instrution_1(p):
    'instrucion : G1 parameters'
    p[0] = [p[2]]


def p_instrution_2(p):
    'instrucion : G0 parameters'
    p[0] = [p[2]]

# 合并参数


def p_parameters_1(p):
    # G1 F1800 X156.458 Y81.471 E0.00998
    # 移动喷头并放置方块
    'parameters : SPEED POSX POSY POSE'
    p[0] = (0, p[2], p[3])


def p_parameters_2(p):
    # G0 F3600 X156.204 Y81.937 Z0.3
    # 修改 Z 坐标,并移动喷头
    'parameters : SPEED POSX POSY POSZ'
    p[0] = (2, p[2], p[3], p[4])

def p_parameters_3(p):
    # G0 F3600 X156.907 Y82.32
    # 移动喷头但不放置方块
    'parameters : SPEED POSX POSY'
    p[0] = (1, p[2], p[3])

def p_parameters_4(p):
    # G1 F1500 E0
    # 空指令
    'parameters : SPEED POSE'
    p[0] = (3, 0, 0)


def p_parameters_5(p):
    # G1 X156.871 Y80.798 E0.02484
    # 移动喷头并放置方块
    'parameters : POSX POSY POSE'
    p[0] = (0, p[1], p[2])


def p_parameters_6(p):
    # G1 X166.13 Y89.762
    # 移动喷头但不放置方块
    'parameters : POSX POSY'
    p[0] = (1, p[1], p[2])


# 错误处理


def p_error(p):
    print("Syntax error in input!", p)


parser = yacc.yacc()

# 转换函数


def compile(data):
    result = parser.parse(data)
    return result
