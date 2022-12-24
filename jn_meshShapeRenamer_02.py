import bpy
#---------------------------------------------------------------#

#helper function to make the shape name match the transform name:
def childShapeRename():
    transformName = bpy.context.object.name
    bpy.context.object.data.name = 'msh_'+transformName

#helper function to process a bunch of selected objects one at a time:
def listLoop(list):
    bpy.ops.object.select_all(action='DESELECT') #deselect all
    eachItem = list.pop() #pop an item off the list
    eachItem.select_set(True) #select that item
    bpy.context.view_layer.objects.active = eachItem #make that item active
    return eachItem #serve it up to operate on
        
#---------------------------------------------------------------#

#define the bunch of selected objects:
allSelectedObjects = bpy.context.selected_objects

while allSelectedObjects:
    
    #get at each object individually:
    listLoop(allSelectedObjects)

    #define the currently selected individual object:
    currentSelection = bpy.context.active_object
    bpy.ops.object.mode_set(mode = 'OBJECT') 

    #see if the currently selected object has children:
    if len(set(currentSelection.children)) > 0:
        
        #if it has children...create a set from them:
        itsChildren = set(currentSelection.children)
        #then go ahead and rename the parent object:
        childShapeRename()
        #then copy the set of its children to process:
        childs = itsChildren.copy()
        #then pop each child off the set and rename each shape
        while childs:
            listLoop(childs)
            childShapeRename()

    #If the currently selected object has no children...just do the renaming on it.
    else:
        
        childShapeRename()
    
