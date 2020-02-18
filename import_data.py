import django
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FoolInterview.settings")
django.setup()
from quote_api import models as quote_models
from content_api import models as content_models

def main():
    import_content()
    import_quotes()

def import_content():
    # load json file
    with open('content_api.json') as json_file:
        data = json.load(json_file)['results']

    # import data into models
    for article_info in data:
        set_attrs(content_models, content_models.Article, article_info)

def import_quotes():
    # load json file
    with open('quotes_api.json') as json_file:
        data = json.load(json_file)

    # import data into models
    for company_info in data:
        set_attrs(quote_models, quote_models.Company, company_info)

def set_attrs(models_module, model_class, attributes):
    obj = model_class()

    for attr_name, attr_val in attributes.items():
        if type(attr_val) == dict:
            attr_name = attr_name[0].upper() + attr_name[1:]
            attr_val = set_attrs(models_module, getattr(models_module, attr_name), attr_val)
        if type(attr_val) == list: # m2m rel # TODO: this is gross and I want to fix it
            obj.save()
            for nested_val in attr_val:
                attr_name = attr_name[0].upper() + attr_name[1:]
                attr_name = attr_name[:-1]
                attr_val = set_attrs(models_module, getattr(models_module, attr_name), nested_val)
                attr_name = attr_name[0].lower() + attr_name[1:] + 's'
                getattr(obj, attr_name).add(attr_val)
            continue

        attr_name = attr_name[0].lower() + attr_name[1:]
        setattr(obj, attr_name, attr_val)
    print('creating object for {}'.format(type(obj)))
    obj.save()
    return obj

if __name__ == '__main__':
    main()
