import frappe 

def submit_material_request_to_stock_entry(doc, method):
	if doc.material_request_type=='Material Issue':
		stock_entry= frappe.new_doc("Stock Entry")
		stock_entry.stock_entry_type ='Material Issue'
		stock_entry.to_warehouse=doc.set_warehouse
		for item in doc.items:
			if item and item.item_code:
				stock_entry.append('items', {
					'item_code':item.item_code,
					'qty': item.qty,
					'uom': item.uom,
					's_warehouse': item.warehouse,
					't_warehouse': doc.set_warehouse,
					'material_request': doc.name
				})
		stock_entry.save()

