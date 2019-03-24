# CourseActivitySchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_identifier** | **str** | An arbitrary identifier that the external LMS system can associate with this LearningObject to track it as it isreused across courses  | [optional] 
**item_identifier** | **str** | The string which identifies this activity in the context of its course | [optional] 
**resource_identifier** | **str** | The string which identifies this activity&#39;s resource in a course&#39;s manifest | [optional] 
**activity_type** | **str** | The type of activity this is | [optional] 
**href** | **str** | The web path used to launch this activity | [optional] 
**scaled_passing_score** | **str** | The score required of a learner to pass this activity | [optional] 
**title** | **str** | The title of the activity | [optional] 
**children** | [**list[CourseActivitySchema]**](CourseActivitySchema.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


