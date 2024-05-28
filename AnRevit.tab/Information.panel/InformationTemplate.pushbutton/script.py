from pyrevit import forms

selected_viewtemplates = forms.select_viewtemplates()
if selected_viewtemplates:
  print(selected_viewtemplates)