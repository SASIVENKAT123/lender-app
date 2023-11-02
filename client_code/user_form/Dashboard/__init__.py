from ._anvil_designer import DashboardTemplate
from anvil import *

class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("user_form")

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("user_form.Dashboard.opbal")

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("user_form.Dashboard.avbal")

  def outlined_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("user_form.Dashboard.blr")

  def outlined_button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("user_form.Dashboard.td")

  def outlined_button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("user_form.Dashboard.vcl")
