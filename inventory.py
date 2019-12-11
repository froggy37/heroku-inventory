#!/usr/bin/env python3

import json
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

with open('./inventory.json', 'r') as f:
    inventory_data = json.loads(f.read())

@app.route('/')
def index():
    return "<h1>Welcome to the bootcamp dummy inventory server !!</h1>"

@app.route('/rest/getInventory', methods=['GET'])
def inventoryGet():
    return json.dumps(inventory_data), 200

@app.route('/rest/getFreeIntfs', methods=['GET'])
def getFreeIntfs():
    result = []
    for interface in inventory_data:
        if interface["description"] in ["FREE", "free", "Free"]:
            result.append(interface)
    return json.dumps(result), 200

@app.route('/rest/updateInventory', methods=['POST'])
def updateInventory():
    content = request.json
    if "interface" not in content.keys():
        return json.dumps("invalid interface"), 400
    if "description" in content.keys():
        description = content["description"]
    else:
        description = None
    if "ipAddress" in content.keys():
        ipAddress =  content["ipAddress"]
    else:
        ipAddress = None
    if "mask" in content.keys():
        mask = content["mask"]
    else:
        mask = None
    found = False
    for interface in inventory_data:
        if interface["interface"] == content["interface"]:
            found = True
            if description:
                interface["description"] = description
            if ipAddress:
                interface["ipAddress"] = ipAddress
            if mask:
                interface["mask"] = mask
    if not found:
        return json.dumps("interface not in inventory"), 400
    else:
        return {}, 201


if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0', port=5000, debug=True)
