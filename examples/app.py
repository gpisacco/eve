from eve import Eve
from eve.auth import BasicAuth
from flask import request,render_template,redirect,session,abort
import logging
from  datetime import timedelta,date,time
from flask import request,redirect,session,abort
from werkzeug import secure_filename
from werkzeug.local import LocalProxy

from bson.son import SON
import pymongo
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import os, random, string
import json
import datetime
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import g


from logging.handlers import RotatingFileHandler 

class DemoAuth(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource, method):
        # use Eve's own db driver; no additional connections/resources are used
        app.logger.debug(password)
        self.request_auth_value__tenant = "tonga.net"
        self.request_auth_value__user=username
        self.request_auth_value__group = "group" 
        self.request_auth_value__permission = [7,5,5]
        
        return True
    
    def auth_field_and_value(self,resource):
        """ If auth is active and the resource requires it, return both the
        current request 'request_auth_value' and the 'auth_field' for the resource

        .. versionadded:: 0.3
        """
        if '|resource' in request.endpoint:
            # We are on a resource endpoint and need to check against
            # `public_methods`
            public_method_list_to_check = 'public_methods'
        else:
            # We are on an item endpoint and need to check against
            # `public_item_methods`
            public_method_list_to_check = 'public_item_methods'

        resource_dict = app.config['DOMAIN'][resource]

        if request.method not in ['POST','PUT']:

            request_auth_value=[{"_tenant":self.request_auth_value__tenant, \
                                    "$or":[{"_user":self.request_auth_value__user},\
                                            {"_group":{"$in":[self.request_auth_value__group]},\
                                             "_permission.1":{"$gt":1}\
                                            }\
                                           ]\
                                }]
        else:
            auth_fields=resource_dict.get('auth_field')
            request_auth_value=[]
            for i,f in enumerate(auth_fields):
            	request_auth_value[i] = getattr(self,'request_auth_value_'+f) 
            return auth_fields,request_auth_value
                
        return ["$and"],[request_auth_value]

 
app = Eve(__name__,auth=DemoAuth)
app.on_pre_GET += pre_get_callback
# set the secret key.  keep this really secret:
app.secret_key = '11111111111111111111111111111'

file_handler = RotatingFileHandler("error_eve.log")
file_handler.setLevel(logging.ERROR)
app.logger.addHandler(file_handler)



if __name__ == '__main__':
    
    app.run(settings='settings.py')
    app.debug = True
    app.wsgi_app = ProxyFix(app.wsgi_app)
    