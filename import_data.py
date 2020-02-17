import django
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FoolInterview.settings")
django.setup()
from api import models

def main():
    # load json file
    with open('quotes_api.json') as json_file:
        data = json.load(json_file)

    # import data into models
    for company_info in data:
        set_attrs(models.Company, company_info)

def set_attrs(model_class, attributes):
    obj = model_class()
    for attr_name, attr_val in attributes.items():
        if type(attr_val) == dict:
            attr_val = set_attrs(getattr(models, attr_name), attr_val)
        attr_name = attr_name[0].lower() + attr_name[1:]
        setattr(obj, attr_name, attr_val)
    print('creating object for {}'.format(type(obj)))
    obj.save()
    return obj

if __name__ == '__main__':
    main()
