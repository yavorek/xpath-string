[![Build Status](https://travis-ci.com/yavorek/xpath-string.svg?token=f1xCAxxKbQvFBcvCqY82&branch=master)](https://travis-ci.com/yavorek/xpath_string)


xpath-string
============
Simple module providing operations on Xpath string

Currently only addition of xpath is supported


Xpath Object
------------
* Initialization
    ```python
        from xpath_string.xpath import Xpath

        xpath_object = Xpath('//some[@xpath="string"]')
    ```
* Attributes:\
    ``xpath`` - xpath string (type: 'str')

Xpath Adding
---------------
* Xpath object + string\
    Result of addition string to Xpath object is Xpath object.
    Adding string to Xpath object is the same as adding two strings.
    ```python
    xpath_object = Xpath('//some[@xpath="string"]')
    string = '//div[@class="name"]'
    result = xpath_object + string

    # result == '//some[@xpath="string"]//div[@class="name"]'
    # result.xpath == '//some[@xpath="string"]//div[@class="name"]'
    ```
    Same situation is when Xpath object represents xpath string with OR operator
    ```python
    xpath_object = Xpath('//some[@xpath="string"]|\\span')
    string = '//div[@class="name"]'

    result = xpath_object + string
    # result == '//some[@xpath="string"]|//span//div[@class="name"]'
    # result.xpath == '//some[@xpath="string"]|//span//div[@class="name"]'
    ```

* Xpath object + Xpath object\
    Result of addition Xpath object to Xpath object is Xpath Object.
    ```python
    xpath_object_1 = Xpath('//some[@xpath="string"]')
    xpath_object_2 = Xpath('//div[@class="name"]')

    result = xpath_object_1 + xpath_object_2
    # result == '//some[@xpath="string"]//div[@class="name"]'
    # result.xpath == '//some[@xpath="string"]//div[@class="name"]'
    ```
    When at least one Xpath object has or operator in main part of xpath (not inside square brackets):
    ```python
    xpath_object_1 = Xpath('//some[@xpath="string"]|//span')
    xpath_object_2 = Xpath('//div[@class="name"]')

    result_1 = xpath_object_1 + xpath_object_2
    # result_1 == '//some[@xpath="string"]//div[@class="name"|//span//div[@class="name"]'
    # result_1.xpath == '//some[@xpath="string"]//div[@class="name"|//span//div[@class="name"]'

    result_2 = xpath_object_2 + xpath_object_1
    # result_2 == '//div[@class="name"]//some[@xpath="string"]|//div[@class="name"]//span'
    # result_2.xpath == '//div[@class="name"]//some[@xpath="string"]|//div[@class="name"]//span'
    ```

Running tests
-------------
Install tox (pip install tox)
Then:

    tox

OR install nose (pip install nose)
Then:

    nosetests