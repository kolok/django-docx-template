# django-template-docx



Django-Template-Docx provide all the necessities to deal fastly with editable document exportations.

Main functionnalities:
- easy data definition for developpers with autogenerated documentations for end users
- complete set of views and templates for end users to upload templates and download them merged

## Install

`pip install django-docx-template`

Then update your settings:

 ```python
 INSTALLED_APPS = [
     ...
     "django_docx_template",
     ...
 ]
 ```

## Usage

First you'll need to create a source of data:

```python
# my_app/data_sources.py
from django_docx_template.data_source import DataSource

# let's imagine you have a Model Person
from .models import Person


class PersonDataSource(DataSource):
    name = "My first data source"
    data_definition = [  # used for autogenerated documentation
        {
            "name": "first_name",
            "type": "string",
            "description": "first name of a person",
            "examples_values": ["Simon", "Edouard", "Francis"],
        },
        {
            "name": "Last_name",
            "type": "string",
            "description": "Family name of a person",
            "examples_values": ["Dupont", "Smith", "Gutierez"],
        },
        {
            "name": "age",
            "type": "int",
            "description": "Age of a person in year",
            "examples_values": [7, 33, 102],
        },
    ]
    keys_definition = {"person_id": "int"}  # used for url generation

    def get_context_data(self, person_id=None):
        person = Person.objects.get(pk=person_id)
        return {
            "first_name": person.first_name,
            "last_name": person.last_name,
            "age": person.get_age(),
        }
        
```

then you need to add the data source to your settings:

```python
# config/settings.py
...
DJANGO_DOCX_TEMPLATE = {
    "data_sources":[
        "my_app.data_sources.PersonDataSource",
    ]
}
```

to finish, wire urls:

```python
# config/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("docx/", include("django_docx_template.urls.py")),
]
```

Now your end users can access :
- docx/sources/ to explore data sources
- docx/library/ to browse and upload new templates
- docx/merge/<slug>/<key1>/<key2>/... to download a merged document

For example, to download a document with slug="identity" and wired to the data source previously built, the url would be /docx/merge/identity/123 (where 123 is a person_id).

## Ideas for future improvements

* Make a ModelDataSource that really autogenerated doc from field type and help argument
* And maybe make a mixin that turn a Model into DataSource
* Add managed command to help generate DataSource
* Use queryset and fields property make get_context_data automatic (like a serializer in DRF)
* use examples to merge document and help check everything is alright (which could be with url : docx/example/identity)

**The last point seems the way to go !!!!**

## Contributing

Please, use Black as code formatter and make sure the test coverage stick to 100%.

To run test, please see [https://github.com/Swannbm/runtest_on_dj_packages](https://github.com/Swannbm/runtest_on_dj_packages) ; if you know a better way to do it I am all ears :D

## Why

Because it is fun !