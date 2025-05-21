"""
Tests categorize:
    Functional tests (functions): They determine if the features and functionalities are in line with the expectations
    Non functional tests (performance): Involve metrics such as overall performance and quality of the product
    Maintenance tests: Occur when the system and its operational environment is corrected, changed or extended

The four main levels of testing are:
    1- Unit or component testing: the program tests specific individual components by isolating them
    2- integration testing: combines the unit tests and test the flow of data from one component to another.
        There are different approaches to it such as top down, bottom up and sandwich approaches
    3- system testing: which tests all the software you tested against the set requirements 
        and expectations to ensure completeness. his includes measurements of the location of deployed components 
        such as reliability, performance, security and load balancing. It also measures operability in the 
        working environment such as the platform and the operating system.
    4- acceptance testing: It normally involves alpha, beta and regression testing. One way of approaching 
        this is to give pre-written scenarios to the users.  You use the results for improvements and 
        try to find bugs that were missed earlier.

Test automation backages:
    1- Pytest
    2- Robot
    3- Selenium

----------------------------------------------------------------------------------------

Alternative method
    py.test will look for the keyword test and run the tests over those files and functions automatically.

py.test test_file.py

    When you run pytest for a specific function add     ::    to run a specific function in a given file.

Flags used
    For example, -v is the flag:

python3 -m pytest abc.py -v

Some other flag options are:
    -v for verbose
    -q quiet mode
    -s allows the print statement inside the functions to be executed
    -x is to flag the tests to stop execution after first failure
    -m is used to mark a specific function
    -k is a flag for searching and running tests with a specific keyword
    --tb is to disable the traceback code of errors
    --maxfail n specifies maximum number of test fails allowed

Tips
    - The rule of thumb is that the assert statement looks for a Boolean result. 
        You can use in, not in, is, <, >, other than == to check Boolean values. 

    - You can add multiple assert statements inside a single test function.

Additional reading:

Fixtures
    Fixtures are a type of function that is applied to functions to be tested. 
    These functions must run before that test is executed. 
    The purpose of fixtures is to supply data from multiple sources including URLs and databases 
    to the test before running the test. Fixtures are used in cases where code repeats initialization.

Format:
    @pytest.fixture 

Markers
    Markers are used to 'mark' specific functions to be executed by letting users create special names. 
    There are many built-in markers such as xfail, xpass, skip and so on.

They follow a format such as:
    @pytest.mark.<markername> 

For example:
    @pytest.mark.alpha 
    Running the specific marked test in the command line can be done with the following command:
    pytest -m <markername> -v 
    Which will be as follows for a marker called alpha.
    pytest -m alpha -v 
"""

import module_5
import pytest

def test_add():
    assert module_5.add(4, 5) == 9
    # The rule of thumb is that the assert statement looks for a Boolean result. 
    # You can use in, not in, is, <, >, other than == to check Boolean values. 
    # You can add multiple assert statements inside a single test function.

def test_sub():
    assert module_5.sub(4, 5) == -2

test_add()
test_sub()