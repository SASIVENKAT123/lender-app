from ._anvil_designer import Lender_reg_form_8Template
from anvil import *

class Lender_reg_form_8(Lender_reg_form_8Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('user_form.Lender_reg_form_7')
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    if self.radio_button_1.selected:
      open_form('user_form.Lender_reg_individual_form_1')
    elif self.radio_button_2.selected:
      open_form('user_form.Lender_reg_Institutional_form_1')
    """This method is called when the button is clicked"""
    
