# -*- coding: utf-8 -*-
from Autodesk.Revit.DB import *
import clr
clr.AddReference('System')
from pyrevit import forms, revit
doc     = __revit__.ActiveUIDocument.Document                       
uidoc   = __revit__.ActiveUIDocument                            
app     = __revit__.Application

active_view = doc.ActiveView
active_level = doc.ActiveView.GenLevel