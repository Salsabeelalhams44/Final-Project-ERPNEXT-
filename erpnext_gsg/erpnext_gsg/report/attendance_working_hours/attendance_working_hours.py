# Copyright (c) 2023, Salsabeel Alhams and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [], []
	data = get_all_attendance(filters)
	columns = get_columns(filters)
	return columns, data
	

def get_columns(filters):
	columns = [
		{'fieldname': 'attendance_date', 'label':'Attendance Date', 'fieldtype':'Date' },
		{'fieldname': 'employee', 'label':'Employee', 'fieldtype':'Link', 'options': 'Employee' },
		{'fieldname': 'employee_name', 'label':'Employee Name', 'fieldtype':'Data' },
		{'fieldname': 'check_in', 'label':'Check In', 'fieldtype':'Time' },
		{'fieldname': 'check_out', 'label':'Check Out', 'fieldtype':'Time' },
		{'fieldname': 'working_hours', 'label':'Working Hours', 'fieldtype':'Float' },
		#{'fieldname': 'employee', 'label':'View Attendance Form', 'fieldtype':'Link', 'options': 'Attendance' },
	]
	return columns

def get_all_attendance(filters):
	return frappe.db.get_all("Attendance",
	 [
	 'employee',
	 'employee_name',
	 'attendance_date',
	 'check_in',
	 'check_out',
	 'working_hours',
	 ],
	 filters= filters
	 )


