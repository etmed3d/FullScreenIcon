bl_info = {
    "name": "Full Screen Icon",
    "author": "Floo",
    "version": (0,1),
    "blender": (2, 68, 0),
    "location": "View3D",
    "description": "",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "",
    "category": "3D View"}

import bpy
from bpy.props import IntProperty
           
		   
class FULLSCR_A(bpy.types.Header):
    bl_space_type = 'VIEW_3D'
#    bl_space_type = 'TIMELINE'       
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER")
        
class FULLSCR_AA(bpy.types.Header):
    bl_space_type = 'TEXT_EDITOR'    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER")                 

class FULLSCR_B(bpy.types.Header):
    bl_space_type = 'NODE_EDITOR'

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER") 

class FULLSCR_C(bpy.types.Header):
    bl_space_type = 'GRAPH_EDITOR'    
 
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER")  
    
class FULLSCR_D(bpy.types.Header):
    bl_space_type = 'DOPESHEET_EDITOR'    
 
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER")  
    
class FULLSCR_E(bpy.types.Header):
    bl_space_type = 'NLA_EDITOR'   
 
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER")  
        
class FULLSCR_F(bpy.types.Header):
    bl_space_type = 'IMAGE_EDITOR'    

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER") 

class FULLSCR_G(bpy.types.Header):
    bl_space_type = 'SEQUENCE_EDITOR'    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER")     
    
class FULLSCR_H(bpy.types.Header):
    bl_space_type = 'CLIP_EDITOR'    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER")     
    
class FULLSCR_I(bpy.types.Header):
    bl_space_type = 'NODE_EDITOR'    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER")     
    
class FULLSCR_J(bpy.types.Header):
    bl_space_type = 'OUTLINER'    
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER")     
    
class FULLSCR_K(bpy.types.Header):
    bl_space_type = 'INFO'
    
    def draw(self, context):
        layout = self.layout
        scene = context.scene
        layout.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER")
        layout.operator('wm.window_fullscreen_toggle', text='', icon = 'FULLSCREEN')     
    
class FULLSCR_L(bpy.types.Header):    
    bl_space_type = 'CONSOLE'  

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        self.layout.separator()
        layout.operator("screen.screen_full_area", text="", icon="FULLSCREEN_ENTER")                 

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
