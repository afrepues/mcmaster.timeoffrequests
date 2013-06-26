from zope.interface import Interface
# -*- Additional Imports Here -*-
from zope import schema

from mcmaster.timeoffrequests import timeoffrequestsMessageFactory as _



class IVacationandtimeoffrequest(Interface):
    """Requests for time off for vacation and other reasons."""

    # -*- schema definition goes here -*-
    department = schema.TextLine(
        title=_(u"Department"),
        required=True,
        description=_(u""),
    )
#
    daterange1 = schema.TextLine(
        title=_(u"Date range 1"),
        required=True,
        description=_(u""),
    )
#
    timeoffcategory1 = schema.TextLine(
        title=_(u"Type of time off"),
        required=True,
        description=_(u""),
    )
#
    startdate1 = schema.Date(
        title=_(u"Start date"),
        required=True,
        description=_(u"The first day of your time off."),
    )
#
    timeoff1 = schema.Int(
        title=_(u"Time off"),
        required=True,
        description=_(u"Enter hours if taking the time off in lieu of overtime.

Otherwise enter days."),
    )
#
    enddate1 = schema.Date(
        title=_(u"End date"),
        required=False,
        description=_(u"The last day of your time off."),
    )
#
    notes1 = schema.TextLine(
        title=_(u"Notes"),
        required=False,
        description=_(u"Please add here any relevant information not covered in the fields above. "),
    )
#
    fieldsetend.20130424.1328217162 = schema.TextLine(
        title=_(u"fieldsetend.2013-04-24.1328217162"),
        required=False,
        description=_(u""),
    )
#
    daterange2 = schema.TextLine(
        title=_(u"Date  range 2"),
        required=True,
        description=_(u""),
    )
#
    timeoffcategory2 = schema.TextLine(
        title=_(u"Type of time off"),
        required=False,
        description=_(u""),
    )
#
    startdate2 = schema.Date(
        title=_(u"Start date"),
        required=False,
        description=_(u"The first day of your time off."),
    )
#
    timeoff2 = schema.Int(
        title=_(u"Time off"),
        required=False,
        description=_(u"Enter hours if taking the time off in lieu of overtime.

Otherwise enter days."),
    )
#
    enddate2 = schema.Date(
        title=_(u"End date"),
        required=False,
        description=_(u"The last day of your time off."),
    )
#
    notes2 = schema.TextLine(
        title=_(u"Notes"),
        required=False,
        description=_(u"Please add here any relevant information not covered in the fields above. "),
    )
#
    fieldsetend.20130424.2191480306 = schema.TextLine(
        title=_(u"fieldsetend.2013-04-24.2191480306"),
        required=False,
        description=_(u""),
    )
#
    daterange3 = schema.TextLine(
        title=_(u"Date range 3"),
        required=True,
        description=_(u""),
    )
#
    timeoffcategory3 = schema.TextLine(
        title=_(u"Type of time off"),
        required=False,
        description=_(u""),
    )
#
    startdate3 = schema.Date(
        title=_(u"Start date"),
        required=False,
        description=_(u"The first day of your time off."),
    )
#
    timeoff3 = schema.Int(
        title=_(u"Time off"),
        required=False,
        description=_(u"Enter hours if taking the time off in lieu of overtime.

Otherwise enter days."),
    )
#
    enddate3 = schema.Date(
        title=_(u"End date"),
        required=False,
        description=_(u"The last day of your time off."),
    )
#
    notes3 = schema.TextLine(
        title=_(u"Notes"),
        required=False,
        description=_(u"Please add here any relevant information not covered in the fields above. "),
    )
#
    fieldsetend.20130424.2618407419 = schema.TextLine(
        title=_(u"fieldsetend.2013-04-24.2618407419"),
        required=False,
        description=_(u""),
    )
#
