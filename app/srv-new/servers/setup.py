from setuptools import setup, Extension

try:
    from Cython.Distutils import build_ext
    cmdclass = { 'build_ext': build_ext }
except ImportError:
    cmdclass = {}


setup(
    name = 'servers',
    version = '0.0.2',
    cmdclass = cmdclass,
    url = 'www.weirdbyte.de',
    author = 'Alexander Rose',
    author_email = 'alexander.rose@weirdbyte.de',
    packages = [
        'static'
    ],
    install_requires = [ 'numpy', 'matplotlib', 'poster', 'fastcluster' ],
    scripts=[
        'static/local.py'
    ]
)