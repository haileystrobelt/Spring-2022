import maya.cmds as cmds

# Get sel
sels = cmds.ls(sl=True)

parent = sels[0]
child = sels[1]

cmds.parentConstraint(parent, child, maintainOffset=True, weight=1)
cmds.scaleConstraint(parent, child, maintainOffset=True, weight=1)