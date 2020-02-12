from yacc import compile
import json

if __name__ == "__main__":
    file_names = ["killer queen1","killer queen2","killer queen3","killer queen4","killer queen5"] 
    for file_name in file_names:
        with open(file_name + ".txt",'r',encoding='utf-8') as file:
            data = file.read()

        result = compile(data)

        with open(file_name + ".json",'w',encoding='utf-8') as file:
            json.dump(result,file)
