import sys
import os

from wunder_gkeep.keep import Keep
from wunder_gkeep.wunderlist import Wunderlist


def wunder_to_keep(request=None):
    wunderlist = Wunderlist()
    tasks = wunderlist.get_tasks()

    keep = Keep()
    keep.add_tasks(tasks)


def main(argv):
    import yaml
    with open('.env.yaml', 'r') as stream:
        envs = yaml.safe_load(stream)
        for env in envs:
            os.environ[env] = envs[env]

    wunder_to_keep()


if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0) # pylint: disable=protected-access
