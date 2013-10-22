bl_info = {
    "name": "Full Screen Icon",
    "author": "Floo",
    "version": (0,2),
    "blender": (2, 68, 0),
    "location": "View3D",
    "description": "Add Full Screen icon and update Ctr+Space shortcut",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "http://blenderartists.org/forum/showthread.php?315272-Addon-Full-Screen-Icon",
    "category": "3D View"}

import bpy
from bpy.props import IntProperty

class FullScrOperator(bpy.types.Operator):

    bl_idname = "object.fullscr_operator"
    bl_label = "Simple Full Scr Operator"

    def execute(self, context):
        bpy.ops.screen.screen_full_area() 
        bpy.ops.wm.window_fullscreen_toggle()
        return {'FINISHED'}
        
class FULLSCR_L(bpy.types.Header):    
    bl_space_type = 'VIEW_3D'  

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("object.fullscr_operator", text="", icon="FULLSCREEN_ENTER")          

class FULLSCR_A(bpy.types.Header):
    bl_space_type = 'TEXT_EDITOR'    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.operator("object.fullscr_operator", text="", icon="FULLSCREEN_ENTER")                 

class FULLSCR_B(bpy.types.Header):
    bl_space_type = 'NODE_EDITOR'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("object.fullscr_operator", text="", icon="FULLSCREEN_ENTER") 

class FULLSCR_C(bpy.types.Header):
    bl_space_type = 'GRAPH_EDITOR'    
 
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("object.fullscr_operator", text="", icon="FULLSCREEN_ENTER")  
    
class FULLSCR_D(bpy.types.Header):
    bl_space_type = 'DOPESHEET_EDITOR'    
 
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("object.fullscr_operator", text="", icon="FULLSCREEN_ENTER")  
    
class FULLSCR_E(bpy.types.Header):
    bl_space_type = 'NLA_EDITOR'   
 
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("object.fullscr_operator", text="", icon="FULLSCREEN_ENTER")  
        
class FULLSCR_F(bpy.types.Header):
    bl_space_type = 'IMAGE_EDITOR'    

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("object.fullscr_operator", text="", icon="FULLSCREEN_ENTER") 

class FULLSCR_G(bpy.types.Header):
    bl_space_type = 'SEQUENCE_EDITOR'    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("object.fullscr_operator", text="", icon="FULLSCREEN_ENTER")     
    
class FULLSCR_H(bpy.types.Header):
    bl_space_type = 'CLIP_EDITOR'    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("object.fullscr_operator", text="", icon="FULLSCREEN_ENTER")     
    
class FULLSCR_I(bpy.types.Header):
    bl_space_type = 'NODE_EDITOR'    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("object.fullscr_operator", text="", icon="FULLSCREEN_ENTER")     
    
class FULLSCR_J(bpy.types.Header):
    bl_space_type = 'OUTLINER'    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("object.fullscr_operator", text="", icon="FULLSCREEN_ENTER")     
    
class FULLSCR_K(bpy.types.Header):
    bl_space_type = 'INFO'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.operator("object.fullscr_operator", text="", icon="FULLSCREEN_ENTER")  
    
class FULLSCR_L(bpy.types.Header):    
    bl_space_type = 'CONSOLE'  

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("object.fullscr_operator", text="", icon="FULLSCREEN_ENTER")  


def menu_func(self, context):
    self.layout.operator(FullScrOperator.bl_idname)

addon_keymaps = []

def register():
    bpy.utils.register_module(__name__)
        
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(FullScrOperator.bl_idname, 'SPACE', 'PRESS', shift=True)
    addon_keymaps.append((km, kmi))


def unregister():
    bpy.utils.unregister_module(__name__)      

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    
if __name__ == "__main__":
    register() 
