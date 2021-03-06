# -*- coding: utf-8 -*-
"""Test echo module."""
#
# (C) Pywikibot team, 2019
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, division, unicode_literals

import pywikibot

from pywikibot.echo import Notification

from tests.aspects import unittest, DefaultDrySiteTestCase


class TestNotification(DefaultDrySiteTestCase):

    """Test cases for Notification class."""

    dry = True

    data = {
        '*': 'html text',
        'agent': {'id': 916245, 'name': 'Xqt'},
        'category': 'emailuser',
        'id': '15977044',
        'section': 'alert',
        'targetpages': [],
        'timestamp': {
            'date': '5 September',
            'mw': '20160905204520',
            'unix': '1473108320',
            'utciso8601': '2016-09-05T20:45:20Z',
            'utcmw': '20160905204520',
            'utcunix': '1473108320'
        },
        'type': 'emailuser',
        'wiki': 'dewiki',
    }

    def test_from_json(self):
        """Test Notification.fromJSON class method and instance attributes."""
        notif = Notification.fromJSON(self.get_site(), self.data)
        self.assertIsInstance(notif, Notification)
        self.assertEqual(notif.site, self.get_site())
        self.assertEqual(notif.id, self.data['id'])
        self.assertEqual(int(notif.id), notif.event_id)
        self.assertEqual(notif.type, self.data['type'])
        self.assertEqual(notif.category, self.data['category'])
        self.assertIsInstance(notif.timestamp, pywikibot.Timestamp)
        self.assertEqual(notif.timestamp.totimestampformat(),
                         self.data['timestamp']['mw'])
        self.assertIsInstance(notif.agent, pywikibot.User)
        self.assertIsNone(notif.page)
        self.assertEqual(notif.agent.title(with_ns=False),
                         self.data['agent']['name'])
        self.assertFalse(notif.read)
        self.assertEqual(notif.content, self.data['*'])
        self.assertIsNone(notif.revid)


if __name__ == '__main__':  # pragma: no cover
    try:
        unittest.main()
    except SystemExit:
        pass
