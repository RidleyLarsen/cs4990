"""project9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from project9.crm.views import HomepageView, \
    OpportunityCreateView, OpportunityDetailView, OpportunityDeleteView, OpportunityListView, OpportunityUpdateView, \
    ContactCreateView, ContactDetailView, ContactListView, ContactDeleteView, \
    StageCreateView, StageDetailView, StageListView, StageDeleteView, StageUpdateView, \
    CompanyCreateView, CompanyDetailView, CompanyListView, CompanyDeleteView, CompanyUpdateView, \
    CampaignCreateView, CampaignDetailView, CampaignListView, CampaignDeleteView, CampaignUpdateView, \
    ReminderCreateView, ReminderDetailView, ReminderListView, ReminderDeleteView, ReminderUpdateView, \
    ReportCreateView, ReportDetailView, ReportListView, ReportDeleteView, ReportUpdateView, \
    CallLogCreateView, CallLogDetailView, CallLogListView, CallLogDeleteView, CallLogUpdateView, \
    OpportunityStageCreateView, OpportunityStageDetailView, OpportunityStageListView, OpportunityStageDeleteView, OpportunityStageUpdateView

urlpatterns = [
    url(r'^$', HomepageView.as_view(), name="home"),

    # Opportunity
    url(r'^opportunity/add/$', OpportunityCreateView.as_view(), name="opportunity-create"),
    url(r'^opportunity/(?P<pk>\d+)/$', OpportunityDetailView.as_view(), name="opportunity-detail"),
    url(r'^opportunity/(?P<pk>\d+)/delete/$', OpportunityDeleteView.as_view(), name="opportunity-delete"),
    url(r'^opportunity/list/', OpportunityListView.as_view(), name="opportunity-list"),
    url(r'^opportunity/(?P<pk>\d+)/update/', OpportunityUpdateView.as_view(), name="opportunity-update"),

    # Contact
    url(r'^contact/add/$', ContactCreateView.as_view(), name="contact-create"),
    url(r'^contact/(?P<pk>\d+)/$', ContactDetailView.as_view(), name="contact-detail"),
    url(r'^contact/list/', ContactListView.as_view(), name="contact-list"),
    url(r'^contact/(?P<pk>\d+)/delete/$', ContactDeleteView.as_view(), name="contact-delete"),

    # Stage
    url(r'^stage/add/$', StageCreateView.as_view(), name="stage-create"),
    url(r'^stage/(?P<pk>\d+)/$', StageDetailView.as_view(), name="stage-detail"),
    url(r'^stage/list/', StageListView.as_view(), name="stage-list"),
    url(r'^stage/(?P<pk>\d+)/delete/$', StageDeleteView.as_view(), name="stage-delete"),
    url(r'^stage/(?P<pk>\d+)/update/$', StageUpdateView.as_view(), name="stage-update"),

    # Company
    url(r'^company/add/$', CompanyCreateView.as_view(), name="company-create"),
    url(r'^company/(?P<pk>\d+)/$', CompanyDetailView.as_view(), name="company-detail"),
    url(r'^company/list/', CompanyListView.as_view(), name="company-list"),
    url(r'^company/(?P<pk>\d+)/delete/$', CompanyDeleteView.as_view(), name="company-delete"),
    url(r'^company/(?P<pk>\d+)/update/$', CompanyUpdateView.as_view(), name="company-update"),

    # Campaign
    url(r'^campaign/add/$', CampaignCreateView.as_view(), name="campaign-create"),
    url(r'^campaign/(?P<pk>\d+)/$', CampaignDetailView.as_view(), name="campaign-detail"),
    url(r'^campaign/list/', CampaignListView.as_view(), name="campaign-list"),
    url(r'^campaign/(?P<pk>\d+)/delete/$', CampaignDeleteView.as_view(), name="campaign-delete"),
    url(r'^campaign/(?P<pk>\d+)/update/$', CampaignUpdateView.as_view(), name="campaign-update"),

    # Reminder
    url(r'^reminder/add/$', ReminderCreateView.as_view(), name="reminder-create"),
    url(r'^reminder/(?P<pk>\d+)/$', ReminderDetailView.as_view(), name="reminder-detail"),
    url(r'^reminder/list/', ReminderListView.as_view(), name="reminder-list"),
    url(r'^reminder/(?P<pk>\d+)/delete/$', ReminderDeleteView.as_view(), name="reminder-delete"),
    url(r'^reminder/(?P<pk>\d+)/update/$', ReminderUpdateView.as_view(), name="reminder-update"),

    # Report
    url(r'^report/add/$', ReportCreateView.as_view(), name="report-create"),
    url(r'^report/(?P<pk>\d+)/$', ReportDetailView.as_view(), name="report-detail"),
    url(r'^report/list/', ReportListView.as_view(), name="report-list"),
    url(r'^report/(?P<pk>\d+)/delete/$', ReportDeleteView.as_view(), name="report-delete"),
    url(r'^report/(?P<pk>\d+)/update/$', ReportUpdateView.as_view(), name="report-update"),

    # CallLog
    url(r'^calllog/add/$', CallLogCreateView.as_view(), name="calllog-create"),
    url(r'^calllog/(?P<pk>\d+)/$', CallLogDetailView.as_view(), name="calllog-detail"),
    url(r'^calllog/list/', CallLogListView.as_view(), name="calllog-list"),
    url(r'^calllog/(?P<pk>\d+)/delete/$', CallLogDeleteView.as_view(), name="calllog-delete"),
    url(r'^calllog/(?P<pk>\d+)/update/$', CallLogUpdateView.as_view(), name="calllog-update"),

    # OpportunityStage
    url(r'^opportunitystage/add/$', OpportunityStageCreateView.as_view(), name="opportunitystage-create"),
    url(r'^opportunitystage/(?P<pk>\d+)/$', OpportunityStageDetailView.as_view(), name="opportunitystage-detail"),
    url(r'^opportunitystage/list/', OpportunityStageListView.as_view(), name="opportunitystage-list"),
    url(r'^opportunitystage/(?P<pk>\d+)/delete/$', OpportunityStageDeleteView.as_view(), name="opportunitystage-delete"),
    url(r'^opportunitystage/(?P<pk>\d+)/update/$', OpportunityStageUpdateView.as_view(), name="opportunitystage-update"),

    url(r'^admin/', include(admin.site.urls)),
]
