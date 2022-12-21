import bpy
import glob 

for AsePaletteFile in glob.glob('/tmp/ase/*.ase'):
    bpy.ops.import_ase.read(filepath=AsePaletteFile)

for GplPaletteFile in glob.glob('/tmp/GPL/*.gpl'):    
    bpy.ops.import_krita.read(filepath=GplPaletteFile)    
