import maya.cmds as cmds
#Turns off scaling Scaling issue - when you scale, the joint shrinks, this fixes that issue.

# Get sel
sels = cmds.ls(sl=True)

for sel in sels:
    cmds.setAttr('%s.segmentScaleCompensate' % sel, 0)