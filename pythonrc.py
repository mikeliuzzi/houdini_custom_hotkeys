import hou

print ("script loading")

def switch_context(context_type):

    #create path for context
    context_path = f"/{context_type}"

    #find and store the network pane
    network_pane = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)

    if network_pane:
        network_pane.setPwd(hou.node(context_path))
    else:
        print("no active network pane")
    


