from fw.SQL.SQLBase import SQLBase
from fw.api.profile.api_actions_in_profile import ActionsInProfile
from fw.api.users.api_addresses import ApiAddresses
from fw.api.users.api_departments import ApiDepartments
from fw.api.users.api_organizations import ApiOrganizations
from fw.api.users.api_positions import ApiPositions
from fw.appium_Instance import AppiumInstance
from fw.driverInstance import DriverInstance
from data.group_data import GroupData
from data.settings import Settings
from data.g1_settings import G1Settings

from fw.api.api_base import APIBase
from fw.api.analytical.api_work_load import ApiWorkLoad
from fw.api.comments.api_actions_in_comment import ActionsInComment
from fw.api.data_designer.gandiva_service_template import GandivaServiceTemplate
from fw.api.file_manager.api_actions_in_file_manager_files_list import ActionsFileManagerFilesList
from fw.api.file_manager.api_file_manager_files_background import ApiFileManagerFilesBackground
from fw.api.messenger.api_actions_in_messenger import ActionsInMessenger
from fw.api.notification_email.api_actions_in_notification_email import ActionsInNotificationEmail
from fw.api.service_catalog.api_actions_in_responsibility_groups import ActionsInResponsibilityGroups
from fw.api.service_catalog.api_actions_in_service_catalog import ActionsInServiceCatalog
from fw.api.service_catalog.api_gandiva_services import ApiGandivaServices
from fw.api.service_catalog.responsibility_groups import ResponsibilityGroups
from fw.api.service_catalog.service_catalogs import ServiceCatalogs
from fw.api.tickets.api_actions_in_task import ActionsInTask
from fw.api.tickets.api_request_custom_field_collection.api_actions_in_request_with_custom_field import ActionsInRequestWithCustomField
from fw.api.tickets.api_actions_in_project import ActionsInProject
from fw.api.tickets.api_request_custom_field_collection.api_request_custom_field_collection import ApiRequestCustomFieldCollection
from fw.api.tickets.api_requests_methods.api_actions_in_request import ApiActionsInRequest
from fw.api.tickets.api_requests_methods.api_change_request import ApiChangeRequest
from fw.api.tickets.api_requests_methods.api_clarifications import ApiClarifications
from fw.api.tickets.api_projects import ApiProjects
from fw.api.tickets.api_requests import ApiRequests
from fw.api.tickets.api_task_custom_field_collection.api_actions_in_task_with_custom_field import ActionsInTaskWithCustomField
from fw.api.tickets.api_task_custom_field_collection.api_task_custom_field_collection import ApiTaskCustomFieldCollection
from fw.api.tickets.api_tasks import ApiTasks
from fw.api.tickets.api_nodes import ApiNodes
from fw.api.tickets.api_tickets import ApiTickets
from fw.api.api_service_catalog.api_gandiva_services_for_tickets import ApiGandivaServicesForTickets
from fw.api.connect.token import Token
from fw.api.users.api_users import ApiUsers
from fw.api.messenger.api_messenger import ApiMessenger
from fw.api.comments.api_comments import ApiComments
from fw.api.notification.api_notification import ApiNotification
from fw.api.notification_email.api_notification_email import ApiNotificationEmail
from fw.api.custom_field_dictionary.api_actions_in_custom_field_dictionary import ActionsInCustomFieldDirectory
from fw.api.custom_field_dictionary.api_custom_field_dictionary import ApiCustomFieldDirectory
from fw.api.tickets.api_actions_in_tickets import ActionsInTickets
from fw.fw_base import FWBase
from fw.g1_api.access_sheet.g1_api_access_sheet import G1ApiAccessSheet
from fw.g1_api.access_tree.g1_api_access_tree import G1ApiAccessTree
from fw.g1_api.account.g1_api_account import G1ApiAccount
from fw.g1_api.activity.g1_api_activity import G1ApiActivity
from fw.g1_api.common.g1_api_common import G1ApiCommon
from fw.g1_api.custom_fields.g1_api_custom_fields import G1ApiCustomFields
from fw.g1_api.g1_api_base import G1APIBase
from fw.g1_api.knowledge_base.g1_api_knowledge_base import G1ApiKnowledgeBase
from fw.g1_api.permissions.g1_api_permissions import G1ApiPermissions
from fw.g1_web.tickets.g1_ticket_base import G1TicketsBase
from fw.g1_api.reports.g1_api_reports import G1ApiReports
from fw.g1_api.responsibility_groups.g1_api_responsibility_groups import G1ApiResponsibilityGroups
from fw.g1_api.time_sheet.g1_api_time_sheet import G1ApiTimeSheet
from fw.g1_api.task_user_filters.g1_api_task_user_filters import G1ApiTaskUserFilters
from fw.g1_web.tickets.request.g1_request_base import G1RequestBase
from fw.g1_web.tickets.request.g1_request_edit import G1RequestEdit
from fw.g1_web.tickets.request.g1_request_new import G1RequestNew
from fw.g1_api.tasks.g1_api_actions_task import G1ActionsInTask
from fw.g1_web.g1_any_page import G1AnyPage
from fw.g1_api.g1_requests.g1_api_actions_in_requests import G1ActionsInRequests
from fw.scripts.users_scripts import UsersScripts
from fw.web.account.login import Login
from fw.web.AnyPage import AnyPage
from fw.web.catalogue.others import CustomFieldDictionary
from fw.web.MainPage import MainPage
from fw.web.access_lists.access_list_create import AccessListCreate
from fw.web.access_lists.access_list_id import AccessListId
from fw.web.access_lists_web import AccessListsWEB
from fw.web.activity import Activity
from fw.web.catalogue_web import CatalogueWeb
from fw.web.knowledge_base.knowledge_base_article import KnowledgeBaseArticle
from fw.web.knowledge_base.knowledge_base_create import KnowledgeBaseCreate
from fw.web.knowledge_base.knowledge_base_edit import KnowledgeBaseEdit
from fw.web.messenger.messenger_id import MessengerId
from fw.web.messenger_web import MessengerWeb
from fw.web.project.project_create import ProjectCreate
from fw.web.project.project_id import ProjectId
from fw.web.project_list import ProjectList
from fw.web.tickets.request.request_create import RequestCreate
from fw.web.tickets.request.request_id import RequestId
from fw.web.tickets.task.task_id import TaskId
from fw.web.tickets.task.task_create import TaskCreate
from fw.web.tickets.tickets_base import TicketsBase
from fw.web.tickets_list import TicketsList
from fw.web.web_base import WebBase
from fw.work_with_email import WorkWithEmail
from fw.work_with_time import work_with_time
from fw.api.tickets.api_tickets_filtration.api_tickets_filtration import FiltrationInTickets
from fw.api.knowledge_base.api_knowledge_base import ApiKnowledgeBase
from fw.api.knowledge_base.api_action_in_articles import ActionsInArticles
from fw.api.knowledge_base.api_access import ApiAccess
from fw.api.users.api_groups import ApiGroups
from fw.api.users.api_actions_with_groups import ActionsInGroups
from fw.work_with_file import WorkWithFile
from fw.api.file_manager.api_file_manager_files import ApiFileManagerFiles
from fw.api.file_manager.api_file_manager_files_image import ApiFileManagerFilesImage
from fw.api.file_manager.api_file_manager_files_archive import ApiFileManagerFilesArchive
from fw.api.file_manager.api_file_manager_files_extensions import ApiFileManagerFilesExtensions
from fw.api.file_manager.api_file_manager_files_list import ApiFileManagerFilesList
from fw.api.file_manager.api_actions_in_file_manager_files_extensions import ActionsFileManagerFilesExtensions
from fw.scripts.environment import Environment
from fw.g1_api.connect.g1_api_token import G1ApiToken
from fw.g1_api.work_normative.g1_api_work_normative import G1ApiWorkNormative
from fw.g1_api.g1_requests.g1_api_requests import G1ApiRequests
from fw.g1_api.users.g1_api_users import G1ApiUsers
from fw.g1_api.users.g1_api_users_wrapper import G1ApiUsersWrapper
from fw.g1_api.tasks.g1_api_tasks import G1ApiTasks
from fw.api.users.api_actions_users import ActionsInUsers
from fw.api.users.api_organizations import ApiOrganizations



