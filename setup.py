from setuptools import setup

package_name = 'simple_pubsub_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lsc',
    maintainer_email='chulslee20@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'basic_publisher = simple_pubsub_python.basic_publisher:main',
            'basic_subscriber = simple_pubsub_python.basic_subscriber:main',
            'cumstom_msg_publisher = simple_pubsub_python.custom_msg_publisher:main',
            'cumstom_msg_subscriber = simple_pubsub_python.custom_msg_subscriber:main',

        ],
    },
)
