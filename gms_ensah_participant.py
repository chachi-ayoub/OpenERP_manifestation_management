from osv import osv,fields
# import openerp


class gms_ensah_participant(osv.osv):
    _name= 'gms.ensah.participant'
    _columns={
        'image':fields.binary('photo_participant', filters="*.png"),
        'name':fields.char('Nom Complet', required=True) ,
        'CNE':fields.char('CNE', required=True)  ,
        'phone':fields.char('Number')  ,
        'email': fields.char('Email', required=True) ,
        'age': fields.integer('Age', required=True) ,
        'residence': fields.boolean('Residence') ,
        'date_naissance': fields.date('Date de naissance') ,
        'address': fields.char('Address', required=True) ,
        'id_manifestation':fields.many2one('gms.ensah.manifestation','Manifestation', ondelete='cascade'),
    } 

gms_ensah_participant()