
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

## Django REST Framework
Django REST framework is a powerful and flexible toolkit for building Web APIs.

- The Web browsable API is a huge usability win for your developers.
- Authentication policies including packages for OAuth1 and OAuth2.
- Serialization that supports both ORM and non-ORM data sources.
- Customizable all the way down - just use regular function-based views if you don't need the more powerful features.
- Extensive documentation, and great community support.
- Used and trusted by internationally recognized companies including Mozilla, Red Hat, Heroku, and Eventbrite.

## Requirements
- Python
- Django

The following packages are optional:

- PyYAML, uritemplate (5.1+, 3.0.0+) - Schema generation support.
-  Markdown (3.0.0+) - Markdown support for the browsable API.
- Pygments (2.4.0+) - Add syntax highlighting to Markdown processing.
- django-filter (1.0.1+) - Filtering support.
- django-guardian (1.1.1+) - Object level permissions support.

## How to Install DRF

If python and django are installed globally on your system, then

Install using pip

```bash 
  pip install djangorestframework

```

  
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


## Serializer Field

Serializer fields handle converting between primitive values and internal datatypes. They also deal with validating input values, as well as retrieving and setting the values from their parent objects.

Syntax:

```bash 
  from rest_framework import serializers 
  serializers.Field_Name()

```
## Core Arguments

**label:** A short text string that may be used as the name of the field in HTML form fields or other descriptive elements.

**validators:** A list of validator functions which should be applied to the incoming field input, and which either raise a validation error or simply return. Validator functions should typically raise serializers. **ValidationError**, but Django's built-in ValidationError is also supported for compatibility with validators defined in the Django codebase or third party Django packages.

## De-serialization

Serializers are also responsible for deserialization which means it allows parsed data to be converted back into complex types, after first validating the incoming data.

## BytesIO()

A stream implementation using an in-memory bytes buffer. It inherits BufferedlOBase. The buffer is discarded when the close() method is called.

```bash 
  import io
  streamio.BytesIO(json_data)
```

## JSONParser()

This is used to parse json data to python native data type.  

```bash 
  from rest_framework.parsers
  parsed_data = JSONParser().parse(stream)
```

## De-serialization

Deserialization allows parsed data to be converted back into complex types, after first validating the incoming data.

**Creating Serializer Object**

```bash 
  serializer = StudentSerializer(data = parsed_data)
```

**Validated Data**

```bash 
   serializer.is_valid()
```

```bash 
   serializer.validated_data
   serializer.errors
```

## Python JSON

Python has a built in package called json, which is used to work with json data.

**dumps(data):** This is used to convert python object into json string.


## Validators

REST framework the validation is performed entirely on the serializer class. This is advantageous for the following reasons:

- It introduces a proper separation of concerns, making your code behavior more obvious.
- It is easy to switch between using shortcut ModelSerializer classes and using explicit Serializer classes. Any validation behavior being used for ModelSerializer is simple to replicate.

Printing the repr() of a serializer instance will show you exactly what validation rules it applies. There's no extra hidden validation behavior being called on the model instance.

When you're using ModelSerializer all of this is handled automatically for you. If you' want to drop down to using Serializer classes instead, then you need to define the validation rules explicitly.  


## Function Based api_view

This wrapper provide a few bits of functionality such as making sure you receive Request instances in your view, and adding context to Response objects so that content negotiation can be performed.

The wrapper also provide behaviour such as returning 405 Method Not Allowed responses when appropriate, and handling any ParseError exceptions that occur when accessing request.data with malformed input.

By default only GET methods will be accepted. Other methods will respond with "405 Method Not Allowed".

@api_view()

@api_view(['GET', ‘POST', ‘PUT', 'DELETE']) def function_name(request):



## Field Level Validation

We can specify custom field-level validation by adding validate_fieldName methods to your Serializer subclass.

These are similar to the clean fieldName methods on Django forms. validate fieldName methods should return the validated value or raise a serializers.ValidationError

Syntax:
```bash 
  def validate_fieldname(self, value)
```
Example:- def validate_roll(self, value)

## Object Level Validation

When we need to do validation that requires access to multiple fields we do object level validation by adding a method called validate() to Serializer subclass.

It raises a serializers. ValidationError if necessary, or just return the validated values.

Syntax:
```bash 
  def validate (self, data)
```
Example:- def validate (self, data)

Where, data is a dictionary of field values.


