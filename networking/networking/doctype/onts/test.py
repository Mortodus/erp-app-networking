import frappe
#from netmiko import ConnectHandler
from frappe.model.document import Document



class ONTs(Document):
	


@frappe.whitelist()
def get_prod_type():
	value = "metal"
	return value