#!/usr/bin/python3

from flask import Flask
from flask import request
from flask import Response
import xmltodict
import dicttoxml
import json




#
# create a REST response for a
#  Dictionary dict values
#  content_type : application/xml or application/json
#  root : root xml/json name
#
def create_dict_response(dict, content_type, root):
    if content_type == "application/json":
        resp = Response(json.dumps({root:dict}))
    elif content_type == "application/xml":
        resp = Response(dicttoxml.dicttoxml(dict, custom_root=root))        

    resp.headers["Content-Type"] = content_type
    return resp


#
# Convert REST request into Dictionary
# 
# accepts content-type=application/xml
# accepts content-type=application/json
#
def get_request_dict(request):
    if request.content_type == "application/json":
        content = request.get_json()        
        print ('JSON posted')
    elif request.content_type == "application/xml":
        content = xmltodict.parse(request.data)        
        print ('XML posted')
    return content

