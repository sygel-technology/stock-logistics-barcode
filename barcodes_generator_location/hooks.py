# Copyright 2020 Tecnativa - David Vidal
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).


def uninstall_hook(env):
    """Delete barcode rules with generate model `stock.location` as they
    won't be useful anymore"""
    env.cr.execute(
        """
        DELETE FROM barcode_rule
        WHERE generate_model = 'stock.location'
    """
    )
