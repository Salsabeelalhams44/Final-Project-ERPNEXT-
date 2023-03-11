# Copyright (c) 2023, Salsabeel Alhams and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document
from frappe.utils import time_diff_in_hours
from datetime import datetime
class EmployeeExcuseApplication(Document):
	def validate(self):
		self.calculate_hours()
		
	def on_submit(self):
		pass
		#self.update_allownace_hours()
		
	def calculate_hours(self):
		if self.from_time and self.to_time and self.from_time < self.to_time:
			hours= time_diff_in_hours(self.to_time,self.from_time)
			self.hours= float(hours)
			dept_name= self.employee_department.rstrip(' - GSG')
			
			get_allownace_hours = frappe.db.sql(""" select excuse_hour_allowed from `tabDepartment` where 
			department_name=%s""",dept_name, as_dict=1)[0].excuse_hour_allowed
			
			#default_allownace_hours=get_allownace_hours
			#print('###########################################')
			#print('default_allownace_hours:  ', default_allownace_hours)
			#excuse_date= datetime.strptime(self.excuse_date, '%Y-%m-%d').month


			#check_same_month=frappe.db.sql("""select employee_name from `tabEmployee Excuse Application` where excuse_date=%s and employee_name=%s""", (self.excuse_date, self.employee_name))

			#if len(check_same_month)>1:
			if self.hours > float(get_allownace_hours):
				frappe.throw('Sorry, there are No hours allow!!')
			#update_allow_hour= float(get_allownace_hours) - self.hours
			#frappe.db.sql("""update `tabDepartment` set excuse_hour_allowed=%s where department_name=%s"""(str(update_allow_hour),dept_name))
				#print('###########################################')
				#print('default_allownace_hours:  ', default_allownace_hours)
			#else:
				#print('###########################################')
				#print('default_allownace_hours:  ', default_allownace_hours)
				#allow_hour=frappe.db.sql("""update `tabDepartment` set excuse_hour_allowed=%s where department_name=%s"""(str(default_allownace_hours),dept_name))
				#if self.hours > float(allow_hour):
				#	frappe.throw('Sorry, there are No hours allow!!')
				#update_allow_hour= float(get_allownace_hours) - self.hours
				#frappe.db.sql("""update `tabDepartment` set excuse_hour_allowed=%s where department_name=%s"""(str(update_allow_hour),dept_name))
				

			
				
			
			
				
		
		
			
			
			
			
			
			
			
			
			
			
		
