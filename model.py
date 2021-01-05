class Video(object):
    def __init__(self, form: dict):
        self.bvid = form.get('bvid')
        self.up = form.get('up')
        self.title = form.get('title')
        self.create = form.get('create')
        self.url = form.get('url')
        self.name = form.get('name', self.title)
        self.downloaded = form.get('downloaded', False)
        self.allow_download = form.get('allow_download', True)

    def __to_dict(self):
        r = dict(
            bvid=self.bvid,
            up=self.up,
            create=self.create,
            title=self.title,
            url=self.url,
            name=self.name,
            downloaded=self.downloaded,
            allow_download=self.allow_download,
        )

        return r

    # def dump_to_csv

    if __name__ == "__main__":
        with open('test.csv', 'a', encoding='utf-8-sig') as f:
            f.write('1')