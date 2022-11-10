# coding: utf-8

# flake8: noqa

"""
    SCORM Cloud Rest API

    REST API used for SCORM Cloud integrations.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: systems@rusticisoftware.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from rustici_software_cloud_v2.api.about_api import AboutApi
from rustici_software_cloud_v2.api.application_management_api import ApplicationManagementApi
from rustici_software_cloud_v2.api.authentication_api import AuthenticationApi
from rustici_software_cloud_v2.api.content_connectors_api import ContentConnectorsApi
from rustici_software_cloud_v2.api.course_api import CourseApi
from rustici_software_cloud_v2.api.dispatch_api import DispatchApi
from rustici_software_cloud_v2.api.invitations_api import InvitationsApi
from rustici_software_cloud_v2.api.learner_api import LearnerApi
from rustici_software_cloud_v2.api.ping_api import PingApi
from rustici_software_cloud_v2.api.registration_api import RegistrationApi
from rustici_software_cloud_v2.api.reporting_api import ReportingApi
from rustici_software_cloud_v2.api.xapi_api import XapiApi
from rustici_software_cloud_v2.api.zoomi_api import ZoomiApi

# import ApiClient
from rustici_software_cloud_v2.api_client import ApiClient
from rustici_software_cloud_v2.configuration import Configuration
# import models into sdk package
from rustici_software_cloud_v2.models.about_schema import AboutSchema
from rustici_software_cloud_v2.models.activity_result_schema import ActivityResultSchema
from rustici_software_cloud_v2.models.application_info_list_schema import ApplicationInfoListSchema
from rustici_software_cloud_v2.models.application_info_schema import ApplicationInfoSchema
from rustici_software_cloud_v2.models.application_list_schema import ApplicationListSchema
from rustici_software_cloud_v2.models.application_request_schema import ApplicationRequestSchema
from rustici_software_cloud_v2.models.application_schema import ApplicationSchema
from rustici_software_cloud_v2.models.application_token import ApplicationToken
from rustici_software_cloud_v2.models.asset_file_schema import AssetFileSchema
from rustici_software_cloud_v2.models.batch_tags_schema import BatchTagsSchema
from rustici_software_cloud_v2.models.comment_schema import CommentSchema
from rustici_software_cloud_v2.models.completion_amount_schema import CompletionAmountSchema
from rustici_software_cloud_v2.models.connector_list_schema import ConnectorListSchema
from rustici_software_cloud_v2.models.connector_schema import ConnectorSchema
from rustici_software_cloud_v2.models.course_activity_schema import CourseActivitySchema
from rustici_software_cloud_v2.models.course_list_non_paged_schema import CourseListNonPagedSchema
from rustici_software_cloud_v2.models.course_list_schema import CourseListSchema
from rustici_software_cloud_v2.models.course_reference_schema import CourseReferenceSchema
from rustici_software_cloud_v2.models.course_schema import CourseSchema
from rustici_software_cloud_v2.models.create_connector_schema import CreateConnectorSchema
from rustici_software_cloud_v2.models.create_dispatch_id_schema import CreateDispatchIdSchema
from rustici_software_cloud_v2.models.create_dispatch_list_schema import CreateDispatchListSchema
from rustici_software_cloud_v2.models.create_dispatch_schema import CreateDispatchSchema
from rustici_software_cloud_v2.models.create_private_invitation_schema import CreatePrivateInvitationSchema
from rustici_software_cloud_v2.models.create_public_invitation_schema import CreatePublicInvitationSchema
from rustici_software_cloud_v2.models.create_registration_schema import CreateRegistrationSchema
from rustici_software_cloud_v2.models.credential_created_schema import CredentialCreatedSchema
from rustici_software_cloud_v2.models.credential_list_schema import CredentialListSchema
from rustici_software_cloud_v2.models.credential_request_schema import CredentialRequestSchema
from rustici_software_cloud_v2.models.credential_schema import CredentialSchema
from rustici_software_cloud_v2.models.destination_id_schema import DestinationIdSchema
from rustici_software_cloud_v2.models.destination_list_schema import DestinationListSchema
from rustici_software_cloud_v2.models.destination_schema import DestinationSchema
from rustici_software_cloud_v2.models.dispatch_id_schema import DispatchIdSchema
from rustici_software_cloud_v2.models.dispatch_list_schema import DispatchListSchema
from rustici_software_cloud_v2.models.dispatch_lti13_info_schema import DispatchLti13InfoSchema
from rustici_software_cloud_v2.models.dispatch_lti_info_schema import DispatchLtiInfoSchema
from rustici_software_cloud_v2.models.dispatch_registration_count_schema import DispatchRegistrationCountSchema
from rustici_software_cloud_v2.models.dispatch_schema import DispatchSchema
from rustici_software_cloud_v2.models.enabled_schema import EnabledSchema
from rustici_software_cloud_v2.models.file_list_item_schema import FileListItemSchema
from rustici_software_cloud_v2.models.file_list_schema import FileListSchema
from rustici_software_cloud_v2.models.import_asset_request_schema import ImportAssetRequestSchema
from rustici_software_cloud_v2.models.import_connector_request_schema import ImportConnectorRequestSchema
from rustici_software_cloud_v2.models.import_fetch_request_schema import ImportFetchRequestSchema
from rustici_software_cloud_v2.models.import_job_result_schema import ImportJobResultSchema
from rustici_software_cloud_v2.models.import_media_file_reference_request_schema import ImportMediaFileReferenceRequestSchema
from rustici_software_cloud_v2.models.import_request_schema import ImportRequestSchema
from rustici_software_cloud_v2.models.import_result_schema import ImportResultSchema
from rustici_software_cloud_v2.models.integer_result_schema import IntegerResultSchema
from rustici_software_cloud_v2.models.invitation_email_schema import InvitationEmailSchema
from rustici_software_cloud_v2.models.invitation_job_status_schema import InvitationJobStatusSchema
from rustici_software_cloud_v2.models.invitation_summary_list import InvitationSummaryList
from rustici_software_cloud_v2.models.invitation_summary_schema import InvitationSummarySchema
from rustici_software_cloud_v2.models.item_value_pair_schema import ItemValuePairSchema
from rustici_software_cloud_v2.models.launch_auth_options_schema import LaunchAuthOptionsSchema
from rustici_software_cloud_v2.models.launch_auth_schema import LaunchAuthSchema
from rustici_software_cloud_v2.models.launch_history_list_schema import LaunchHistoryListSchema
from rustici_software_cloud_v2.models.launch_history_schema import LaunchHistorySchema
from rustici_software_cloud_v2.models.launch_link_request_schema import LaunchLinkRequestSchema
from rustici_software_cloud_v2.models.launch_link_schema import LaunchLinkSchema
from rustici_software_cloud_v2.models.learner_preference_schema import LearnerPreferenceSchema
from rustici_software_cloud_v2.models.learner_schema import LearnerSchema
from rustici_software_cloud_v2.models.lti13_platform_configuration_schema import Lti13PlatformConfigurationSchema
from rustici_software_cloud_v2.models.lti13_tool_configuration_schema import Lti13ToolConfigurationSchema
from rustici_software_cloud_v2.models.media_file_metadata_schema import MediaFileMetadataSchema
from rustici_software_cloud_v2.models.message_schema import MessageSchema
from rustici_software_cloud_v2.models.metadata_schema import MetadataSchema
from rustici_software_cloud_v2.models.objective_schema import ObjectiveSchema
from rustici_software_cloud_v2.models.paginated_list import PaginatedList
from rustici_software_cloud_v2.models.permissions_schema import PermissionsSchema
from rustici_software_cloud_v2.models.ping_schema import PingSchema
from rustici_software_cloud_v2.models.post_back_schema import PostBackSchema
from rustici_software_cloud_v2.models.private_invitation_list import PrivateInvitationList
from rustici_software_cloud_v2.models.private_invitation_schema import PrivateInvitationSchema
from rustici_software_cloud_v2.models.private_invitation_update_schema import PrivateInvitationUpdateSchema
from rustici_software_cloud_v2.models.public_invitation_list import PublicInvitationList
from rustici_software_cloud_v2.models.public_invitation_schema import PublicInvitationSchema
from rustici_software_cloud_v2.models.public_invitation_update_schema import PublicInvitationUpdateSchema
from rustici_software_cloud_v2.models.registration_completion import RegistrationCompletion
from rustici_software_cloud_v2.models.registration_list_schema import RegistrationListSchema
from rustici_software_cloud_v2.models.registration_schema import RegistrationSchema
from rustici_software_cloud_v2.models.registration_success import RegistrationSuccess
from rustici_software_cloud_v2.models.reportage_account_info_schema import ReportageAccountInfoSchema
from rustici_software_cloud_v2.models.reportage_account_info_usage_schema import ReportageAccountInfoUsageSchema
from rustici_software_cloud_v2.models.reportage_auth_token_schema import ReportageAuthTokenSchema
from rustici_software_cloud_v2.models.reportage_link_schema import ReportageLinkSchema
from rustici_software_cloud_v2.models.response_error import ResponseError
from rustici_software_cloud_v2.models.runtime_interaction_schema import RuntimeInteractionSchema
from rustici_software_cloud_v2.models.runtime_objective_schema import RuntimeObjectiveSchema
from rustici_software_cloud_v2.models.runtime_schema import RuntimeSchema
from rustici_software_cloud_v2.models.score_schema import ScoreSchema
from rustici_software_cloud_v2.models.setting_item import SettingItem
from rustici_software_cloud_v2.models.setting_list_schema import SettingListSchema
from rustici_software_cloud_v2.models.setting_metadata import SettingMetadata
from rustici_software_cloud_v2.models.setting_valid_value import SettingValidValue
from rustici_software_cloud_v2.models.settings_individual_schema import SettingsIndividualSchema
from rustici_software_cloud_v2.models.settings_post_schema import SettingsPostSchema
from rustici_software_cloud_v2.models.shared_data_entry_schema import SharedDataEntrySchema
from rustici_software_cloud_v2.models.static_properties_schema import StaticPropertiesSchema
from rustici_software_cloud_v2.models.string_result_schema import StringResultSchema
from rustici_software_cloud_v2.models.tag_list_schema import TagListSchema
from rustici_software_cloud_v2.models.title_schema import TitleSchema
from rustici_software_cloud_v2.models.token_request_schema import TokenRequestSchema
from rustici_software_cloud_v2.models.update_application_schema import UpdateApplicationSchema
from rustici_software_cloud_v2.models.update_connector_schema import UpdateConnectorSchema
from rustici_software_cloud_v2.models.update_dispatch_schema import UpdateDispatchSchema
from rustici_software_cloud_v2.models.user_invitation_list import UserInvitationList
from rustici_software_cloud_v2.models.user_invitation_schema import UserInvitationSchema
from rustici_software_cloud_v2.models.user_invitation_schema_registration_report import UserInvitationSchemaRegistrationReport
from rustici_software_cloud_v2.models.xapi_account import XapiAccount
from rustici_software_cloud_v2.models.xapi_activity import XapiActivity
from rustici_software_cloud_v2.models.xapi_activity_definition import XapiActivityDefinition
from rustici_software_cloud_v2.models.xapi_agent_group import XapiAgentGroup
from rustici_software_cloud_v2.models.xapi_attachment import XapiAttachment
from rustici_software_cloud_v2.models.xapi_context import XapiContext
from rustici_software_cloud_v2.models.xapi_context_activity import XapiContextActivity
from rustici_software_cloud_v2.models.xapi_credential_auth_type_schema import XapiCredentialAuthTypeSchema
from rustici_software_cloud_v2.models.xapi_credential_permissions_level_schema import XapiCredentialPermissionsLevelSchema
from rustici_software_cloud_v2.models.xapi_credential_post_schema import XapiCredentialPostSchema
from rustici_software_cloud_v2.models.xapi_credential_put_schema import XapiCredentialPutSchema
from rustici_software_cloud_v2.models.xapi_credential_schema import XapiCredentialSchema
from rustici_software_cloud_v2.models.xapi_credentials_list_schema import XapiCredentialsListSchema
from rustici_software_cloud_v2.models.xapi_endpoint_schema import XapiEndpointSchema
from rustici_software_cloud_v2.models.xapi_interaction_component import XapiInteractionComponent
from rustici_software_cloud_v2.models.xapi_result import XapiResult
from rustici_software_cloud_v2.models.xapi_score import XapiScore
from rustici_software_cloud_v2.models.xapi_statement import XapiStatement
from rustici_software_cloud_v2.models.xapi_statement_pipe_list_schema import XapiStatementPipeListSchema
from rustici_software_cloud_v2.models.xapi_statement_pipe_post_schema import XapiStatementPipePostSchema
from rustici_software_cloud_v2.models.xapi_statement_pipe_put_schema import XapiStatementPipePutSchema
from rustici_software_cloud_v2.models.xapi_statement_pipe_schema import XapiStatementPipeSchema
from rustici_software_cloud_v2.models.xapi_statement_reference import XapiStatementReference
from rustici_software_cloud_v2.models.xapi_statement_result import XapiStatementResult
from rustici_software_cloud_v2.models.xapi_verb import XapiVerb
from rustici_software_cloud_v2.models.zoomi_company_id import ZoomiCompanyId
from rustici_software_cloud_v2.models.zoomi_course_options_schema import ZoomiCourseOptionsSchema
