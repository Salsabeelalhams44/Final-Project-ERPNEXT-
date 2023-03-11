// Copyright (c) 2023, sals and contributors
// For license information, please see license.txt
frappe.ui.form.on('Payment Entry', {
	load: function(frm) {
		set_df_property('naming_series','read_only',1);
		set_value('naming_series','GSG-JV-.YYYY.-');
	}
});