`

## Response ()

REST framework supports HTTP content negotiation by providing a Response class which allows you to return content that can be rendered into multiple content types, depending on the client request.

Response objects are initialized with data, which should consist of native Python primitives. REST framework then uses standard HTTP content negotiation to determine how it should render the final response content.

Response class simply provides a nicer interface for returning content-negotiated Web API responses, that can be rendered to multiple formats.


`Response(data, status=None, template_name=None, headers-None, content_type=None)
`


**data:** The unrendered, serialized data for the response.

**status:** A status code for the response. Defaults to 200.

**template_name:** A template name to use only if HTMLRenderer or some other custom template renderer is the accepted renderer for the response.

**headers:** A dictionary of HTTP headers to use in the response.

**content_type:** The content type of the response. Typically, this will be set automatically by the renderer as determined by content negotiation, but there may be some cases where you need to specify the content type explicitly.

## GenericAPIView

**lookup_field-** The model field that should be used to for performing object lookup of individual model instances. Defaults to 'pk'.

**lookup_url_kwarg-** The URL keyword argument that should be used for object lookup. The URL conf should include a keyword argument corresponding to this value. If unset this defaults to using the same value as lookup_field.

**pagination_class-** The pagination class that should be used when paginating list results. Defaults to the same value as the DEFAULT_PAGINATION_CLASS setting, which is 'rest_framework.pagination.PageNumberPagination'. Setting pagination_class=None will disable pagination on this view.

**filter backends -** A list of filter backend classes that should be used for filtering the queryset. Defaults to the same value as the DEFAULT_FILTER_BACKENDS setting.

### Methods

**get_queryset(self)-** It returns the queryset that should be used for list views, and that should be used as the base for lookups in detail views. Defaults to returning the queryset specified by the queryset attribute.

This method should always be used rather than accessing self.queryset directly, as self.queryset gets evaluated only once, and those results are cached for all subsequent requests.

**get_object(self)-** It returns an object instance that should be used for detail views. Defaults to using the lookup_field parameter to filter the base queryset.

**get_serializer_class(self)-** It returns the class that should be used for the serializer. Defaults to returning the serializer_class attribute.

**get_serializer_context(self)-** It returns a dictionary containing any extra context that should be supplied to the serializer. Defaults to including 'request', 'view' and 'format' keys.

**get_serializer(self, instance=None, data=None, many=False, partial=False) -** It returns a serializer instance.

**get_paginated_response(self, data)-** It returns a paginated style Response object.

**paginate_queryset(self, queryset)-** Paginate a queryset if required, either returning a page object, or None if pagination is not configured for this view.

**filter_queryset(self, queryset)-** Given a queryset, filter it with whichever filter backends are in use, returning a new queryset.

## Mixins

One of the big wins of using class-based views is that it allows us to easily compose reusable bits of behaviour.

The create/retrieve/update/delete operations that we've been using so far are going to be pretty similar for any model-backed API views we create.

Those bits of common behaviour are implemented in REST framework's mixin classes.

The mixin classes provide the actions that are used to provide the basic view behavior.



**Note-** the mixin classes provide action methods rather than defining the handler methods, such as get() and post(), directly. This allows for more flexible composition of behavior.

### ListModelMixin

It provides a list(request, *args, **kwargs) method, that implements listing a queryset.

If the queryset is populated, this returns a 200 OK response, with a serialized representation of the queryset as the body of the response. The response data may optionally be paginated.

`from rest_framework.mixins import ListModelMixin`

`from rest_framework.generics import GenericAPIView`

### CreateModelMixin

It provides a create(request, *args, **kwargs) method, that implements creating and saving a new model instance.

If an object is created this returns a 201 Created response, with a serialized representation of the object as the body of the response. If the representation contains a key named url, then the Location header of the response will be populated with that value.

If the request data provided for creating the object was invalid, a 400 Bad Request response will be returned, with the error details as the body of the response.
  
### RetrieveModelMixin

It provides a retrieve(request, *args, **kwargs) method, that implements returning an existing model instance in a response.

If an object can be retrieved this returns a 200 OK response, with a serialized representation of the object as the body of the response. Otherwise it will return a 404 Not Found.

### UpdateModelMixin

It provides a update(request, *args, **kwargs) method, that implements updating and saving an existing model instance.

It also provides a partial_update(request, *args, **kwargs) method, which is similar to the update method, except that all fields for the update will be optional. This allows support for HTTP PATCH requests.

If an object is updated this returns a 200 OK response, with a serialized representation of the object as the body of the response.

### DestroyModelMixin

It provides a destroy(request, *args, **kwargs) method, that implements deletion of an existing model instance.

If an object is deleted this returns a 204 No Content response, otherwise it will return a 404 Not Found.

  
  
  
