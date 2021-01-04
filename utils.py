import time
import sys


def log(*args, **kwargs):
    """
    日志打印函数, 输入任意数据, 将其按特定格式打印出来并保存的根目录的log文件中
    :param args: Any thing you want
    :param kwargs:
    :return: None
    """
    # time.time() 返回 unix time, 并将其转换为如下格式
    time_format = '[%Y/%m/%d--%H:%M:%S]:'
    localtime = time.localtime(int(time.time()))
    formatted = time.strftime(time_format, localtime)

    with open('log.txt', 'a', encoding='utf-8') as f:
        # 时间和log内容分开, 并且加上分隔符号
        print(f'{formatted}', *args)

        # If kwargs is not null, then print them
        if len(kwargs) > 0:
            for k in kwargs.keys():
                print(f'{k}: {kwargs[k]}')

        # 将log的内容写到文件里, 与之前的print分开是为了避免写文件太慢影响print
        print(f'{formatted}', *args, file=f)
        if len(kwargs) > 0:
            for k in kwargs.keys():
                print(f'{k}: {kwargs[k]}', file=f)


def load_str(filename):
    fn = filename
    with open(fn, 'r', encoding='utf-8') as f:
        r = f.read()
    return r


def dump_str(filename, content):
    fn = filename
    c = content
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(c)
    return 0


def percent(x, y):
    p = round(x / y, 2) * 100
    percent = int(p)
    return percent


def progress_bar(x, y, info='0', speed='Null'):
    print("\r", end="")
    print(f"{info} MB Downloading Speed: {speed}K/S {percent(x, y)}: ",
          "▋ " * (percent(x, y) // 5),
          end="")
    sys.stdout.flush()
    time.sleep(0.5)
    if x == y:
        print()


if __name__ == "__main__":
    print('\r>'*20)