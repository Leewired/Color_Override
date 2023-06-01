import maya.cmds as cmds

sel = cmds.ls(sl=True)

if len(sel) == 0:

    cmds.confirmDialog(t="Hei", m="Select something")

else:

    cmds.colorEditor()

    if cmds.colorEditor(q=True, result=True):

        values = cmds.colorEditor(q=True, rgb=True)
        print("RGB = ")

        for value in values:

            print(value)
        
        for item in sel:

            cmds.setAttr(item + ".overrideEnabled", 1)
            cmds.setAttr(item + ".overrideRGBColors", 1)
            cmds.setAttr(item + ".overrideColorRGB", values[0], values[1], values[2])
    
    else:
        pass
