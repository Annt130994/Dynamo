from pyrevit import forms

selected_titleblocks = forms.select_titleblocks()
if selected_titleblocks:
    print(selected_titleblocks)