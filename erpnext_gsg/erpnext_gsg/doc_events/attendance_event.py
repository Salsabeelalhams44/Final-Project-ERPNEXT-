import frappe 
from frappe.utils import time_diff_in_hours

def calculate_working_hours(doc,method):
	if doc.check_in and doc.check_out:
		hours= time_diff_in_hours(doc.check_out,doc.check_in)
		doc.working_hours= float(hours)
	if not doc.check_in or  not doc.check_out:
		doc.working_hours=0

