import maya.cmds as cmds

def display_joint_orient():
    sels = cmds.ls(sl=True)
    
    for sel in sels:
        if cmds.nodeType(sel) == 'joint':
            state = cmds.getAttr('%s.displayLocalAxis' % sel)
            cmds.setAttr('%s.displayLocalAxis' % sel, not state)
            cmds.setAttr('%s.displayLocalAxis' % sel, keyable=not state, channelBox=not state)
            cmds.setAttr('%s.jointOrientX' % sel, keyable=not state, channelBox=not state)
            cmds.setAttr('%s.jointOrientY' % sel, keyable=not state, channelBox=not state)
            cmds.setAttr('%s.jointOrientZ' % sel, keyable=not state, channelBox=not state)
            
display_joint_orient()