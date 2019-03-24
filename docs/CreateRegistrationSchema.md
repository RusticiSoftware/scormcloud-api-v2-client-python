# CreateRegistrationSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**course_id** | **str** |  | 
**learner** | [**LearnerSchema**](LearnerSchema.md) |  | 
**registration_id** | **str** |  | 
**xapi_registration_id** | **str** | The xapiRegistrationId to be associated with this registration. If not specified, the system will assign an xapiRegistrationId. As per the xApi specification, this must be a UUID. | [optional] 
**learner_tags** | **list[str]** |  | [optional] 
**course_tags** | **list[str]** |  | [optional] 
**registration_tags** | **list[str]** |  | [optional] 
**post_back** | [**PostBackSchema**](PostBackSchema.md) | Specifies an optional override URL for which to post activity and status data in real time as the course is completed. By default all of these settings are read from your configuration. | [optional] 
**initial_registration_state** | [**RegistrationSchema**](RegistrationSchema.md) |  | [optional] 
**initial_settings** | [**SettingsPostSchema**](SettingsPostSchema.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


