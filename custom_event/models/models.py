# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Events(models.Model):
    _name = "event.event"
    _description = "Events"
    _rec_name = "title"

    title = fields.Char("Title")
    location = fields.Char("Location")
    date = fields.Datetime("Date")
