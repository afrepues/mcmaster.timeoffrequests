"""Definition of the Vacationandtimeoffrequest content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from mcmaster.timeoffrequests import timeoffrequestsMessageFactory as _

from mcmaster.timeoffrequests.interfaces import IVacationandtimeoffrequest
from mcmaster.timeoffrequests.config import PROJECTNAME

VacationandtimeoffrequestSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

    atapi.StringField(
        'department',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Department"),
            description=_(u""),
        ),
        required=True,
    ),


    atapi.StringField(
        'daterange1',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Date range 1"),
            description=_(u""),
        ),
        required=True,
        default=_(u"1"),
    ),


    atapi.StringField(
        'timeoffcategory1',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Type of time off"),
            description=_(u""),
        ),
        required=True,
    ),


    atapi.DateTimeField(
        'startdate1',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Start date"),
            description=_(u"The first day of your time off."),
        ),
        required=True,
        default=_(u""),
        validators=('isValidDate'),
    ),


    atapi.IntegerField(
        'timeoff1',
        storage=atapi.AnnotationStorage(),
        widget=atapi.IntegerWidget(
            label=_(u"Time off"),
            description=_(u"Enter hours if taking the time off in lieu of overtime.

Otherwise enter days."),
        ),
        required=True,
        default=_(u""),
        validators=('isInt'),
    ),


    atapi.DateTimeField(
        'enddate1',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"End date"),
            description=_(u"The last day of your time off."),
        ),
        default=_(u""),
        validators=('isValidDate'),
    ),


    atapi.StringField(
        'notes1',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Notes"),
            description=_(u"Please add here any relevant information not covered in the fields above. "),
        ),
    ),


    atapi.StringField(
        'fieldsetend.20130424.1328217162',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"fieldsetend.2013-04-24.1328217162"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'daterange2',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Date  range 2"),
            description=_(u""),
        ),
        required=True,
        default=_(u"1"),
    ),


    atapi.StringField(
        'timeoffcategory2',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Type of time off"),
            description=_(u""),
        ),
    ),


    atapi.DateTimeField(
        'startdate2',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Start date"),
            description=_(u"The first day of your time off."),
        ),
        default=_(u""),
        validators=('isValidDate'),
    ),


    atapi.IntegerField(
        'timeoff2',
        storage=atapi.AnnotationStorage(),
        widget=atapi.IntegerWidget(
            label=_(u"Time off"),
            description=_(u"Enter hours if taking the time off in lieu of overtime.

Otherwise enter days."),
        ),
        default=_(u""),
        validators=('isInt'),
    ),


    atapi.DateTimeField(
        'enddate2',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"End date"),
            description=_(u"The last day of your time off."),
        ),
        default=_(u""),
        validators=('isValidDate'),
    ),


    atapi.StringField(
        'notes2',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Notes"),
            description=_(u"Please add here any relevant information not covered in the fields above. "),
        ),
    ),


    atapi.StringField(
        'fieldsetend.20130424.2191480306',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"fieldsetend.2013-04-24.2191480306"),
            description=_(u""),
        ),
    ),


    atapi.StringField(
        'daterange3',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Date range 3"),
            description=_(u""),
        ),
        required=True,
        default=_(u"1"),
    ),


    atapi.StringField(
        'timeoffcategory3',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Type of time off"),
            description=_(u""),
        ),
    ),


    atapi.DateTimeField(
        'startdate3',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"Start date"),
            description=_(u"The first day of your time off."),
        ),
        default=_(u""),
        validators=('isValidDate'),
    ),


    atapi.IntegerField(
        'timeoff3',
        storage=atapi.AnnotationStorage(),
        widget=atapi.IntegerWidget(
            label=_(u"Time off"),
            description=_(u"Enter hours if taking the time off in lieu of overtime.

Otherwise enter days."),
        ),
        default=_(u""),
        validators=('isInt'),
    ),


    atapi.DateTimeField(
        'enddate3',
        storage=atapi.AnnotationStorage(),
        widget=atapi.CalendarWidget(
            label=_(u"End date"),
            description=_(u"The last day of your time off."),
        ),
        default=_(u""),
        validators=('isValidDate'),
    ),


    atapi.StringField(
        'notes3',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"Notes"),
            description=_(u"Please add here any relevant information not covered in the fields above. "),
        ),
    ),


    atapi.StringField(
        'fieldsetend.20130424.2618407419',
        storage=atapi.AnnotationStorage(),
        widget=atapi.StringWidget(
            label=_(u"fieldsetend.2013-04-24.2618407419"),
            description=_(u""),
        ),
    ),


))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

VacationandtimeoffrequestSchema['title'].storage = atapi.AnnotationStorage()
VacationandtimeoffrequestSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(VacationandtimeoffrequestSchema, moveDiscussion=False)


class Vacationandtimeoffrequest(base.ATCTContent):
    """Requests for time off for vacation and other reasons."""
    implements(IVacationandtimeoffrequest)

    meta_type = "Vacationandtimeoffrequest"
    schema = VacationandtimeoffrequestSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-
    department = atapi.ATFieldProperty('department')

    daterange1 = atapi.ATFieldProperty('daterange1')

    timeoffcategory1 = atapi.ATFieldProperty('timeoffcategory1')

    startdate1 = atapi.ATFieldProperty('startdate1')

    timeoff1 = atapi.ATFieldProperty('timeoff1')

    enddate1 = atapi.ATFieldProperty('enddate1')

    notes1 = atapi.ATFieldProperty('notes1')

    fieldsetend.20130424.1328217162 = atapi.ATFieldProperty('fieldsetend.20130424.1328217162')

    daterange2 = atapi.ATFieldProperty('daterange2')

    timeoffcategory2 = atapi.ATFieldProperty('timeoffcategory2')

    startdate2 = atapi.ATFieldProperty('startdate2')

    timeoff2 = atapi.ATFieldProperty('timeoff2')

    enddate2 = atapi.ATFieldProperty('enddate2')

    notes2 = atapi.ATFieldProperty('notes2')

    fieldsetend.20130424.2191480306 = atapi.ATFieldProperty('fieldsetend.20130424.2191480306')

    daterange3 = atapi.ATFieldProperty('daterange3')

    timeoffcategory3 = atapi.ATFieldProperty('timeoffcategory3')

    startdate3 = atapi.ATFieldProperty('startdate3')

    timeoff3 = atapi.ATFieldProperty('timeoff3')

    enddate3 = atapi.ATFieldProperty('enddate3')

    notes3 = atapi.ATFieldProperty('notes3')

    fieldsetend.20130424.2618407419 = atapi.ATFieldProperty('fieldsetend.20130424.2618407419')


atapi.registerType(Vacationandtimeoffrequest, PROJECTNAME)
