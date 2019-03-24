# rustici_software_cloud_v2.RegistrationApi

All URIs are relative to *https://dev.cloud.scorm.com/api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_registration_instance**](RegistrationApi.md#create_new_registration_instance) | **POST** /registrations/{registrationId}/instances | Create a new instance for this registration specified by the registration ID
[**create_registration**](RegistrationApi.md#create_registration) | **POST** /registrations | Create a registration.
[**delete_registration**](RegistrationApi.md#delete_registration) | **DELETE** /registrations/{registrationId} | Delete &#x60;registrationId&#x60;
[**delete_registration_configuration_setting**](RegistrationApi.md#delete_registration_configuration_setting) | **DELETE** /registrations/{registrationId}/configuration/{settingId} | Clears the &#x60;settingId&#x60; value for this registration
[**delete_registration_instance_configuration_setting**](RegistrationApi.md#delete_registration_instance_configuration_setting) | **DELETE** /registrations/{registrationId}/instances/{instanceId}/configuration/{settingId} | Clears the &#x60;settingId&#x60; value for this registration instance
[**delete_registration_progress**](RegistrationApi.md#delete_registration_progress) | **DELETE** /registrations/{registrationId}/progress | Delete registration progress (clear registration)
[**delete_registrations_global_data**](RegistrationApi.md#delete_registrations_global_data) | **DELETE** /registrations/{registrationId}/globalData | Delete global data associated with &#x60;registrationId&#x60;
[**get_registration_configuration**](RegistrationApi.md#get_registration_configuration) | **GET** /registrations/{registrationId}/configuration | Returns all configuration settings for this registration
[**get_registration_instance_configuration**](RegistrationApi.md#get_registration_instance_configuration) | **GET** /registrations/{registrationId}/instances/{instanceId}/configuration | Returns all configuration settings for this registration instance
[**get_registration_instance_launch_history**](RegistrationApi.md#get_registration_instance_launch_history) | **GET** /registrations/{registrationId}/instances/{instanceId}/launchHistory | Returns history of this registration&#39;s launches
[**get_registration_instance_progress**](RegistrationApi.md#get_registration_instance_progress) | **GET** /registrations/{registrationId}/instances/{instanceId} | Get registration progress for instance &#x60;instanceId&#x60; of &#x60;registrationId&#x60;
[**get_registration_instance_statements**](RegistrationApi.md#get_registration_instance_statements) | **GET** /registrations/{registrationId}/instances/{instanceId}/xAPIStatements | Get xAPI statements for instance &#x60;instanceId&#x60; of &#x60;registrationId&#x60;
[**get_registration_instances**](RegistrationApi.md#get_registration_instances) | **GET** /registrations/{registrationId}/instances | Get all the instances of this the registration specified by the registration ID
[**get_registration_launch_history**](RegistrationApi.md#get_registration_launch_history) | **GET** /registrations/{registrationId}/launchHistory | Returns history of this registration&#39;s launches
[**get_registration_launch_link**](RegistrationApi.md#get_registration_launch_link) | **POST** /registrations/{registrationId}/launchLink | Returns the link to use to launch this registration
[**get_registration_progress**](RegistrationApi.md#get_registration_progress) | **GET** /registrations/{registrationId} | Get registration progress for &#x60;registrationId&#x60;
[**get_registration_statements**](RegistrationApi.md#get_registration_statements) | **GET** /registrations/{registrationId}/xAPIStatements | Get xAPI statements for &#x60;registrationId&#x60;
[**get_registrations**](RegistrationApi.md#get_registrations) | **GET** /registrations | Gets a list of registrations including a summary of the status of each registration.
[**registration_exists**](RegistrationApi.md#registration_exists) | **HEAD** /registrations/{registrationId} | Does this registration exist?
[**set_registration_configuration**](RegistrationApi.md#set_registration_configuration) | **POST** /registrations/{registrationId}/configuration | Set configuration settings for this registration.
[**set_registration_instance_configuration**](RegistrationApi.md#set_registration_instance_configuration) | **POST** /registrations/{registrationId}/instances/{instanceId}/configuration | Set configuration settings for this registration instance.


# **create_new_registration_instance**
> create_new_registration_instance(registration_id)

Create a new instance for this registration specified by the registration ID

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration

try: 
    # Create a new instance for this registration specified by the registration ID
    api_instance.create_new_registration_instance(registration_id)
except ApiException as e:
    print "Exception when calling RegistrationApi->create_new_registration_instance: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_registration**
> create_registration(registration, course_version=course_version)

Create a registration.

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration = rustici_software_cloud_v2.CreateRegistrationSchema() # CreateRegistrationSchema | 
course_version = 56 # int | The version of the course you want to create the registration for. Unless you have a reason for using this you probably do not need to. (optional)

try: 
    # Create a registration.
    api_instance.create_registration(registration, course_version=course_version)
except ApiException as e:
    print "Exception when calling RegistrationApi->create_registration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration** | [**CreateRegistrationSchema**](CreateRegistrationSchema.md)|  | 
 **course_version** | **int**| The version of the course you want to create the registration for. Unless you have a reason for using this you probably do not need to. | [optional] 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registration**
> delete_registration(registration_id)

Delete `registrationId`

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration

try: 
    # Delete `registrationId`
    api_instance.delete_registration(registration_id)
except ApiException as e:
    print "Exception when calling RegistrationApi->delete_registration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registration_configuration_setting**
> delete_registration_configuration_setting(registration_id, setting_id)

Clears the `settingId` value for this registration

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
setting_id = 'setting_id_example' # str | 

try: 
    # Clears the `settingId` value for this registration
    api_instance.delete_registration_configuration_setting(registration_id, setting_id)
except ApiException as e:
    print "Exception when calling RegistrationApi->delete_registration_configuration_setting: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **setting_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registration_instance_configuration_setting**
> delete_registration_instance_configuration_setting(registration_id, instance_id, setting_id)

Clears the `settingId` value for this registration instance

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
instance_id = 56 # int | The instance of this registration
setting_id = 'setting_id_example' # str | 

try: 
    # Clears the `settingId` value for this registration instance
    api_instance.delete_registration_instance_configuration_setting(registration_id, instance_id, setting_id)
except ApiException as e:
    print "Exception when calling RegistrationApi->delete_registration_instance_configuration_setting: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **instance_id** | **int**| The instance of this registration | 
 **setting_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registration_progress**
> delete_registration_progress(registration_id)

Delete registration progress (clear registration)

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration

try: 
    # Delete registration progress (clear registration)
    api_instance.delete_registration_progress(registration_id)
except ApiException as e:
    print "Exception when calling RegistrationApi->delete_registration_progress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registrations_global_data**
> delete_registrations_global_data(registration_id)

Delete global data associated with `registrationId`

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration

try: 
    # Delete global data associated with `registrationId`
    api_instance.delete_registrations_global_data(registration_id)
except ApiException as e:
    print "Exception when calling RegistrationApi->delete_registrations_global_data: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_configuration**
> SettingListSchema get_registration_configuration(registration_id, include_metadata=include_metadata)

Returns all configuration settings for this registration

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
include_metadata = false # bool |  (optional) (default to false)

try: 
    # Returns all configuration settings for this registration
    api_response = api_instance.get_registration_configuration(registration_id, include_metadata=include_metadata)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationApi->get_registration_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **include_metadata** | **bool**|  | [optional] [default to false]

### Return type

[**SettingListSchema**](SettingListSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_instance_configuration**
> SettingListSchema get_registration_instance_configuration(registration_id, instance_id, include_metadata=include_metadata)

Returns all configuration settings for this registration instance

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
instance_id = 56 # int | The instance of this registration
include_metadata = false # bool |  (optional) (default to false)

try: 
    # Returns all configuration settings for this registration instance
    api_response = api_instance.get_registration_instance_configuration(registration_id, instance_id, include_metadata=include_metadata)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationApi->get_registration_instance_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **instance_id** | **int**| The instance of this registration | 
 **include_metadata** | **bool**|  | [optional] [default to false]

### Return type

[**SettingListSchema**](SettingListSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_instance_launch_history**
> LaunchHistoryListSchema get_registration_instance_launch_history(registration_id, instance_id, include_history_log=include_history_log)

Returns history of this registration's launches

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
instance_id = 56 # int | The instance of this registration
include_history_log = false # bool | Whether to include the history log in the launch history (optional) (default to false)

try: 
    # Returns history of this registration's launches
    api_response = api_instance.get_registration_instance_launch_history(registration_id, instance_id, include_history_log=include_history_log)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationApi->get_registration_instance_launch_history: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **instance_id** | **int**| The instance of this registration | 
 **include_history_log** | **bool**| Whether to include the history log in the launch history | [optional] [default to false]

### Return type

[**LaunchHistoryListSchema**](LaunchHistoryListSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_instance_progress**
> RegistrationSchema get_registration_instance_progress(registration_id, instance_id, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime)

Get registration progress for instance `instanceId` of `registrationId`

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
instance_id = 56 # int | The instance of this registration
include_child_results = false # bool | Include information about each learning object, not just the top level in the results (optional) (default to false)
include_interactions_and_objectives = false # bool | Include interactions and objectives in the results (optional) (default to false)
include_runtime = false # bool | Include runtime details in the results (optional) (default to false)

try: 
    # Get registration progress for instance `instanceId` of `registrationId`
    api_response = api_instance.get_registration_instance_progress(registration_id, instance_id, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationApi->get_registration_instance_progress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **instance_id** | **int**| The instance of this registration | 
 **include_child_results** | **bool**| Include information about each learning object, not just the top level in the results | [optional] [default to false]
 **include_interactions_and_objectives** | **bool**| Include interactions and objectives in the results | [optional] [default to false]
 **include_runtime** | **bool**| Include runtime details in the results | [optional] [default to false]

### Return type

[**RegistrationSchema**](RegistrationSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_instance_statements**
> XapiStatementResult get_registration_instance_statements(registration_id, instance_id, since=since, until=until, more=more)

Get xAPI statements for instance `instanceId` of `registrationId`

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
instance_id = 56 # int | The instance of this registration
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of registration lists, where needed. An opaque value, construction and parsing may change without notice. (optional)

try: 
    # Get xAPI statements for instance `instanceId` of `registrationId`
    api_response = api_instance.get_registration_instance_statements(registration_id, instance_id, since=since, until=until, more=more)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationApi->get_registration_instance_statements: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **instance_id** | **int**| The instance of this registration | 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **more** | **str**| Value for this parameter will be provided in the &#39;more&#39; property of registration lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 

### Return type

[**XapiStatementResult**](XapiStatementResult.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_instances**
> RegistrationListSchema get_registration_instances(registration_id, until=until, since=since, more=more, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime)

Get all the instances of this the registration specified by the registration ID

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of registration lists, where needed. An opaque value, construction and parsing may change without notice. (optional)
include_child_results = false # bool | Include information about each learning object, not just the top level in the results (optional) (default to false)
include_interactions_and_objectives = false # bool | Include interactions and objectives in the results (optional) (default to false)
include_runtime = false # bool | Include runtime details in the results (optional) (default to false)

try: 
    # Get all the instances of this the registration specified by the registration ID
    api_response = api_instance.get_registration_instances(registration_id, until=until, since=since, more=more, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationApi->get_registration_instances: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **until** | **datetime**| Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **more** | **str**| Value for this parameter will be provided in the &#39;more&#39; property of registration lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 
 **include_child_results** | **bool**| Include information about each learning object, not just the top level in the results | [optional] [default to false]
 **include_interactions_and_objectives** | **bool**| Include interactions and objectives in the results | [optional] [default to false]
 **include_runtime** | **bool**| Include runtime details in the results | [optional] [default to false]

### Return type

[**RegistrationListSchema**](RegistrationListSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_launch_history**
> LaunchHistoryListSchema get_registration_launch_history(registration_id, include_history_log=include_history_log)

Returns history of this registration's launches

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
include_history_log = false # bool | Whether to include the history log in the launch history (optional) (default to false)

try: 
    # Returns history of this registration's launches
    api_response = api_instance.get_registration_launch_history(registration_id, include_history_log=include_history_log)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationApi->get_registration_launch_history: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **include_history_log** | **bool**| Whether to include the history log in the launch history | [optional] [default to false]

### Return type

[**LaunchHistoryListSchema**](LaunchHistoryListSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_launch_link**
> LaunchLinkSchema get_registration_launch_link(registration_id, launch_link_request)

Returns the link to use to launch this registration

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
launch_link_request = rustici_software_cloud_v2.LaunchLinkRequestSchema() # LaunchLinkRequestSchema | 

try: 
    # Returns the link to use to launch this registration
    api_response = api_instance.get_registration_launch_link(registration_id, launch_link_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationApi->get_registration_launch_link: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **launch_link_request** | [**LaunchLinkRequestSchema**](LaunchLinkRequestSchema.md)|  | 

### Return type

[**LaunchLinkSchema**](LaunchLinkSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_progress**
> RegistrationSchema get_registration_progress(registration_id, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime)

Get registration progress for `registrationId`

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
include_child_results = false # bool | Include information about each learning object, not just the top level in the results (optional) (default to false)
include_interactions_and_objectives = false # bool | Include interactions and objectives in the results (optional) (default to false)
include_runtime = false # bool | Include runtime details in the results (optional) (default to false)

try: 
    # Get registration progress for `registrationId`
    api_response = api_instance.get_registration_progress(registration_id, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationApi->get_registration_progress: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **include_child_results** | **bool**| Include information about each learning object, not just the top level in the results | [optional] [default to false]
 **include_interactions_and_objectives** | **bool**| Include interactions and objectives in the results | [optional] [default to false]
 **include_runtime** | **bool**| Include runtime details in the results | [optional] [default to false]

### Return type

[**RegistrationSchema**](RegistrationSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_statements**
> XapiStatementResult get_registration_statements(registration_id, since=since, until=until, more=more)

Get xAPI statements for `registrationId`

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of registration lists, where needed. An opaque value, construction and parsing may change without notice. (optional)

try: 
    # Get xAPI statements for `registrationId`
    api_response = api_instance.get_registration_statements(registration_id, since=since, until=until, more=more)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationApi->get_registration_statements: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **more** | **str**| Value for this parameter will be provided in the &#39;more&#39; property of registration lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 

### Return type

[**XapiStatementResult**](XapiStatementResult.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registrations**
> RegistrationListSchema get_registrations(course_id=course_id, learner_id=learner_id, since=since, until=until, more=more, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime)

Gets a list of registrations including a summary of the status of each registration.

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
course_id = 'course_id_example' # str | Only registrations for the specified course id will be included. (optional)
learner_id = 'learner_id_example' # str | Only registrations for the specified learner id will be included. (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of registration lists, where needed. An opaque value, construction and parsing may change without notice. (optional)
include_child_results = false # bool | Include information about each learning object, not just the top level in the results (optional) (default to false)
include_interactions_and_objectives = false # bool | Include interactions and objectives in the results (optional) (default to false)
include_runtime = false # bool | Include runtime details in the results (optional) (default to false)

try: 
    # Gets a list of registrations including a summary of the status of each registration.
    api_response = api_instance.get_registrations(course_id=course_id, learner_id=learner_id, since=since, until=until, more=more, include_child_results=include_child_results, include_interactions_and_objectives=include_interactions_and_objectives, include_runtime=include_runtime)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationApi->get_registrations: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| Only registrations for the specified course id will be included. | [optional] 
 **learner_id** | **str**| Only registrations for the specified learner id will be included. | [optional] 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **more** | **str**| Value for this parameter will be provided in the &#39;more&#39; property of registration lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 
 **include_child_results** | **bool**| Include information about each learning object, not just the top level in the results | [optional] [default to false]
 **include_interactions_and_objectives** | **bool**| Include interactions and objectives in the results | [optional] [default to false]
 **include_runtime** | **bool**| Include runtime details in the results | [optional] [default to false]

### Return type

[**RegistrationListSchema**](RegistrationListSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registration_exists**
> registration_exists(registration_id)

Does this registration exist?

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration

try: 
    # Does this registration exist?
    api_instance.registration_exists(registration_id)
except ApiException as e:
    print "Exception when calling RegistrationApi->registration_exists: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_registration_configuration**
> set_registration_configuration(registration_id, configuration_settings)

Set configuration settings for this registration.

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
configuration_settings = rustici_software_cloud_v2.SettingsPostSchema() # SettingsPostSchema | 

try: 
    # Set configuration settings for this registration.
    api_instance.set_registration_configuration(registration_id, configuration_settings)
except ApiException as e:
    print "Exception when calling RegistrationApi->set_registration_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **configuration_settings** | [**SettingsPostSchema**](SettingsPostSchema.md)|  | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_registration_instance_configuration**
> set_registration_instance_configuration(registration_id, instance_id, configuration_settings)

Set configuration settings for this registration instance.

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: OAUTH
rustici_software_cloud_v2.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.RegistrationApi()
registration_id = 'registration_id_example' # str | id for this registration
instance_id = 56 # int | The instance of this registration
configuration_settings = rustici_software_cloud_v2.SettingsPostSchema() # SettingsPostSchema | 

try: 
    # Set configuration settings for this registration instance.
    api_instance.set_registration_instance_configuration(registration_id, instance_id, configuration_settings)
except ApiException as e:
    print "Exception when calling RegistrationApi->set_registration_instance_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| id for this registration | 
 **instance_id** | **int**| The instance of this registration | 
 **configuration_settings** | [**SettingsPostSchema**](SettingsPostSchema.md)|  | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

