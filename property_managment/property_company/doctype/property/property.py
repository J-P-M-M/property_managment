# Copyright (c) 2023, a@gmail.com and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document

class Property(Document):
	#@frappe.whitelist()
	#def set_responsible_person(self, values):

		#print(type(values))
		#res = json.loads(values)

		#self =frappe.get_doc("Property", self.name)
	#	self.responsible_person = values["responsible_person"]
	#	self.save()


	pass


@frappe.whitelist()
def set_responsible_person(responsible_person, name):

	res= json.loads(responsible_person)

	doc=frappe.get_doc("Property", name)
	doc.responsible_person = res["responsible_person"]
	doc.save()
	
	
