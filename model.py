import json
from os.path import exists
from os import makedirs
from utils import log


def check_folder_and_file_exists(folder, fname):

    if not exists(folder):
        makedirs(folder)

    if not exists(f'{folder}\\{fname}.json'):
        with open(f'{folder}\\{fname}.json', 'w', encoding='utf-8'):
            pass


def load(folder, fname):
    check_folder_and_file_exists(folder, fname)

    with open(f'{folder}\\{fname}.json', 'r', encoding='utf-8') as f:
        try:
            d = json.load(f)
        except json.decoder.JSONDecodeError as e:
            log(f'[ERROR] {e.msg}')
            return None
        else:
            return d


def dump(folder, fname, data):
    check_folder_and_file_exists(folder, fname)

    with open(f'{folder}\\{fname}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f)


class BaseModel(object):
    def __init__(self, up):

        self.up = up
        self.add_up()

    def add_up(self):
        up_list = load('data', 'ups')

        if up_list is None:
            up_list = list()
            log('UP list is not exists')

        up_list.append(self.up)
        dump('data', 'ups', up_list)

    @classmethod
    def all(cls, fname):

        check_folder_and_file_exists('data', fname)

        with open(f'data\\{fname}.json', 'r', encoding='utf-8') as f:

            log(f'Load all data [{cls.__name__}]')
            c = f.read()

            try:
                all_cls = json.loads(c, object_hook=cls)
            except json.decoder.JSONDecodeError as e:
                log(f'[ERROR] {e.msg}')
                log('Return default null list')
                all_cls = []
            else:
                log('Load data successfully')
        return all_cls

    def save(self):
        all_objects = self.all(self.up)

        log('Start save object')
        for o in all_objects:
            if self.__dict__ == o.__dict__:
                return 'NOT UNIQUE'

        with open(f'data\\{self.up}.json', 'w+', encoding='utf-8') as f:

            all_objects.append(self)
            all_objects_dump = [o.__dict__ for o in all_objects]

            json.dump(all_objects_dump, f)
            return 'OK'


class Video(BaseModel):
    def __init__(self, form: dict):
        super(Video, self).__init__(form.get('up'))
        self.upname = form.get('upname')
        self.bvid = form.get('bvid')
        self.title = form.get('title')
        self.create = form.get('create')
        self.url = form.get('url')
        self.name = form.get('name', self.title)
        self.downloaded = form.get('downloaded', False)
        self.allow_download = form.get('allow_download', True)

    # @classmethod
    # def import_to_csv(cls, up):
    #     all_objects = cls.all(up)

    #     with open(f'{up}.csv', 'w', encoding='utf-8-sig') as f:
    #         for obj in all_objects:

    #             for v in obj.__dict__.values():
    #                 line_list = [
    #                     obj.up, obj.upname, obj.title, obj.name,
    #                     obj.create, obj.url, obj.downloaded,
    #                     obj.allow_download
    #                 ]

    #             line = ','.join(line_list) + '\n'
    #             f.write(line)


class test(object):
    def __init__(self, form):
        self.a = form['a']
        self.b = form['b']
        print(f'{self.a}-{self.b}')


if __name__ == "__main__":
    form = dict(
        bvid='test1',
        up='test2',
        title='test3',
        create='test4',
        url='test5',
        name='test6',
        downloaded='test7',
        allow_download='test8',
    )

    a = Video(form)
    msg = a.save()
    log(msg)