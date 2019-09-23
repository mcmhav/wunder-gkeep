import os
import gkeepapi


class Keep():

    def __init__(self):
        self._keep = gkeepapi.Keep()
        success = self._keep.login(
            os.environ['USER_MAIL'],
            os.environ['USER_PASS'],
        )

    def find(self):
        glist = self._keep.findLabel(query=os.environ['LIST'])
        glist = self._keep.find(
            labels=[self._keep.findLabel(os.environ['LIST'])])
        glist = self._keep.find(query=os.environ['LIST'])

        print(glist)
        for l in glist:
            print(l)

        print(glist.id)
        print(glist.title)
        print(glist.items)

    def create_list(self):
        glist = self._keep.createList(
            NOTE,
            [
                ('Item 1', False), # Not checked
                ('Item 2', True) # Checked
            ])
        glist.pinned = True
        glist.color = gkeepapi.node.ColorValue.DarkBlue

        # Sync up changes
        self._keep.sync()

    def get(self):
        glist = self._keep.get(os.environ['LIST_ID'])
        print(glist)
        print(glist.title)
        print(glist.items)
        glist.add('Item 2', False)

        self._keep.sync()

    def add_tasks(self, tasks):
        glist = self._keep.get(os.environ['LIST_ID'])
        for gitem in glist.items:
            gitem.delete()
        for task in tasks:
            glist.add(task['title'], False)

        self._keep.sync()
