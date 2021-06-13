
# Project Title

A brief description of what this project does and who it's for



## Application Programming Interface (API)
An API is a software intermediary that allows two or more applications to talk to each other.

API Type in terms of Release Policies:

**Private:** It can be used within the organization.

**Partner:** It can be used within Business Partners.

**Public:** It can be used any third party Developers.

## Web API

An API, which is interface for web is called as Web API.

It may consist of one or more endpoints to define request and response.
  
## How Web API Works
- Client makes HTTP Request to API
- API will communicate to Web Application/Database (If needed).
- Web Application/Database provides required data to API.
- API returns Data to Client
Note - Json Data, XML Data

## How to use Web API
- API may provide API Key for Authentication purpose API Key/Token
- Whenever you need to communicate with server make Request to API with API Key
- If API Key authentication succeed, API will provide required Data.

## REST

It is an architectural guideline to develop Web API.

## REST API

The API which is developed using REST is known as REST API/RESTful API.




#### CRUD operations


| **Operations** | **HTTP methods**    | **Description**                |
| :-------- | :------- | :------------------------- |
| `Create` | `POST` |  Creating/Posting/Inserting Data|
| Read | GET    | Reading/Getting/Retrieving Data                      |
| Update | PUT,PATCH | Updating Data(Complete Update - PUT, Partial Update - PATCH) |
| Delete     | DELETE | Deleting Data |


  
## Serialization

The process of converting complex data such as querysets and model instances to native Python datatypes are called as Serialization in DRF.

## Serializer Class

A serializer class is very similar to a Django Form and ModelForm class, and includes similar validation flags on the various fields, such as required, max_length and default.

DRF provides a Serializer class which gives you a powerful, generic way to control the output of your responses, as well as a ModelSerializer class which provides a useful shortcut for creating serializers that deal with model instances and querysets.
  
## JSONRenderer 

This is used to render Serialized data into JSON which is understandable by Front End.

Importing JSONRenderer

```bash 
 from rest_framework.renderers import JSONRenderer
```

Render the Data into Json

```bash 
 json_data = JSONRenderer().render(serializer.data)
```


    

  
## Requirements
- Python
- Django
The following packages are optional:

- PyYAML, uritemplate (5.1+, 3.0.0+) - Schema generation support.
-  Markdown (3.0.0+) - Markdown support for the browsable API.
- Pygments (2.4.0+) - Add syntax highlighting to Markdown processing.
- django-filter (1.0.1+) - Filtering support.
- django-guardian (1.1.1+) - Object level permissions support.

## Django REST Framework
Django REST framework is a powerful and flexible toolkit for building Web APIs.

- The Web browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1 and OAuth2.
- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognized companies including Mozilla, Red Hat, Heroku, and Eventbrite.
  
## ModelSerializer Class
The ModelSerializer class provides a shortcut that lets you automatically create a Serializer class with fields that correspond to the Model fields.

The ModelSerializer class is the same as a regular Serializer class, except that:
- It will automatically generate a set of fields for you, based on the model.
- It will automatically generate validators for the serializer, such as unique_together validators.
- It includes simple default implementations of create() and update().

## JsonResponse()
JsonResponse(data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs).

An HttpResponse subclass that helps to create a JSON-encoded response. It inherits most behavior from its superclass with a couple differences:
- Its default Content-Type header is set to application/json.
- The first parameter, data, should be a dict instance. If the safe parameter is set to False it can be any JSON-serializable object.
- The encoder, which defaults to django.core.serializers.json.DjangoJSONEncoder, will be used to serialize the data.
- The safe boolean parameter defaults to True. If it's set to False, any object can be passed for serialization (otherwise only dict instances are allowed). If safe is True and a non-dict object is passed as the first argument, a TypeError will be raised.
- The json_dumps_params parameter is a dictionary of keyword arguments to pass to the json.dumps() call used to generate the response.