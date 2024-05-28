# -*- coding: utf-8 -*-
from Autodesk.Revit.DB import *
from pyrevit import forms, revit
doc     = __revit__.ActiveUIDocument.Document                       
uidoc   = __revit__.ActiveUIDocument                            
app     = __revit__.Application

generic_id = ElementId(4111230)
generic    = doc.GetElement(generic_id)
# print("-"*50)
# print('*Parameters: *')
# for c in generic.Parameters:
# if c.Definition.Name == 'Comments':
#     print("Tat ca deu la text")
#     print(c.Id)
#     # print (c)
#     print ('Element: {}'.format(c.Definition.Name))
# #     print ('Element: {}'.format(c.AsValueString))
# print("-"*50)
# generic_comments = generic.LookupParameter('Khối lượng bê tông')
# print('Khối lượng bê tông: {}'.format(generic_comments.AsValueString()))
# generic_nck = generic.getParameter(c.Definition.Name)

# generic_ck = generic.LookupParameter('Tên cấu kiện')
# generic_mt = generic.LookupParameter('Mô tả')
# t = Transaction(doc, __title__)
# t.Start()
# #changes here
# t.Commit()

# generic_nck.set("Cấu kiện A")
# generic_ck.set("Cấu kiện B")
# generic_mt.set("Cấu kiện C")

# print(generic_nck.AsString())
# print(generic_ck.AsString())
# print(generic_mt.AsString())

# print("-"*50)
# print('*Built-in Parameters: *')
# getpara = generic.get_Parameter(Definition.BuiltInParameter.HOT_AREA_COMPUTED)
# print(getpara.AsString())
# # t.Start()
# # Comments.Set(1200.0)
# # t.Commit()
# print("-"*50)
# # PRINT GLOBAL PARAMETERS DATA
# for p_id in all_global_parameter_ids:
#     p = doc.GetElement(p_id)
#     print('Name: {}'.format(p.Name))
# print("-"*50)


print("-"*50)
all_generic = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_GenericModel).WhereElementIsNotElementType().ToElements()
for GenericModel in all_GenericModel:
    generic_mark = generic.get_Parameter(BuiltInParameter.ALL_MODEL_MARK)
    generic_mark.Set(str(GenericModel.Id))
    print(GenericModel.Id)
print("-"*50)
    