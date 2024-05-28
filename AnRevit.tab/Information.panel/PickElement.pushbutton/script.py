import sys
from Autodesk.Revit.DB import *

# PICK ELEMENT
# Use the forms.WarningBar context manager to show a warning or message bar on top of the Revit window
from pyrevit import forms, revit
doc     = __revit__.ActiveUIDocument.Document                       
uidoc   = __revit__.ActiveUIDocument                            
app     = __revit__.Application       
 
with forms.WarningBar(title='Pick an Element:'):
    element      = revit.pick_element()

element_type = type(element)
# if element_type !=Wall:
#  forms.alert('You were supposed to pick a Wall.', exitscript=True)

print(element)
print(element_type)

# if element_type !=Wall:
#  forms.alert('You were supposed to pick a Wall.', exitscript=True)
#  print("You were supposed to pick a Wall.")
#  sys.exit()


# GET INFORMATION
e_cat       = element.Category.Name
e_id        = element.Id
e_level     = doc.GetElement(element.LevelId)


# PRINT CONSOLE
print('Element Category: {}'.format(e_cat))
print('Element Id: {}'.format(e_id))
print('Element Level: {}'.format(e_level.Id))

# if element_type != Wall:
#   forms.alert('You were supposed to pick a Wall.', exitscript=True)
# #  print("You were supposed to pick a Wall.")
# #  sys.exit()


# # PRINT CONSOLE
# print('Element Category: {}'.format(e_cat))
# print('Element Id: {}'.format(e_id))
# print('Element LevelId: {}'.format(e_level.Name))
# print('Element Name: {}'.format(e_name))
# print('Element Parameters: {}'.format(e_para))


