from django.contrib.admin.filters import AllValuesFieldListFilter, RelatedFieldListFilter, ChoicesFieldListFilter

class DropdownFilter(AllValuesFieldListFilter):
    template = 'dropdown_filter.html'

class ChoiceDropdownFilter(ChoicesFieldListFilter):
    template = 'dropdown_filter.html'

class RelatedDropdownFilter(RelatedFieldListFilter):
    template = 'dropdown_filter.html'
