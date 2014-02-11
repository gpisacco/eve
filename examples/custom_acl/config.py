from datetime import datetime
X_DOMAINS='*'



tenant = {
    'resource_methods': ['GET', 'POST'],
     'schema':  {
                 "name":  {
                     'type': 'string',
                     'minlength': 3,
                     'maxlength': 50,
                     'required': True,
                 },
      }
}

group = {
    'resource_methods': ['GET', 'POST'],
     'schema':  {
                 "name":  {
                     'type': 'string',
                     'minlength': 3,
                     'maxlength': 50,
                     'required': True,
                 },
                 "description": {
                     'type': 'string',
                     'minlength': 3,
                     'maxlength': 150,
                     'required': False,
                 },
                 "members":{
                    'type': 'list',
                 },
                 "status":{
                    'type': 'string',
                    'allowed': ["active", "suspended","deleted"],
                    'default':'active'
                 },
                 "creationdate":{
                    'type': 'datetime',
                    'default':datetime.utcnow()
                 },
                'tenant':{
                     'type': 'objectid',
                     'data_relation': {
                                         'resource': 'tenants',
                                         'field': '_id',
                                         'embeddable': True
                                     },
                    'required': True
                },                
      }
}


person = {
        'resource_methods': ['GET', 'POST'],
        'query_objectid_as_string':True,
        'embedded_fields':['group'],
        'schema':  {
                'firstname': {
                    'type': 'string',
                    'minlength': 1,
                    'maxlength': 50,
                    'required': True,
                },
                'lastname': {
                    'type': 'string',
                    'minlength': 1,
                    'maxlength': 50,
                    'required': True,
                },
                'email':    {
                    'type': 'string',
                    'minlength': 1,
                    'maxlength': 50,
                    'required': False,
                },
                'status': {
                    'type': 'string',
                    'allowed': ["active", "suspended","deleted"],
                    'default':'active'
                    
                },
                'creationdate': {
                    'type': 'datetime',
                    'default':datetime.utcnow()
                },
                'group':{
                     'type': 'objectid',
                     'data_relation': {
                                         'resource': 'groups',
                                         'field': '_id',
                                         'embeddable': True
                                     },
                    'required': True
                },
            }
}

user= {
        'resource_methods': ['GET', 'POST'],
        'schema':  {
                'username': {
                    'type': 'string',
                    'minlength': 1,
                    'maxlength': 50,
                    'required': True,
                    'unique': True,
                },
                'person':{
                    'type': 'objectid',
                    'data_relation': {
                                         'resource': 'persons',
                                         'field': '_id',
                                         'embeddable': True
                                     },
                    'required': True,
                    'unique': True
                    
                },
                'password':{
                    'type': 'string',
                    'minlength': 8,
                    'required': True
                },
                'roles':    {
                    'type': 'list',
                    'required': False
                    
                },
                'status':    {
                    'type': 'string',
                    'allowed': ["active", "suspended","deleted"],
                    'default':'active'
                }
            }
}




DOMAIN = {
    'tenants': tenant,
    'persons': person,
    'groups':group,
    'users':user, 
}



# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''
MONGO_DBNAME = 'test'



# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE','PATCH']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

AUTH_FIELD=['_tenant','_user','_group','_permission']

PAGINATION_DEFAULT=10
DATE_FORMAT="%Y-%m-%dT%H:%M:%S.000Z"
DEBUG=True

#Custom Configurations
SECRET_KEY='11111111111111111111111'


