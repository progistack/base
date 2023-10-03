# -*- coding: utf-8 -*-

from odoo import fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    app_ribbon_name = fields.Char('Afficher le ruban', config_parameter='app_ribbon_name')
    app_ribbon_color = fields.Char('Couleur du texte du ruban', config_parameter='app_ribbon_color')
    app_ribbon_background_color = fields.Char('Couleur du ruban', config_parameter='app_ribbon_background_color')
