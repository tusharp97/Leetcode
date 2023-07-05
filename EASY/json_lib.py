import json

json_data ='''
{
  "destination_addresses": [
    "Philadelphia, PA, USA"
  ],
  "origin_addresses": [
    "New York, NY, USA"
  ],
  "rows": [{
    "elements": [{
      "distance": {
        "text": "94.6 mi",
        "value": 152193
      },
      "duration": {
        "text": "1 hour 44 mins",
        "value": 6227
      },
      "status": "OK"
    }]
  }],
  "status": "OK"
}
'''

#print(json_data)
datas = json.loads(json_data)
#data=json.load(json_data)

print(type(datas))
print(type(datas['rows']))
for r in datas['rows']:
    print(r['elements'][0]['distance'])
    #del r['elements']
#print(json.dumps(datas,indent= 2))
#with open('address.json','r') as f:
#   data=json.load(f)

# with open('address.json','w') as f:
#    data=json.dump(f)