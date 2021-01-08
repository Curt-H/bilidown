import json
from utils import log


class BaseModel(object):
    def __init__(self, up):
        self.up = up

    @classmethod
    def all(cls, fname):
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

        with open('data\\data.json', 'w+', encoding='utf-8') as f:

            all_objects.append(self)
            all_objects_dump = [o.__dict__ for o in all_objects]

            json.dump(all_objects_dump, f)
            return 'OK'


class Video(BaseModel):
    def __init__(self, form: dict):
        super(Video, self).__init__(form.get('up'))
        self.bvid = form.get('bvid')
        self.title = form.get('title')
        self.create = form.get('create')
        self.url = form.get('url')
        self.name = form.get('name', self.title)
        self.downloaded = form.get('downloaded', False)
        self.allow_download = form.get('allow_download', True)

    def __to_csv(self):
        r_list = list(
            self.bvid,
            self.up,
            self.title,
            self.create,
            self.url,
            self.name,
            self.downloaded,
            self.allow_download,
        )

        r = ','.join(r_list)

        return r


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