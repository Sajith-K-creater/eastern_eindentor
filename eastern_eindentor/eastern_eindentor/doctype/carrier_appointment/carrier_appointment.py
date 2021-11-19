# Copyright (c) 2021, ideenkreisetech pvt ltd and contributors
# For license information, please see license.txt

# import frappe
from frappe import msgprint
from frappe.model.document import Document

class CarrierAppointment(Document):
	def on_update(self):
		# msgprint("Hello")
		pass
		
