# Copyright (c) 2021, ideenkreisetech pvt ltd and contributors
# For license information, please see license.txt

# import frappe
import frappe
from frappe.model.document import Document

class IssueAnnualCarrierContract(Document):
		def validate(self):
			if self.amount==0 or self.previous_year_amount==0:
				self.difference_=0
				frappe.throw('Amount cannot be zero')
			else:
				percentage=(self.amount-self.previous_year_amount)*(100/self.previous_year_amount)
				self.difference_=percentage
			# frappe.msgprint('amount'+str(percentage))
			
