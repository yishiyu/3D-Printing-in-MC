# -*- coding: utf-8 -*-

import mcpi.minecraft as mcm
import mcpi.block as mcb
import time
import json


class printer():

    def __init__(self):
        super().__init__()
        self.game = self.get_game()
        self.pos = self.getpos(self.game)

        # 喷头坐标,后面需要注意的是,MC中高度坐标是y坐标
        self.nozzle = [0, 0, 0]

    def get_game(self):
        # 获取游戏
        mc = mcm.Minecraft.create()
        return mc

    def getpos(self, mc):
        # 获取玩家位置
        pos = mc.player.getTilePos()
        return pos

    def get_instruction(self, file_name):
        # 获取instruction信息(从json文件中读取)
        with open('./' + file_name, 'r') as file:
            instructions = json.load(file)
        return instructions

    def setblock(self):
        self.game.setBlock(
            self.pos.x + self.nozzle[0] - 80,self.nozzle[2], self.pos.z + self.nozzle[1] - 40, 155)

    def run(self, file_name):

        # 读取指令
        self.instructions = self.get_instruction(file_name)

        # 限制运行速度
        counter = 0

        # 依次读取指令并操作
        for command in self.instructions:
            # 解析指令并执行
            # 移动喷头并放置方块, 2 参数
            if command[0] == 0:
                self.nozzle[0] = command[1]
                self.nozzle[1] = command[2]
                self.setblock()
                counter += 1

            # 移动喷头但不放置方块, 2 参数
            elif command[0] == 1:
                self.nozzle[0] = command[1]
                self.nozzle[1] = command[2]

            # 在三维空间内移动喷头, 3 参数
            elif command[0] == 2:
                self.nozzle[0] = command[1]
                self.nozzle[1] = command[2]
                self.nozzle[2] = command[3]

            # 空指令
            elif command[0] == 3:
                pass

            if counter >= 100:
                counter = 0
                time.sleep(2)


# 主程序
if __name__ == "__main__":

    file_names = ["killer queen1.json","killer queen2.json","killer queen3.json","killer queen4.json","killer queen5.json"]
    MC_printer = printer()
    for file_name in file_names:
        MC_printer.run(file_name)
