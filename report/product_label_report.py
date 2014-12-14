from openerp.report import report_sxw
from openerp.osv import osv,fields
from openerp.tools.translate import _
from openerp.tools import flatten
import time
import openerp.pooler
from dateutil.relativedelta import relativedelta
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, float_compare
from datetime import datetime
from datetime import date, timedelta


class product_label_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(product_label_report, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
                                  "get_loop_time":self.get_loop_time,
                                  "get_attr":self.get_attr
            
        })
        
    def get_loop_time(self,product_ids):
        val1=[]
        val2=[]
        val3=[]
        val5=[]
        l=[]
        dict={}
        for val in product_ids:
            val1.append(val)
        lop=len(val1)
        mid = int(lop+1)/2
        for val2 in range(0,mid):
            val3.append(val2)
        for val4 in product_ids:
            val5.append(val4)
        length = len(val5)
    
        lb = 1
        ub = length
        mid1 = int((lb+ub)/2)
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        i=1
        for val6 in val5:
            if i <= mid1:
                list1.append(val6)
            else:
                list2.append(val6)
            i = i+1
        dict={'loop':val3,'first':list1,'second':list2}
        l.append(dict)
        return l   
    
    def get_attr(self,attr_lines):
        attr=''
        for val in attr_lines:
            attr=attr + ',' +val.name            
        return attr[1:]
    
        
report_sxw.report_sxw('report.product.label.report', 'wiz.product.label', 'addons/product_label_report/report/product_label_report.rml', parser=product_label_report,header=False)

class product_label_form_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context=None):
        super(product_label_form_report, self).__init__(cr, uid, name, context=context)
        self.localcontext.update({
                                  "get_loop_time":self.get_loop_time,
                                  "get_attr":self.get_attr
            
        })
        
    def get_loop_time(self,product_ids):
        val1=[]
        val2=[]
        val3=[]
        val5=[]
        l=[]
        dict={}
        for val in product_ids:
            val1.append(val)
        lop=len(val1)
        mid = int(lop+1)/2
        for val2 in range(0,mid):
            val3.append(val2)
        for val4 in product_ids:
            val5.append(val4)
        length = len(val5)
    
        lb = 1
        ub = length
        mid1 = int((lb+ub)/2)
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        i=1
        for val6 in val5:
            if i <= mid1:
                list1.append(val6)
            else:
                list2.append(val6)
            i = i+1
        dict={'loop':val3,'first':list1,'second':list2}
        l.append(dict)
        return l   
    
    def get_attr(self,attr_lines):
        attr=''
        for val in attr_lines:
            attr=attr + ',' +val.name            
        return attr[1:]
    
        
report_sxw.report_sxw('report.product.label.form.report', 'product.product', 'addons/product_label_report/report/product_label_form_report.rml', parser=product_label_form_report,header=False)