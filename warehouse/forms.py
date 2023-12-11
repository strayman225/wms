from collections.abc import Mapping
from typing import Any
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from datetime import datetime

from django.forms.utils import ErrorList
from .models import *

class IncomingForm(ModelForm):
    class Meta:
        model = Transaction
        fields = 'transdate', 'docnumber', 'item', 'qtyIN', 'warehouse', 'company',


class OutgoingForm(ModelForm):
    class Meta:
        model = Transaction
        fields = 'transdate', 'docnumber', 'item', 'qtyout', 'warehouse', 'company',


