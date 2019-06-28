#!/usr/bin/python3

from flask import Flask
from flask import request
from flask import Response
import xmltodict
import dicttoxml
import json
import os
from rest_tools import get_request_dict
from rest_tools import create_dict_response

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, World!"

#
# Simple get 
#
@app.route('/get', methods=['GET'])    
def get():
    content = {'status' : "ok"}

    if request.content_type == "application/json":
        return create_dict_response(content, request.content_type, 'result')
    elif request.content_type == "application/xml":
        return create_dict_response(content, request.content_type, 'result')


@app.route('/search', methods=['GET'])    
def search():
    search_term = request.args['term']
    matches = []
    content = {'status' : "ok", "search" : search_term, 'matches' : matches }
    searched = 0
    found = 0
    root_directories = ["/home/jcdwyer"]
    for root_dir in root_directories :
        for folders, dirs, files in os.walk(root_dir) :
            for file in files :
                if file.endswith('.txt') :
                    fullpath = os.path.join(folders,file)
                    # print (fullpath)
                    with open(fullpath, 'r', encoding="utf8", errors='ignore') as f:
                        searched = searched + 1
                        for line in f:
                            if search_term in line :
                                matches.append({'file' : { 'name' : fullpath, 'found' : line.strip() } })
                                found = found + 1
                                break
    content['searched'] = searched
    content['found'] = found
    if request.content_type == "application/json":
        return create_dict_response(content, request.content_type, 'result')
    elif request.content_type == "application/xml":
        return create_dict_response(content, request.content_type, 'result')        


# 
# accept post and return as "result"
#
@app.route('/post', methods=['POST'])
def post():
    content = get_request_dict(request)

    print(content)

    return create_dict_response(content, request.content_type, 'result')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)