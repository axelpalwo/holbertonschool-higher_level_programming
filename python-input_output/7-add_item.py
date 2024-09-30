import sys
saveToJson = __import__('5-save_to_json_file').save_to_json_file
loadFromJson = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
try:
    obj = loadFromJson(filename)
except:
    obj = []

i = 1
while i < len(sys.argv):
    obj.append(sys.argv[i])
    i += 1
saveToJson(obj, filename)