# rustici_software_cloud_v2.PingApi

All URIs are relative to *https://cloud.scorm.com/api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping_app_id**](PingApi.md#ping_app_id) | **GET** /ping | Get back a message indicating that the API is working.


# **ping_app_id**
> PingSchema ping_app_id()

Get back a message indicating that the API is working.

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
# Configure OAuth2 access token for authorization: OAUTH
configuration = rustici_software_cloud_v2.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.PingApi(rustici_software_cloud_v2.ApiClient(configuration))

try:
    # Get back a message indicating that the API is working.
    api_response = api_instance.ping_app_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PingApi->ping_app_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PingSchema**](PingSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

