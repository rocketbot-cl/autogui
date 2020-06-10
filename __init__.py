# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""

import sys
import os
base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'autogui' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

import pyautogui
from ctypes import *
"""
    Obtengo el modulo que fueron invocados
"""

module = GetParams("module")

if module == "click":
    coord = GetParams("coord")
    path = GetParams("path")
    type_ = GetParams("type")

    try:
        click = {
            "double": pyautogui.doubleClick,
            "simple": pyautogui.click
        }

        if coord:
            x, y = eval(coord)
            pyautogui.doubleClick(x,y)
            print(x,y)
            click[type_](x, y)
        elif path:
            click[type_](path)
        else:
            click[type_]()
    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

if module == "keyboard":
    type_ = GetParams("type")
    key = GetParams("key")
    try:
        keyboard = {
            "press": pyautogui.press,
            "keyDown": pyautogui.keyDown,
            "keyUp": pyautogui.keyUp
        }

        if len(key) > 1 and type_ == "press":
            key = [c for c in key]

        keyboard[type_](key)


    except Exception as e:
        print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
        PrintException()
        raise e

# if module == "alert":
#     text = GetParams("text")
#
#     try:
#         pyautogui.alert(text)
#
#     except Exception as e:
#         print("\x1B[" + "31;40mError\u2193\x1B[" + "0m")
#         PrintException()
#         raise e