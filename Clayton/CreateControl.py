def createControl():
    # matchtransformations can change both location and orientations to match transforms of selected objs
    # cmds.matchTransform('cylinder1', 'cone1')

    sels = cmds.ls(sl=True)  # grab selection
    len_sels = len(sels)  # store selection list length

    if len_sels == 0: # if no selections, set control to the center
        ctrl = cmds.circle(n='Default_Ctrl', normal=[0,1,0])  # create and name nurbs circle
        cmds.select(ctrl)  # select it
        #cmds.rotate('90deg', 0, 0, r=True)  # fix incorrect rotation
        grp = cmds.group(ctrl, n='Grp_Crtl')


    elif len_sels == 1: # if there is only one selection, name it
        ctrl_name = sels[0] + "_Ctrl"
        ctrl = cmds.circle(n=ctrl_name, normal=[0,1,0])  # create and name nurbs circle
        cmds.select(ctrl)  # select it
        #cmds.rotate('90deg', 0, 0, r=True)  # fix incorrect rotation
        grp = cmds.group(ctrl, n='Grp_Crtl')
        cmds.matchTransform(grp, sels[0]) # set control to match transforms of selection


    else:
        for sel in sels: # multiple selections
            print(sels)
            print(sel)
            ctrl_name = sel + "_Ctrl"
            ctrl = cmds.circle(n=ctrl_name, normal=[0,1,0])  # create and name nurbs circle
            #cmds.select(ctrl[0])  # select it
            #cmds.rotate('90deg', 0, 0, r=True)  # fix incorrect rotation
            grp = cmds.group(ctrl[0], n='Grp_Crtl')
            cmds.matchTransform(grp,sel)  # set control to match transforms of selection

createControl()