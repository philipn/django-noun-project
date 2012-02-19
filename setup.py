from setuptools import setup, find_packages

setup(
    name='django-noun-project',
    version='0.1',
    description='Support for the Noun Project inside Django',
    author='Philip Neustrom',
    author_email='philipn@gmail.com',
    url='http://github.com/philipn/django-noun-project/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['django-classy-tags', 'slumber'],
)
