// Copyright (c) 2021, ideenkreisetech pvt ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Issue Annual Carrier Contract', {
	// refresh: function(frm) {

	// }

	amount: function(frm){
		//frappe.msgprint("amount changed"+frm.doc.difference_);
		if(frm.doc.amount==0||frm.doc.previous_year_amount==0){
			frm.doc.difference_=0;
		}
		else{
			let percentage=(frm.doc.amount-frm.doc.previous_year_amount)*(100/frm.doc.previous_year_amount)
			frm.doc.difference_=percentage
		}
		frm.refresh();
	},

	previous_year_amount: function(frm){
		if(frm.doc.amount==0||frm.doc.previous_year_amount==0){
			frm.doc.difference_=0;
		}
		else{
			let percentage=(frm.doc.amount-frm.doc.previous_year_amount)*(100/frm.doc.previous_year_amount)
			frm.doc.difference_=percentage
		}
		frm.refresh();
	}

	// before_save:function(frm){
	// 	frappe.msgprint("before save");
	// }
});
