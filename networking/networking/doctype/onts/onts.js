// Copyright (c) 2022, Henry Dobinson and contributors
// For license information, please see license.txt

frappe.ui.form.on('ONTs', {
	setup(frm){
		frappe.call({
			method: "networking.networking.doctype.onts.test.get_prod_type",
			callback: function(r){
				console.log(r.message);
			}
		});
	},


});
