from ._anvil_designer import Lender_reg_form_5Template
from anvil import *

class Lender_reg_form_5(Lender_reg_form_5Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    open_form('user_form.Lender_reg_form_4')
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    open_form('user_form.Lender_reg_form_6')
    """This method is called when the button is clicked"""
    
  
