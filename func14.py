models = [{'make':'tesla', 'model':'S', 'color':'Black'}, {'make':'Ford', 'model':'2', 'color':'Gold'}, {'make':'toyota', 'model': 'hilux', 'color':'Blue'}]
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print(sorted_models)