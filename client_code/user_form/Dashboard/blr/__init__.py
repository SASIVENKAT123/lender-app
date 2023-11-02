from ._anvil_designer import blrTemplate
from anvil import *

class blr(blrTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("user_form.Dashboard")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("user_form.Dashboard.avbal")

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("user_form.Dashboard.blr")

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("user_form.Dashboard.ld")

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("user_form.Dashboard.vlo")

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("user_form.Dashboard.td")

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("user_form.Dashboard.vcl")

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("user_form.Dashboard.vler")

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("user_form.Dashboard.vlfr")

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("user_form.Dashboard.rta")

  def link_13_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("user_form.Dashboard.vdp")

  def link_12_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("user_form.Dashboard.vep")

  def link_11_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("user_form.Dashboard.vsn")

  def link_10_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("user_form.Dashboard.cp")
