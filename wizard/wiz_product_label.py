import time
from openerp.tools.translate import _
from openerp.osv import osv, fields
import os
import base64, urllib
import openerp.netsvc
from datetime import datetime, timedelta,date
from dateutil.relativedelta import relativedelta
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT, float_compare
import cStringIO
from xlwt import Workbook, XFStyle, Borders, Pattern, Font, Alignment,  easyxf

class wiz_product_label(osv.TransientModel):
    _name = 'wiz.product.label'
    
    
    _columns = {
                'product_id':fields.many2many('product.product','product_label_table_rel','product_label1','product_label2','Product',),
                }
    
    
    def print_report(self,cr,uid,ids,context=None):
        report_obj = self.pool.get('ir.actions.report.xml')
#        line_ids = []
#       for each in self.browse(cr, uid, ids):
#           for line in each.droptest_line:
#                line_ids.append(line.id)
        datas = {'ids' : ids}
        rpt_id =  report_obj.search(cr, uid, [('model','=','wiz.product.label')])
        if not rpt_id:
            raise osv.except_osv(_('Invalid action !'), _('Report for this name order no exist.'))
        rpt_type = report_obj.read(cr, uid, rpt_id, ['report_name'])[0]
        
        return {
           'type' : 'ir.actions.report.xml',
           'report_name':str(rpt_type['report_name']),
           'datas' : datas,
           'nodestroy':True,
        }
     
        return res
    
