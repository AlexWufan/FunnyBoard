import json

with open('data2.json', 'r') as f:
    data = json.load(f)
print(len(data['features']))

if True:
    # title = request.form['title']
    # message = request.form['message']
    # action_type = request.form['action_type']
    # cordinates = request.form['cordinates']
    new_feature = {
                      "type": "Feature",
                      "geometry": {
                          "type": "Point",
                          "coordinates": 'test'
                      },
                      "properties": {
                          "title": 'easd',
                          "type": 'adasdasd',
                          "message": 'asdadds'
                      }
                  }

    data['features'].append(new_feature)

with open('data2.json', 'w') as f:
        json.dump(data, f)