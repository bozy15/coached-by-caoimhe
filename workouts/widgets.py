from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

class CustomClearableFileInput(ClearableFileInput):
    # Override the template with these attributes
    clear_checkbox_label = _("Remove")
    initial_text = _("Current Image")
    input_text = _("")
    template_name = "workouts/custom_widgets_templates/custom_clearable_file_input.html"