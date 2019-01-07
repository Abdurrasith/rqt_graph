from setuptools import setup

package_name = 'rqt_graph'
setup(
    name=package_name,
    version='0.4.10',
    package_dir={'': 'src'},
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name + '/resource', ['resource/RosGraph.ui']),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
        ('lib/' + package_name, ['scripts/rqt_graph'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Dirk Thomas',
    maintainer='Dirk Thomas, Aaron Blasdell',
    maintainer_email='dthomas@osrfoundation.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'rqt_topic provides a GUI plugin for displaying debug information about ROS topics '
        'including publishers, subscribers, publishing rate, and ROS Messages.'
    ),
    license='BSD',
    tests_require=['pytest'],
    scripts=['scripts/rqt_graph'],
)
