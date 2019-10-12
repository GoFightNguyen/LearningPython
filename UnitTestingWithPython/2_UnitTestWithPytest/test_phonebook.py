import pytest

from phonebook import Phonebook

# @pytest.fixture
# def phonebook(tmpdir):
#     phonebook = Phonebook(tmpdir) 
#     # tmpdir is a temp dir made by pytest
#     # it is removed after each test

@pytest.fixture
def phonebook():
    'Provides an empty Phonebook'
    # the line above is fixture documentation. pytest --fixtures
    phonebook = Phonebook()
    yield phonebook
    phonebook.clear() # anything following yield will be run as a test cleanup

def test_lookup_by_name(phonebook):
    phonebook.add('Bob', '1234')
    assert '1234' == phonebook.lookup('Bob')

def test_lookup_contains_all_names(phonebook):
    phonebook.add('Bob', '1234')
    assert phonebook.names() == {'Bob'}

def test_missing_name_raises_error(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup('Bob')