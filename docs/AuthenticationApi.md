# rustici_software_cloud_v2.AuthenticationApi

All URIs are relative to *https://cloud.scorm.com/api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_token**](AuthenticationApi.md#get_app_token) | **POST** /oauth/authenticate/application/token | Authenticates for a oauth token


# **get_app_token**
> ApplicationToken get_app_token(scope, expiration=expiration)

Authenticates for a oauth token

### Example
```python
from __future__ import print_function
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
configuration = rustici_software_cloud_v2.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.AuthenticationApi(rustici_software_cloud_v2.ApiClient(configuration))
scope = 'scope_example' # str | 
expiration = 300 # int |  (optional) (default to 300)

try:
    # Authenticates for a oauth token
    api_response = api_instance.get_app_token(scope, expiration=expiration)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->get_app_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**|  | 
 **expiration** | **int**|  | [optional] [default to 300]

### Return type

[**ApplicationToken**](ApplicationToken.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

