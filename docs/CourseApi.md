# rustici_software_cloud_v2.CourseApi

All URIs are relative to *https://dev.cloud.scorm.com/api/v2/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_course_preview_launch_link**](CourseApi.md#build_course_preview_launch_link) | **POST** /courses/{courseId}/preview | Returns the launch link to use to preview this course
[**build_course_preview_launch_link_with_version**](CourseApi.md#build_course_preview_launch_link_with_version) | **POST** /courses/{courseId}/versions/{versionId}/preview | Returns the link to use to preview this course
[**create_fetch_and_import_course_job**](CourseApi.md#create_fetch_and_import_course_job) | **POST** /courses/importJobs | Start a job to fetch and import a course.
[**create_upload_and_import_course_job**](CourseApi.md#create_upload_and_import_course_job) | **POST** /courses/importJobs/upload | Upload a course and start an import job for it.
[**delete_course**](CourseApi.md#delete_course) | **DELETE** /courses/{courseId} | Delete &#x60;courseId&#x60;
[**delete_course_configuration_setting**](CourseApi.md#delete_course_configuration_setting) | **DELETE** /courses/{courseId}/configuration/{settingId} | Clears the &#x60;settingId&#x60; value for this course
[**delete_course_version**](CourseApi.md#delete_course_version) | **DELETE** /courses/{courseId}/versions/{versionId} | Delete version &#x60;versionId&#x60; of &#x60;courseId&#x60;
[**delete_course_version_configuration_setting**](CourseApi.md#delete_course_version_configuration_setting) | **DELETE** /courses/{courseId}/versions/{versionId}/configuration/{settingId} | Clears the &#x60;settingId&#x60; value for this course and version.
[**get_course**](CourseApi.md#get_course) | **GET** /courses/{courseId} | Get information about &#x60;courseId&#x60;
[**get_course_configuration**](CourseApi.md#get_course_configuration) | **GET** /courses/{courseId}/configuration | Returns all configuration settings for this course
[**get_course_statements**](CourseApi.md#get_course_statements) | **GET** /courses/{courseId}/xAPIStatements | Get xAPI statements for &#x60;courseId&#x60;
[**get_course_version_configuration**](CourseApi.md#get_course_version_configuration) | **GET** /courses/{courseId}/versions/{versionId}/configuration | Returns all configuration settings for this course and version.
[**get_course_version_info**](CourseApi.md#get_course_version_info) | **GET** /courses/{courseId}/versions/{versionId} | Get version &#x60;versionId&#x60; of &#x60;courseId&#x60;
[**get_course_version_statements**](CourseApi.md#get_course_version_statements) | **GET** /courses/{courseId}/versions/{versionId}/xAPIStatements | Get xAPI statements for version &#x60;versionId&#x60; of &#x60;courseId&#x60;
[**get_course_versions**](CourseApi.md#get_course_versions) | **GET** /courses/{courseId}/versions | Get all versions of &#x60;courseId&#x60;
[**get_courses**](CourseApi.md#get_courses) | **GET** /courses | Get all courses for &#x60;appId&#x60;
[**get_import_job_status**](CourseApi.md#get_import_job_status) | **GET** /courses/importJobs/{importJobId} | Check the status of an import job.
[**set_course_configuration**](CourseApi.md#set_course_configuration) | **POST** /courses/{courseId}/configuration | Set configuration settings for this course.
[**set_course_title**](CourseApi.md#set_course_title) | **PUT** /courses/{courseId}/title | Sets the course title for &#x60;courseId&#x60;
[**set_course_version_configuration**](CourseApi.md#set_course_version_configuration) | **POST** /courses/{courseId}/versions/{versionId}/configuration | Set configuration settings for this course and version.


# **build_course_preview_launch_link**
> LaunchLinkSchema build_course_preview_launch_link(course_id, launch_link_request, css_url=css_url)

Returns the launch link to use to preview this course

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
launch_link_request = rustici_software_cloud_v2.LaunchLinkRequestSchema() # LaunchLinkRequestSchema | 
css_url = 'css_url_example' # str |  (optional)

try: 
    # Returns the launch link to use to preview this course
    api_response = api_instance.build_course_preview_launch_link(course_id, launch_link_request, css_url=css_url)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->build_course_preview_launch_link: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **launch_link_request** | [**LaunchLinkRequestSchema**](LaunchLinkRequestSchema.md)|  | 
 **css_url** | **str**|  | [optional] 

### Return type

[**LaunchLinkSchema**](LaunchLinkSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **build_course_preview_launch_link_with_version**
> LaunchLinkSchema build_course_preview_launch_link_with_version(course_id, version_id, launch_link_request)

Returns the link to use to preview this course

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
version_id = 56 # int | The course version
launch_link_request = rustici_software_cloud_v2.LaunchLinkRequestSchema() # LaunchLinkRequestSchema | 

try: 
    # Returns the link to use to preview this course
    api_response = api_instance.build_course_preview_launch_link_with_version(course_id, version_id, launch_link_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->build_course_preview_launch_link_with_version: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **version_id** | **int**| The course version | 
 **launch_link_request** | [**LaunchLinkRequestSchema**](LaunchLinkRequestSchema.md)|  | 

### Return type

[**LaunchLinkSchema**](LaunchLinkSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fetch_and_import_course_job**
> StringResultSchema create_fetch_and_import_course_job(course_id, import_request, may_create_new_version=may_create_new_version, postback_url=postback_url)

Start a job to fetch and import a course.

An import job will be started to fetch and import the referenced file, and the import job ID will be returned. If the import is successful, the imported course will be registered using the courseId provided.\"

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | A unique identifier your application will use to identify the course after import. Your application is responsible both for generating this unique ID and for keeping track of the ID for later use.
import_request = rustici_software_cloud_v2.ImportFetchRequestSchema() # ImportFetchRequestSchema | 
may_create_new_version = false # bool | Is it OK to create a new version of this course? If this is set to false and the course already exists, the upload will fail. If true and the course already exists then a new version will be created. No effect if the course doesn't already exist. (optional) (default to false)
postback_url = 'postback_url_example' # str | An optional parameter that specifies a URL to send a postback to when the course has finished uploading. (optional)

try: 
    # Start a job to fetch and import a course.
    api_response = api_instance.create_fetch_and_import_course_job(course_id, import_request, may_create_new_version=may_create_new_version, postback_url=postback_url)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->create_fetch_and_import_course_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| A unique identifier your application will use to identify the course after import. Your application is responsible both for generating this unique ID and for keeping track of the ID for later use. | 
 **import_request** | [**ImportFetchRequestSchema**](ImportFetchRequestSchema.md)|  | 
 **may_create_new_version** | **bool**| Is it OK to create a new version of this course? If this is set to false and the course already exists, the upload will fail. If true and the course already exists then a new version will be created. No effect if the course doesn&#39;t already exist. | [optional] [default to false]
 **postback_url** | **str**| An optional parameter that specifies a URL to send a postback to when the course has finished uploading. | [optional] 

### Return type

[**StringResultSchema**](StringResultSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_upload_and_import_course_job**
> StringResultSchema create_upload_and_import_course_job(course_id, may_create_new_version=may_create_new_version, file=file, postback_url=postback_url)

Upload a course and start an import job for it.

An import job will be started to import the posted file, and the import job ID will be returned. If the import is successful, the imported course will be registered using the courseId provided.

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | A unique identifier your application will use to identify the course after import. Your application is responsible both for generating this unique ID and for keeping track of the ID for later use.
may_create_new_version = false # bool | Is it OK to create a new version of this course? If this is set to false and the course already exists, the upload will fail. If true and the course already exists then a new version will be created. No effect if the course doesn't already exist. (optional) (default to false)
file = '/path/to/file.txt' # file | The zip file of the course contents to import. (optional)
postback_url = 'postback_url_example' # str | An optional parameter that specifies a URL to send a postback to when the course has finished uploading. (optional)

try: 
    # Upload a course and start an import job for it.
    api_response = api_instance.create_upload_and_import_course_job(course_id, may_create_new_version=may_create_new_version, file=file, postback_url=postback_url)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->create_upload_and_import_course_job: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| A unique identifier your application will use to identify the course after import. Your application is responsible both for generating this unique ID and for keeping track of the ID for later use. | 
 **may_create_new_version** | **bool**| Is it OK to create a new version of this course? If this is set to false and the course already exists, the upload will fail. If true and the course already exists then a new version will be created. No effect if the course doesn&#39;t already exist. | [optional] [default to false]
 **file** | **file**| The zip file of the course contents to import. | [optional] 
 **postback_url** | **str**| An optional parameter that specifies a URL to send a postback to when the course has finished uploading. | [optional] 

### Return type

[**StringResultSchema**](StringResultSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_course**
> delete_course(course_id)

Delete `courseId`

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 

try: 
    # Delete `courseId`
    api_instance.delete_course(course_id)
except ApiException as e:
    print "Exception when calling CourseApi->delete_course: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_course_configuration_setting**
> delete_course_configuration_setting(course_id, setting_id)

Clears the `settingId` value for this course

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
setting_id = 'setting_id_example' # str | 

try: 
    # Clears the `settingId` value for this course
    api_instance.delete_course_configuration_setting(course_id, setting_id)
except ApiException as e:
    print "Exception when calling CourseApi->delete_course_configuration_setting: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **setting_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_course_version**
> delete_course_version(course_id, version_id)

Delete version `versionId` of `courseId`

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
version_id = 56 # int | The course version

try: 
    # Delete version `versionId` of `courseId`
    api_instance.delete_course_version(course_id, version_id)
except ApiException as e:
    print "Exception when calling CourseApi->delete_course_version: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **version_id** | **int**| The course version | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_course_version_configuration_setting**
> delete_course_version_configuration_setting(course_id, version_id, setting_id)

Clears the `settingId` value for this course and version.

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
version_id = 56 # int | The course version
setting_id = 'setting_id_example' # str | 

try: 
    # Clears the `settingId` value for this course and version.
    api_instance.delete_course_version_configuration_setting(course_id, version_id, setting_id)
except ApiException as e:
    print "Exception when calling CourseApi->delete_course_version_configuration_setting: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **version_id** | **int**| The course version | 
 **setting_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course**
> CourseSchema get_course(course_id, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)

Get information about `courseId`

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
include_registration_count = false # bool | Include the registration count in the results (optional) (default to false)
include_course_metadata = false # bool | Include course metadata in the results. If the course has no metadata, adding this parameter has no effect. (optional) (default to false)

try: 
    # Get information about `courseId`
    api_response = api_instance.get_course(course_id, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->get_course: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **include_registration_count** | **bool**| Include the registration count in the results | [optional] [default to false]
 **include_course_metadata** | **bool**| Include course metadata in the results. If the course has no metadata, adding this parameter has no effect. | [optional] [default to false]

### Return type

[**CourseSchema**](CourseSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_configuration**
> SettingListSchema get_course_configuration(course_id, include_metadata=include_metadata)

Returns all configuration settings for this course

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
include_metadata = false # bool |  (optional) (default to false)

try: 
    # Returns all configuration settings for this course
    api_response = api_instance.get_course_configuration(course_id, include_metadata=include_metadata)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->get_course_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **include_metadata** | **bool**|  | [optional] [default to false]

### Return type

[**SettingListSchema**](SettingListSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_statements**
> XapiStatementResult get_course_statements(course_id, learner_id=learner_id, since=since, until=until, more=more)

Get xAPI statements for `courseId`

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
learner_id = 'learner_id_example' # str | Only entries for the specified learner id will be included. (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of registration lists, where needed. An opaque value, construction and parsing may change without notice. (optional)

try: 
    # Get xAPI statements for `courseId`
    api_response = api_instance.get_course_statements(course_id, learner_id=learner_id, since=since, until=until, more=more)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->get_course_statements: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **learner_id** | **str**| Only entries for the specified learner id will be included. | [optional] 
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

# **get_course_version_configuration**
> SettingListSchema get_course_version_configuration(course_id, version_id, include_metadata=include_metadata)

Returns all configuration settings for this course and version.

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
version_id = 56 # int | The course version
include_metadata = false # bool |  (optional) (default to false)

try: 
    # Returns all configuration settings for this course and version.
    api_response = api_instance.get_course_version_configuration(course_id, version_id, include_metadata=include_metadata)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->get_course_version_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **version_id** | **int**| The course version | 
 **include_metadata** | **bool**|  | [optional] [default to false]

### Return type

[**SettingListSchema**](SettingListSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_version_info**
> CourseSchema get_course_version_info(course_id, version_id, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)

Get version `versionId` of `courseId`

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
version_id = 56 # int | The course version
include_registration_count = false # bool | Include the registration count in the results (optional) (default to false)
include_course_metadata = false # bool | Include course metadata in the results. If the course has no metadata, adding this parameter has no effect. (optional) (default to false)

try: 
    # Get version `versionId` of `courseId`
    api_response = api_instance.get_course_version_info(course_id, version_id, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->get_course_version_info: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **version_id** | **int**| The course version | 
 **include_registration_count** | **bool**| Include the registration count in the results | [optional] [default to false]
 **include_course_metadata** | **bool**| Include course metadata in the results. If the course has no metadata, adding this parameter has no effect. | [optional] [default to false]

### Return type

[**CourseSchema**](CourseSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_course_version_statements**
> XapiStatementResult get_course_version_statements(course_id, version_id, learner_id=learner_id, since=since, until=until, more=more)

Get xAPI statements for version `versionId` of `courseId`

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
version_id = 56 # int | The course version
learner_id = 'learner_id_example' # str | Only entries for the specified learner id will be included. (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of registration lists, where needed. An opaque value, construction and parsing may change without notice. (optional)

try: 
    # Get xAPI statements for version `versionId` of `courseId`
    api_response = api_instance.get_course_version_statements(course_id, version_id, learner_id=learner_id, since=since, until=until, more=more)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->get_course_version_statements: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **version_id** | **int**| The course version | 
 **learner_id** | **str**| Only entries for the specified learner id will be included. | [optional] 
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

# **get_course_versions**
> CourseListNonPagedSchema get_course_versions(course_id, since=since, until=until, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)

Get all versions of `courseId`

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
include_registration_count = false # bool | Include the registration count in the results (optional) (default to false)
include_course_metadata = false # bool | Include course metadata in the results. If the course has no metadata, adding this parameter has no effect. (optional) (default to false)

try: 
    # Get all versions of `courseId`
    api_response = api_instance.get_course_versions(course_id, since=since, until=until, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->get_course_versions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **include_registration_count** | **bool**| Include the registration count in the results | [optional] [default to false]
 **include_course_metadata** | **bool**| Include course metadata in the results. If the course has no metadata, adding this parameter has no effect. | [optional] [default to false]

### Return type

[**CourseListNonPagedSchema**](CourseListNonPagedSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_courses**
> CourseListSchema get_courses(more=more, since=since, until=until, filter=filter, filter_by=filter_by, order_by=order_by, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata, tags=tags)

Get all courses for `appId`

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
api_instance = rustici_software_cloud_v2.CourseApi()
more = 'more_example' # str | Value for this parameter will be provided in the 'more' property of registration lists, where needed. An opaque value, construction and parsing may change without notice. (optional)
since = '2013-10-20T19:20:30+01:00' # datetime | Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. (optional)
filter = 'filter_example' # str | Optional string which filters results by a specified field (described by filterBy). (optional)
filter_by = 'filter_by_example' # str | Optional enum parameter for specifying the field on which to run the filter.  Defaults to course_id. (optional)
order_by = 'order_by_example' # str | Optional enum parameter for specifying the field and order by which to sort the results.  Defaults to creation_date_desc. (optional)
include_registration_count = false # bool | Include the registration count in the results (optional) (default to false)
include_course_metadata = false # bool | Include course metadata in the results. If the course has no metadata, adding this parameter has no effect. (optional) (default to false)
tags = ['tags_example'] # list[str] |  (optional)

try: 
    # Get all courses for `appId`
    api_response = api_instance.get_courses(more=more, since=since, until=until, filter=filter, filter_by=filter_by, order_by=order_by, include_registration_count=include_registration_count, include_course_metadata=include_course_metadata, tags=tags)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->get_courses: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **more** | **str**| Value for this parameter will be provided in the &#39;more&#39; property of registration lists, where needed. An opaque value, construction and parsing may change without notice. | [optional] 
 **since** | **datetime**| Only items updated since the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **until** | **datetime**| Only items updated before the specified ISO 8601 TimeStamp (inclusive) are included. If a time zone is not specified, UTC time zone will be used. | [optional] 
 **filter** | **str**| Optional string which filters results by a specified field (described by filterBy). | [optional] 
 **filter_by** | **str**| Optional enum parameter for specifying the field on which to run the filter.  Defaults to course_id. | [optional] 
 **order_by** | **str**| Optional enum parameter for specifying the field and order by which to sort the results.  Defaults to creation_date_desc. | [optional] 
 **include_registration_count** | **bool**| Include the registration count in the results | [optional] [default to false]
 **include_course_metadata** | **bool**| Include course metadata in the results. If the course has no metadata, adding this parameter has no effect. | [optional] [default to false]
 **tags** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**CourseListSchema**](CourseListSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_job_status**
> ImportResultSchema get_import_job_status(import_job_id)

Check the status of an import job.

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
api_instance = rustici_software_cloud_v2.CourseApi()
import_job_id = 'import_job_id_example' # str | Id received when the import job was submitted to the importJobs resource.

try: 
    # Check the status of an import job.
    api_response = api_instance.get_import_job_status(import_job_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->get_import_job_status: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_job_id** | **str**| Id received when the import job was submitted to the importJobs resource. | 

### Return type

[**ImportResultSchema**](ImportResultSchema.md)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_course_configuration**
> set_course_configuration(course_id, configuration_settings)

Set configuration settings for this course.

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
configuration_settings = rustici_software_cloud_v2.SettingsPostSchema() # SettingsPostSchema | 

try: 
    # Set configuration settings for this course.
    api_instance.set_course_configuration(course_id, configuration_settings)
except ApiException as e:
    print "Exception when calling CourseApi->set_course_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **configuration_settings** | [**SettingsPostSchema**](SettingsPostSchema.md)|  | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_course_title**
> str set_course_title(course_id, title)

Sets the course title for `courseId`

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
title = rustici_software_cloud_v2.TitleSchema() # TitleSchema | 

try: 
    # Sets the course title for `courseId`
    api_response = api_instance.set_course_title(course_id, title)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling CourseApi->set_course_title: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **title** | [**TitleSchema**](TitleSchema.md)|  | 

### Return type

**str**

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_course_version_configuration**
> set_course_version_configuration(course_id, version_id, configuration_settings)

Set configuration settings for this course and version.

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
api_instance = rustici_software_cloud_v2.CourseApi()
course_id = 'course_id_example' # str | 
version_id = 56 # int | The course version
configuration_settings = rustici_software_cloud_v2.SettingsPostSchema() # SettingsPostSchema | 

try: 
    # Set configuration settings for this course and version.
    api_instance.set_course_version_configuration(course_id, version_id, configuration_settings)
except ApiException as e:
    print "Exception when calling CourseApi->set_course_version_configuration: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **version_id** | **int**| The course version | 
 **configuration_settings** | [**SettingsPostSchema**](SettingsPostSchema.md)|  | 

### Return type

void (empty response body)

### Authorization

[APP_NORMAL](../README.md#APP_NORMAL), [OAUTH](../README.md#OAUTH)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

