from django.contrib import admin
from nested_inline.admin import NestedTabularInline, NestedStackedInline, NestedModelAdmin 
from .models import Creditor, Offer, Requirements
from main.models import Contacts

from django.forms import TextInput, ModelForm, Textarea, Select
from suit_ckeditor.widgets import CKEditorWidget

class OfferInline(NestedStackedInline):
    class Meta:
        widgets = {
            'body': CKEditorWidget(editor_options={'startupFocus': True})
        }
    model = Offer
    extra = 1
    fieldsets = [
        (None, {
            'classes': (),
            'fields': ['name', 'body',]
        }),
        ('Statistics', {
            'classes': (),
            'fields': ['amount', 'amount_begin', 'amount_end']}),
        ('Architecture', {
            'classes': (),
            'fields': ['loan_begin', 'loan_end']}),
    ]


# class LoanInline(NestedStackedInline):
#     model = Loanrange
#     extra = 1
#     inlines = [OfferInline]

class ContactsInline(NestedStackedInline):
    model = Contacts
    extra = 1
    # fields = (('contact_value', 'name'))
    fieldsets = (
        (None, {
            'fields': [('value','choice')]
        }),
    )
class CreditorForm(ModelForm):
    class Meta:
        widgets = {
            'name': CKEditorWidget(editor_options={'startupFocus': True})
        }
class CreditorAdmin(NestedModelAdmin):
    inlines = [OfferInline, ContactsInline]


admin.site.register(Creditor, CreditorAdmin)
admin.site.register(Contacts)
admin.site.register(Requirements)
