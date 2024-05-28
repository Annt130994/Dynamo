from pyrevit import forms
selected_views = forms.select_views()
if selected_views:
 print(selected_views)