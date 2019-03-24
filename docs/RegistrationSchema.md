# RegistrationSchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**instance** | **int** |  | [optional] 
**xapi_registration_id** | **str** | xAPI registration id associated with this registration | [optional] 
**dispatch_id** | **str** | Dispatch ID for this registration, if applicable | [optional] 
**updated** | **datetime** |  | [optional] 
**registration_completion** | [**RegistrationCompletion**](RegistrationCompletion.md) |  | [optional] 
**registration_completion_amount** | **float** |  | [optional] 
**registration_success** | [**RegistrationSuccess**](RegistrationSuccess.md) |  | [optional] 
**score** | [**ScoreSchema**](ScoreSchema.md) |  | [optional] 
**total_seconds_tracked** | **float** |  | [optional] 
**first_access_date** | **datetime** |  | [optional] 
**last_access_date** | **datetime** |  | [optional] 
**completed_date** | **datetime** |  | [optional] 
**created_date** | **datetime** |  | [optional] 
**course** | [**CourseReferenceSchema**](CourseReferenceSchema.md) |  | [optional] 
**learner** | [**LearnerSchema**](LearnerSchema.md) |  | [optional] 
**global_objectives** | [**list[ObjectiveSchema]**](ObjectiveSchema.md) |  | [optional] 
**shared_data** | [**list[SharedDataEntrySchema]**](SharedDataEntrySchema.md) |  | [optional] 
**suspended_activity_id** | **str** |  | [optional] 
**activity_details** | [**ActivityResultSchema**](ActivityResultSchema.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


