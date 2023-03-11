# Copyright (c) 2023, Salsabeel Alhams and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ToWhomItConcerns(Document):
	
	def validate(self):
		self.get_employee_salary()
		
	def get_employee_salary(self):
		salary= frappe.db.sql(""" select gross_pay from `tabSalary Slip` where employee_name=%s""",(self.employee_name), as_dict=1)
		print('--------------------------------------')
		print('salary ', salary[0].gross_pay)
		self.salary= salary[0].gross_pay 
		