class ApplicationManager:

    group_data = GroupData()
    settings = Settings()
    g1_settings = G1Settings()

    def __init__(self):
        self.driver_instance = DriverInstance()
        self.appium_instance = AppiumInstance()
        self.sql = SQLBase(self)
        self.fw_base = FWBase(self)
        self.api_base = APIBase(self)
        self.web_base = WebBase(self)
        self.time = work_with_time()
        self.mail = WorkWithEmail()
        self.scripts_users = UsersScripts(self)
        self.scripts_environment = Environment(self)
        self.work_with_file = WorkWithFile()

        self.web_any_page = AnyPage(self)
        self.web_main_page = MainPage(self)
        self.web_login = Login(self)
        self.web_activity = Activity(self)
        self.web_task_create = TaskCreate(self)
        self.web_task_id = TaskId(self)
        self.web_request_create = RequestCreate(self)
        self.web_tickets_list = TicketsList(self)
        self.web_custom_field_dictionary = CustomFieldDictionary(self)
        self.web_catalogue = CatalogueWeb(self)
        self.web_request_id = RequestId(self)
        self.web_project_create = ProjectCreate(self)
        self.web_project_id = ProjectId(self)
        self.web_project_list = ProjectList(self)
        self.web_tickets_base = TicketsBase(self)
        self.web_access_lists = AccessListsWEB(self)
        self.web_access_list_create = AccessListCreate(self)
        self.web_access_list_id = AccessListId(self)
        self.web_messenger_id = MessengerId(self)
        self.web_messenger = MessengerWeb(self)
        self.web_knowledge_base_article = KnowledgeBaseArticle(self)
        self.web_knowledge_base_create = KnowledgeBaseCreate(self)
        self.web_knowledge_base_edit = KnowledgeBaseEdit(self)

        self.api_tasks = ApiTasks(self)
        self.api_token = Token(self)
        self.api_tickets = ApiTickets(self)
        self.api_users = ApiUsers(self)
        self.api_nodes = ApiNodes(self)
        self.api_work_load = ApiWorkLoad(self)
        self.api_responsibility_groups = ResponsibilityGroups(self)
        self.api_service_catalogs = ServiceCatalogs(self)
        self.api_gandiva_services = ApiGandivaServices(self)
        self.api_requests = ApiRequests(self)
        self.api_gandiva_services_for_tickets = ApiGandivaServicesForTickets(self)
        self.api_projects = ApiProjects(self)
        self.api_messenger = ApiMessenger(self)
        self.api_comments = ApiComments(self)
        self.api_gandiva_service_template = GandivaServiceTemplate(self)
        self.api_notification = ApiNotification(self)
        self.api_notification_email = ApiNotificationEmail(self)
        self.api_actions_in_request = ApiActionsInRequest(self)
        self.api_clarifications = ApiClarifications(self)
        self.api_change_request = ApiChangeRequest(self)
        self.api_actions_in_comment = ActionsInComment(self)
        self.api_actions_in_messenger = ActionsInMessenger(self)
        self.api_actions_in_notification_email = ActionsInNotificationEmail(self)
        self.api_actions_in_responsibility_groups = ActionsInResponsibilityGroups(self)
        self.api_actions_in_service_catalog = ActionsInServiceCatalog(self)
        self.api_actions_in_task = ActionsInTask(self)
        self.api_tickets_filtration = FiltrationInTickets(self)
        self.api_file_manager_files_background = ApiFileManagerFilesBackground(self)
        self.api_actions_in_file_manager_files_list = ActionsFileManagerFilesList(self)
        self.api_knowledge_base = ApiKnowledgeBase(self)
        self.api_action_in_article = ActionsInArticles(self)
        self.api_access = ApiAccess(self)
        self.api_groups = ApiGroups(self)
        self.api_actions_in_group = ActionsInGroups(self)
        self.api_request_custom_field_collection = ApiRequestCustomFieldCollection(self)
        self.api_actions_in_request_with_custom_field = ActionsInRequestWithCustomField(self)
        self.api_actions_in_custom_field_dictionary = ActionsInCustomFieldDirectory(self)
        self.api_custom_field_dictionary = ApiCustomFieldDirectory(self)
        self.api_task_custom_field_collection = ApiTaskCustomFieldCollection(self)
        self.api_actions_in_task_with_custom_field = ActionsInTaskWithCustomField(self)
        self.api_actions_in_tickets = ActionsInTickets(self)
        self.api_file_manager_files = ApiFileManagerFiles(self)
        self.api_file_manager_files_image = ApiFileManagerFilesImage(self)
        self.api_file_manager_files_archive = ApiFileManagerFilesArchive(self)
        self.api_file_manager_files_extension = ApiFileManagerFilesExtensions(self)
        self.api_file_manager_files_list = ApiFileManagerFilesList(self)
        self.api_actions_in_file_manager_files_extensions = ActionsFileManagerFilesExtensions(self)
        self.api_actions_in_project = ActionsInProject(self)
        self.api_actions_in_profile = ActionsInProfile(self)
        self.api_departments = ApiDepartments(self)
        self.api_organizations = ApiOrganizations(self)
        self.api_positions = ApiPositions(self)
        self.api_addresses = ApiAddresses(self)
        self.api_actions_users = ActionsInUsers(self)


        self.g1_api_base = G1APIBase(self)
        self.g1_api_token = G1ApiToken(self)
        self.g1_api_requests = G1ApiRequests(self)
        self.g1_api_work_normative = G1ApiWorkNormative(self)
        self.g1_api_access_sheet = G1ApiAccessSheet(self)
        self.g1_api_access_tree = G1ApiAccessTree(self)
        self.g1_api_account = G1ApiAccount(self)
        self.g1_api_acctivity = G1ApiActivity(self)
        self.g1_api_common = G1ApiCommon(self)
        self.g1_api_users = G1ApiUsers(self)
        self.g1_api_users_wrapper = G1ApiUsersWrapper(self)
        self.g1_api_actions_in_request = G1ActionsInRequests(self)
        self.g1_api_actions_in_task = G1ActionsInTask(self)
        self.g1_api_tasks = G1ApiTasks(self)
        self.g1_api_permissions = G1ApiPermissions(self)
        self.g1_api_custom_fields = G1ApiCustomFields(self)
        self.g1_api_knowledge_base = G1ApiKnowledgeBase(self)
        self.g1_api_task_user_filters = G1ApiTaskUserFilters(self)


        self.g1_web_request_new = G1RequestNew(self)
        self.g1_web_request_edit = G1RequestEdit(self)
        self.g1_web_ticket_base = G1TicketsBase(self)
        self.g1_web_any_page = G1AnyPage(self)
        self.g1_web_request_base = G1RequestBase(self)
        self.g1_api_time_sheet = G1ApiTimeSheet(self)
        self.g1_api_responsibility_groups = G1ApiResponsibilityGroups(self)
        self.g1_api_reports = G1ApiReports(self)
