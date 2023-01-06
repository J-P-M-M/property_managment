import frappe
from erpnext.setup.doctype.territory.territory import Territory


class CustomTerritory(Territory):

    def save(self, *args, **kwargs):
        print("888888888888000000000888888888888888")
        super().save(*args, **kwargs)
    
    def validate(self):
        if self.territory_type == "Country" and self.is_group == 0:
            frappe.throw("Country can not be is group 1")

        super().validate()