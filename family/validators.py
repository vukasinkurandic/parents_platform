import os
from django.core.exceptions import ValidationError
#from django.core.validators import RegexValidator
#from django.utils.translation import ugettext_lazy as _


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.file.size
    megabyte_limit = 2.0
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
