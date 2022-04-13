import maya.cmds as cmds


def locator():
    
    sels = cmds.ls(sl=True)

    bbox = cmds.xform(sels, q= True, boundingBox=True, ws=True) #[xmin, ymin, zmin, xmax, ymax, zmax]

    mid_x = (bbox[0] + bbox[3]) / 2
    mid_y = (bbox[1] + bbox[4]) / 2
    mid_z = (bbox[2] + bbox[5]) / 2

    loc = cmds.spaceLocator(position=[0,0,0], absolute=True)[0]

    cmds.xform(loc, translation=[mid_x, mid_y, mid_z], ws=True)
locator()

def joints_from_sels():
    sels = cmds.ls(sl=True)
    
    for sel in sels:
        pos = cmds.xform(sel, q=True, rotatePivot=True, ws=True) #[x,y,z]
        
        cmds.select(cl=True)
        n_joint = cmds.joint(position=[0,0,0], absolute=True)
        cmds.xform(n_joint, translation=pos, ws=True)

def parent_from_sels():
    sels = cmds.ls(sl=True)
    
    for i, sel in enumerate(sels):
        if i < (len(sels) - 1):
            cmds.parent(sels[i], sels[i+1])
        
