# LaunchHistorySchema

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**instance** | **int** |  | [optional] 
**score** | [**ScoreSchema**](ScoreSchema.md) |  | [optional] 
**completion_status** | **str** |  | [optional] [default to 'UNKNOWN']
**success_status** | **str** |  | [optional] [default to 'UNKNOWN']
**history_log** | **str** |  | [optional] 
**total_seconds_tracked** | **float** |  | [optional] 
**launch_time** | **datetime** | The time of the launch in UTC | [optional] 
**exit_time** | **datetime** | The time of the exit in UTC | [optional] 
**last_runtime_update** | **datetime** | The time of the last runtime update in UTC | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


