import maya.cmds as cmds

# Get sel
sels = cmds.ls(sl=True)

constraint_target = sels[0]
ctrl = sels[1]
ctrl_grp = cmds.listRelatives(ctrl, parent=True)[0]

# Creating parent constraint that isolate, translate, and rotate
t_constraint = cmds.parentConstraint(constraint_target,
                                     ctrl_grp,
                                     maintainOffset=True,
                                     skipRotate=['x', 'y', 'z'],
                                     weight=1)
r_constraint = cmds.parentConstraint(constraint_target,
                                     ctrl_grp,
                                     maintainOffset=True,
                                     skipTranslate=['x', 'y', 'z'],
                                     weight=1)
# Adding custom attributes to control (FollowTranslate/FollowRotate)
cmds.addAttr(ctrl,
             longName='FollowTranslate',
             attributeType='double',
             min=0,
             max=1,
             defaultValue=1)
cmds.setAttr('%s.FollowTranslate' % ctrl, e=True, keyable=True)
cmds.addAttr(ctrl,
             longName='FollowRotate',
             attributeType='double',
             min=0,
             max=1,
             defaultValue=1)
cmds.setAttr('%s.FollowRotate' % ctrl, e=True, keyable=True)


# Connect attributes into constraint wegiht parameters
cmds.connectAttr('%s.FollowTranslate' % ctrl,
                 '%s.w0' % t_constraint,
                 force=True)
cmds.connectAttr('%s.FollowRotate' % ctrl,
                 '%s.w0' % r_constraint,
                 force=True)

             