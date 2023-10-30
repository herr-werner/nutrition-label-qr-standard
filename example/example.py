
import json
from newsmile import SmileEncoder
from bidict import bidict
import qrcode


# key values for common fields of the FDA Nutrition Label
key_map = bidict({
	'servings per container': 'srvs',
	'serving information': 'srv',
	'serving unit label': 'srvu',
	'units per serving': 'qty',
	'fractional denominator': 'd',
	'fractional numerator': 'n',
	'grams': 'g',
	'milligrams': 'mg',
	'micrograms': 'mcg',
	'percent daily value': 'dv',
	'total fat': 'tf',
	'saturated fat': 'sf',
	'cholesterol': 'ch',
	'sodium': 'na',
	'total carbohydrate': 'cb',
	'dietary fiber': 'fb',
	'total sugars': 'sg',
	'includes added sugars': 'asg',
	'protein': 'pt',
	'vitamin d': 'vd',
	'calcium': 'ca',
	'iron': 'fe',
	'potassium': 'k',
	'vitamin a': 'va',
	'vitamin c': 'vc',
	'thiamin': 'th',
	'riboflavin': 'rb',
	'niacin': 'ni',
	'vitamin b6': 'vb6'
})

# example label key
label_key = {
	"srvs": 1,
	"srv": {
		"srvu":  "box",
		"qty": 1,
		"g":   85
	},
	"tf": {"g":  1.5, "dv": 4},
	"sf": {"g":  0.5, "dv": 5},
	"ch": {"mg": 10,  "dv": 3},
	"na": {"mg": 240, "dv": 16},
	"cb": {"g":  11,  "dv": 7},
	"fb": {"g":  1,   "dv": 7},
	"sg": {"g":  1,   "dv": 4},
	"pt": {"g":  3,   "dv": 23},
	"vd":  {"mcg": 2,   "dv": 10},
	"ca":  {"mg":  0,   "dv": 0},
	"fe":  {"mg":  2,   "dv": 10},
	"k":   {"mg":  120, "dv": 2},
	"va":  {"dv":  0},
	"vc":  {"dv":  0},
	"th":  {"dv":  35},
	"rb":  {"dv":  30},
	"ni":  {"dv":  30},
	"vb6": {"dv":  30}
}

encoder = SmileEncoder(shared_values=True)
json_str = json.dumps(label_key,indent=None, separators=(',', ':'))

print(f'json string size: {len(json_str)}')

print(json_str)

result = encoder.encode(json.dumps(label_key))

print(f'encoded size: {len(result)}')

for b in result:
	print(f'0x{b:x} ', end='')

img = qrcode.make(result)
type(img)
img.save("label.png")
