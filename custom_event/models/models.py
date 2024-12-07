# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Events(models.Model):
    _name = "event.event"
    _description = "Events"

    title = fields.Char("Title")
    location = fields.Char("Location")
    date = fields.Datetime("Date")
