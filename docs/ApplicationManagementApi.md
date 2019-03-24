# rustici_software_cloud_v2.ApplicationManagementApi

All URIs are relative to *https://dev.cloud.scorm.com/api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application**](ApplicationManagementApi.md#create_application) | **PUT** /appManagement/applications/{applicationName} | Create a new application
[**create_credential**](ApplicationManagementApi.md#create_credential) | **POST** /appManagement/{childAppId}/credentials | Create credential
[**create_token**](ApplicationManagementApi.md#create_token) | **POST** /appManagement/token | Create token
[**delete_application**](ApplicationManagementApi.md#delete_application) | **DELETE** /appManagement/applications/{childAppId} | Delete an application.  If the application contains content, it must first be manually removed before calling this method, else an error will be thrown.
[**delete_credential**](ApplicationManagementApi.md#delete_credential) | **DELETE** /appManagement/{childAppId}/credentials/{credentialId} | Removes &#x60;credentialId&#x60; credentials
[**get_application_configuration**](ApplicationManagementApi.md#get_application_configuration) | **GET** /appManagement/configuration | Returns all configuration settings for this level
[**get_application_list**](ApplicationManagementApi.md#get_application_list) | **GET** /appManagement/applications | Get list of all applications in this realm.
[**get_credentials**](ApplicationManagementApi.md#get_credentials) | **GET** /appManagement/{childAppId}/credentials | List of credentials
[**set_application_configuration**](ApplicationManagementApi.md#set_application_configuration) | **POST** /appManagement/configuration | Set configuration settings for this level.
[**update_credential**](ApplicationManagementApi.md#update_credential) | **PUT** /appManagement/{childAppId}/credentials/{credentialId} | Update the name or status associated with &#x60;credentialId&#x60;


# **create_application**
> ApplicationSchema create_application(application_name)

Create a new application

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
api_instance = rustici_software_cloud_v2.ApplicationManagementApi()
application_name = 'application_name_example' # str | 

try: 
    # Create a new application
    api_response = api_instance.create_application(application_name)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationManagementApi->create_application: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_name** | **str**|  | 

### Return type

[**ApplicationSchema**](ApplicationSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_credential**
> CredentialCreatedSchema create_credential(child_app_id, credential_request)

Create credential

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
api_instance = rustici_software_cloud_v2.ApplicationManagementApi()
child_app_id = 'child_app_id_example' # str | 
credential_request = rustici_software_cloud_v2.CredentialRequestSchema() # CredentialRequestSchema | 

try: 
    # Create credential
    api_response = api_instance.create_credential(child_app_id, credential_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationManagementApi->create_credential: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_app_id** | **str**|  | 
 **credential_request** | [**CredentialRequestSchema**](CredentialRequestSchema.md)|  | 

### Return type

[**CredentialCreatedSchema**](CredentialCreatedSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token**
> StringResultSchema create_token(token_request)

Create token

Creates, signs and returns a token based on the provided permissions, if the credentials used to request the token have the permissions being requested. Note: the token is not stored and therefore can not be modified or deleted. The requested permissions are encoded in the token which is then signed. As long as the secret used to create it is not changed the token will be valid until it expires.

### Example 
```python
import time
import rustici_software_cloud_v2
from rustici_software_cloud_v2.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: APP_NORMAL
rustici_software_cloud_v2.configuration.username = 'YOUR_USERNAME'
rustici_software_cloud_v2.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = rustici_software_cloud_v2.ApplicationManagementApi()
token_request = rustici_software_cloud_v2.TokenRequestSchema() # TokenRequestSchema | 

try: 
    # Create token
    api_response = api_instance.create_token(token_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationManagementApi->create_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_request** | [**TokenRequestSchema**](TokenRequestSchema.md)|  | 

### Return type

[**StringResultSchema**](StringResultSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application**
> delete_application(child_app_id)

Delete an application.  If the application contains content, it must first be manually removed before calling this method, else an error will be thrown.

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
api_instance = rustici_software_cloud_v2.ApplicationManagementApi()
child_app_id = 'child_app_id_example' # str | 

try: 
    # Delete an application.  If the application contains content, it must first be manually removed before calling this method, else an error will be thrown.
    api_instance.delete_application(child_app_id)
except ApiException as e:
    print "Exception when calling ApplicationManagementApi->delete_application: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_app_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credential**
> delete_credential(child_app_id, credential_id)

Removes `credentialId` credentials

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
api_instance = rustici_software_cloud_v2.ApplicationManagementApi()
child_app_id = 'child_app_id_example' # str | 
credential_id = 'credential_id_example' # str | 

try: 
    # Removes `credentialId` credentials
    api_instance.delete_credential(child_app_id, credential_id)
except ApiException as e:
    print "Exception when calling ApplicationManagementApi->delete_credential: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_app_id** | **str**|  | 
 **credential_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_configuration**
> SettingListSchema get_application_configuration(learning_standard=learning_standard, single_sco=single_sco, include_metadata=include_metadata)

Returns all configuration settings for this level

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
api_instance = rustici_software_cloud_v2.ApplicationManagementApi()
learning_standard = 'learning_standard_example' # str | If specified, the request will be scoped to the provided learning standard. (optional)
single_sco = true # bool | Required if learningStandard is specified. Scopes settings to whether a package has only one SCO or assignable unit within it or not. To apply a configuration setting to a learning standard for single and multi-SCO content, it must be set for both scopes. (optional)
include_metadata = false # bool |  (optional) (default to false)

try: 
    # Returns all configuration settings for this level
    api_response = api_instance.get_application_configuration(learning_standard=learning_standard, single_sco=single_sco, include_metadata=include_metadata)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationManagementApi->get_application_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **learning_standard** | **str**| If specified, the request will be scoped to the provided learning standard. | [optional] 
 **single_sco** | **bool**| Required if learningStandard is specified. Scopes settings to whether a package has only one SCO or assignable unit within it or not. To apply a configuration setting to a learning standard for single and multi-SCO content, it must be set for both scopes. | [optional] 
 **include_metadata** | **bool**|  | [optional] [default to false]

### Return type

[**SettingListSchema**](SettingListSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_list**
> ApplicationListSchema get_application_list()

Get list of all applications in this realm.

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
api_instance = rustici_software_cloud_v2.ApplicationManagementApi()

try: 
    # Get list of all applications in this realm.
    api_response = api_instance.get_application_list()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationManagementApi->get_application_list: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationListSchema**](ApplicationListSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credentials**
> CredentialListSchema get_credentials(child_app_id)

List of credentials

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
api_instance = rustici_software_cloud_v2.ApplicationManagementApi()
child_app_id = 'child_app_id_example' # str | 

try: 
    # List of credentials
    api_response = api_instance.get_credentials(child_app_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling ApplicationManagementApi->get_credentials: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_app_id** | **str**|  | 

### Return type

[**CredentialListSchema**](CredentialListSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_application_configuration**
> set_application_configuration(configuration_settings, learning_standard=learning_standard, single_sco=single_sco)

Set configuration settings for this level.

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
api_instance = rustici_software_cloud_v2.ApplicationManagementApi()
configuration_settings = rustici_software_cloud_v2.SettingsPostSchema() # SettingsPostSchema | 
learning_standard = 'learning_standard_example' # str | If specified, the request will be scoped to the provided learning standard. (optional)
single_sco = true # bool | Required if learningStandard is specified. Scopes settings to whether a package has only one SCO or assignable unit within it or not. To apply a configuration setting to a learning standard for single and multi-SCO content, it must be set for both scopes. (optional)

try: 
    # Set configuration settings for this level.
    api_instance.set_application_configuration(configuration_settings, learning_standard=learning_standard, single_sco=single_sco)
except ApiException as e:
    print "Exception when calling ApplicationManagementApi->set_application_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configuration_settings** | [**SettingsPostSchema**](SettingsPostSchema.md)|  | 
 **learning_standard** | **str**| If specified, the request will be scoped to the provided learning standard. | [optional] 
 **single_sco** | **bool**| Required if learningStandard is specified. Scopes settings to whether a package has only one SCO or assignable unit within it or not. To apply a configuration setting to a learning standard for single and multi-SCO content, it must be set for both scopes. | [optional] 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_credential**
> update_credential(child_app_id, credential_id, credential_update)

Update the name or status associated with `credentialId`

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
api_instance = rustici_software_cloud_v2.ApplicationManagementApi()
child_app_id = 'child_app_id_example' # str | 
credential_id = 'credential_id_example' # str | 
credential_update = rustici_software_cloud_v2.CredentialRequestSchema() # CredentialRequestSchema | 

try: 
    # Update the name or status associated with `credentialId`
    api_instance.update_credential(child_app_id, credential_id, credential_update)
except ApiException as e:
    print "Exception when calling ApplicationManagementApi->update_credential: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_app_id** | **str**|  | 
 **credential_id** | **str**|  | 
 **credential_update** | [**CredentialRequestSchema**](CredentialRequestSchema.md)|  | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

