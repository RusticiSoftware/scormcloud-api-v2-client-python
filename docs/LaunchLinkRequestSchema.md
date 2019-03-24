# LaunchLinkRequestSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **int** | Number of seconds from now this link will expire in. Defaults to 120s. Range 10s:300s | [optional] [default to 120]
**redirect_on_exit_url** | **str** | The URL the application should redirect to when the learner exits a course. If not specified, configured value will be used. | [optional] 
**tracking** | **bool** | Should this launch be tracked? If false, Engine will avoid tracking to the extent possible for the standard being used. | [optional] [default to True]
**start_sco** | **str** | For SCORM, SCO identifier to override launch, overriding the normal sequencing. | [optional] 
**culture** | **str** | This parameter should specify a culture code. If specified, and supported, the navigation and alerts in the player will be displayed in the associated language. If not specified, the locale of the user’s browser will be used. | [optional] 
**css_url** | **str** | A Url pointing to custom css for the player to use. | [optional] 
**learner_tags** | **list[str]** |  | [optional] 
**course_tags** | **list[str]** |  | [optional] 
**registration_tags** | **list[str]** |  | [optional] 
**additionalvalues** | [**list[ItemValuePairSchema]**](ItemValuePairSchema.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


