# -*- coding: utf-8 -*-
#
# Выводит экран с текстом лицензии.
#

import os

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from libs.uix.dialogs import dialog


class ShowLicense(Screen):

    _app = ObjectProperty()

    def show_license(self, *args):
        def _show_license(on_language):
            choice_dialog.dismiss()
            path_to_license = '{}/license/license_{}.rst'.format(
                self._app.directory, self._app.data.dict_language[on_language]
            )

            if not os.path.exists(path_to_license):
                dialog(
                    text=self._app.translation._(
                        u'Не найден текст лицензии!'), title=self._app.title
                )
                return

            text_license = open(path_to_license).read()
            self._app.screen.ids.show_license.ids.text_license.text = \
                text_license
            self._app.nav_drawer._toggle()
            previous_screen = self._app.manager.current
            self._app.manager.current = 'show license'
            self._app.screen.ids.action_bar.left_action_items = \
                [['chevron-left', lambda x: self._app.back_screen(
                    previous_screen)]]
            self._app.screen.ids.action_bar.title = \
              self._app.translation._('MIT LICENSE')

        choice_dialog = dialog(
            text=self._app.translation._(u'Ознакомиться с текстом лицензии:'),
            title=self._app.title,
            buttons=[
                [self._app.translation._(u'На русском'),
                 lambda *x: _show_license(
                     self._app.translation._(u'На русском'))],
                [self._app.translation._(u'На английском'),
                 lambda *x: _show_license(
                     self._app.translation._(u'На английском'))]
            ]
        )
