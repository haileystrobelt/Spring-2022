import maya.cmds as cmds

sels = cmds.ls(sl=True)

for sel in sels:
    shapes = cmds.listRelatives(sel, shapes=True, children=True)
    for shape in shapes:
        cmds.setAttr('%s.overrideEnabled' % shape, True)
        cmds.setAttr('%s.overrideColor' % shape, 13)