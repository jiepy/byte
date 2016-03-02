def heidong(fn):
    def warp(*args, **kwargs):
        print('start -----')
        fn()
        print('stop -----')

    return warp


@heidong
def do_smt():
    print('run run run')


do_smt()
