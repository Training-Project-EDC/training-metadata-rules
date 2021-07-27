from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings
from django.core.management.color import color_style

style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'training_metadata_rules'
    verbose_name = 'TRAINING METADATA RULES'


if settings.APP_NAME == 'training_metadata_rules':
    from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
    from edc_metadata.apps import AppConfig as MetadataAppConfig
    from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
    from edc_visit_tracking.apps import (
        AppConfig as BaseEdcVisitTrackingAppConfig)

    class EdcMetadataAppConfig(MetadataAppConfig):
        reason_field = {'training_subject.subjectvisit': 'reason'}

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'training_subject': ('subject_visit', 'training_subject.subjectvisit')}

    class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        country = 'botswana'
        definitions = {
            '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                                 slots=[100, 100, 100, 100, 100, 100, 100]),
            '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                                 slots=[100, 100, 100, 100, 100])}
