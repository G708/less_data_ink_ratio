from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# with open(path.join(here, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()


def main():
    install_list = ['numpy', 'matplotlib', 'pillow', 'opencv-python']

    setup(name='less_data_ink_ratio',
          version='0.0.1',
          description='Quantify the Data Ink Ratio in your plot.',
        #   long_description=long_description,
        #   long_description_content_type='text/markdown',
          author='Gina Miku Oba',
          author_email='gina-oba@g.ecc.u-tokyo.ac.jp',
          url='https://github.com/G708/less_data_ink_ratio',
          classifiers=[
            'Programming Language :: Python :: 3.10',
            ],
          keywords=['data visualization', 'network', 'plot'],
          packages=find_packages(),
		  license='MIT',
          install_requires=install_list,
          extras_require={'indra': ['indra']},
          tests_require=['nose'],
          include_package_data=True,
        )


if __name__ == '__main__':
    main()