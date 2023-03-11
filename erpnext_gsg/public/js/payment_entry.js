// Copyright (c) 2023, sals and contributors
// For license information, please see license.txt
frappe.ui.form.on('Payment Entry', {
	setup: function(frm) {
		set_field_options('naming_series',
		['GSG-JV-.YYYY.-']);
	}
});
