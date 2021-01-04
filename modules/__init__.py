import os

from utils import log


def dump_to_txt(result: dict):
    """
    Dump format "code+\t+title"
    :param result: dict, generate by data washer
    :return:
    """
    r = result
    data = r['data']
    data: list

    fname = '\\'.join(['data', r['filename']]) + '.txt'

    # if "/data/" not exists then create one
    if not os.path.exists('data\\'):
        os.mkdir('data')

    if not os.path.exists(fname):
        with open(fname, mode='w', encoding='utf-8') as f:
            for d in data:
                f.write(d)
            log('File dumped')
    else:
        log('File has existed, start to check content')
        with open(fname, mode='r', encoding='utf-8') as f:
            old_data = f.readlines()
            log(f'Loaded old data {old_data}')

        with open(fname, mode='a+', encoding='utf-8') as f:
            for d in data:
                if d in old_data:
                    log(f'Find duplicate data [{d.strip()}]')
                else:
                    log('New data, appended')
                    f.write(d)
    return 0


if __name__ == '__main__':
    with open('..\\data\\avvr.txt', mode='a+', encoding='utf-8') as f:
        ls = f.read()
        log(ls)
        for l in ls:
            log(l)
