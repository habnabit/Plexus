def Settings(**kwargs):
    return {
        'flags': [
            '-pthread',
            '-DNDEBUG',
            '-g',
            '-fwrapv',
            '-02',
            '-Wall',
            '-g',
            '-fstack-protector-strong',
            '-Wformat',
            '-Werror=format-security',
            '-Wdate-time',
            '-D_FORTIFY_SOURCE=2',
            '-fPIC',
            '-I/usr/include/python3.6m',
            '-w',
        ],
    }
