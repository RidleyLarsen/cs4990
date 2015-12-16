from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView
from .models import Stage, Company, Contact, Campaign, Opportunity, Reminder, Report, CallLog, OpportunityStage


class HomepageView(TemplateView):
    template_name = "base_home.html"

    def get_context_data(self, *args, **kwargs):
        context = super(HomepageView, self).get_context_data(*args, **kwargs)
        return context

class SettingsView(TemplateView):
    template_name = "settings.html"
    

############
# Stage
############

class StageCreateView(CreateView):
    model = Stage
    fields = ()

class StageDetailView(DetailView):
    model = Stage

class StageListView(ListView):
    model = Stage

class StageDeleteView(DeleteView):
    model = Stage

class StageUpdateView(UpdateView):
    model = Stage
    fields = ()

############
# Company
############

class CompanyCreateView(CreateView):
    model = Company
    fields = ()

class CompanyDetailView(DetailView):
    model = Company

class CompanyListView(ListView):
    model = Company

class CompanyDeleteView(DeleteView):
    model = Company

class CompanyUpdateView(UpdateView):
    model = Company
    fields = ()


############
# Contact
############

class ContactCreateView(CreateView):
    model = Contact
    fields = ()

class ContactDetailView(DetailView):
    model = Contact

class ContactListView(ListView):
    model = Contact

class ContactDeleteView(DeleteView):
    model = Contact

class ContactUpdateView(UpdateView):
    model = Contact
    fields = ()

############
# Campaign
############

class CampaignCreateView(CreateView):
    model = Campaign
    fields = ()

class CampaignDetailView(DetailView):
    model = Campaign

class CampaignListView(ListView):
    model = Campaign

class CampaignDeleteView(DeleteView):
    model = Campaign

class CampaignUpdateView(UpdateView):
    model = Campaign
    fields = ()

############
# Opportunity
############

class OpportunityCreateView(CreateView):
    model = Opportunity
    fields = ()

class OpportunityDetailView(DetailView):
    model = Opportunity

class OpportunityListView(ListView):
    model = Opportunity

class OpportunityDeleteView(DeleteView):
    model = Opportunity

class OpportunityUpdateView(UpdateView):
    model = Opportunity
    fields = ()


############
# Reminder
############

class ReminderCreateView(CreateView):
    model = Reminder
    fields = ()

class ReminderDetailView(DetailView):
    model = Reminder

class ReminderListView(ListView):
    model = Reminder

class ReminderDeleteView(DeleteView):
    model = Reminder

class ReminderUpdateView(UpdateView):
    model = Reminder
    fields = ()


############
# Report
############

class ReportCreateView(CreateView):
    model = Report
    fields = ()

class ReportDetailView(DetailView):
    model = Report

class ReportListView(ListView):
    model = Report

class ReportDeleteView(DeleteView):
    model = Report

class ReportUpdateView(UpdateView):
    model = Report
    fields = ()

############
# CallLog
############

class CallLogCreateView(CreateView):
    model = CallLog
    fields = ()

class CallLogDetailView(DetailView):
    model = CallLog

class CallLogListView(ListView):
    model = CallLog

class CallLogDeleteView(DeleteView):
    model = CallLog

class CallLogUpdateView(UpdateView):
    model = CallLog
    fields = ()


############
# OpportunityStage
############

class OpportunityStageCreateView(CreateView):
    model = OpportunityStage
    fields = ()

class OpportunityStageDetailView(DetailView):
    model = OpportunityStage

class OpportunityStageListView(ListView):
    model = OpportunityStage

class OpportunityStageDeleteView(DeleteView):
    model = OpportunityStage

class OpportunityStageUpdateView(UpdateView):
    model = OpportunityStage
    fields = ()




# Stage
# Company
# Contact
# Campaign
# Opportunity
# Reminder
# Report
# CallLog
# OpportunityStage
