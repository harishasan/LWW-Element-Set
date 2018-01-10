"""
This file contains tests written for LWWElementSet
"""
from lww_element_set import LWWElementSet

def test_element_exists():
    lww_element_set = LWWElementSet()
    lww_element_set.add('value1', 1)
    assert lww_element_set.contains('value1')

def test_element_do_not_exists():
    lww_element_set = LWWElementSet()
    lww_element_set.add('value1', 1)
    assert not lww_element_set.contains('value2')

def test_element_removed_after_insertion():
    lww_element_set = LWWElementSet()
    lww_element_set.add('value1', 1)
    lww_element_set.remove('value1', 2)
    assert not lww_element_set.contains('value1')

def test_element_added_after_removal():
    lww_element_set = LWWElementSet()
    lww_element_set.remove('value1', 1)
    lww_element_set.add('value1', 2)
    assert lww_element_set.contains('value1')

def test_merge_sets():
    first = LWWElementSet()
    second = LWWElementSet()
    first.add('one', 1)
    second.add('two', 2)
    merged = first.merge(second)
    assert merged.contains('one')
    assert merged.contains('two')

def test_add_bias():
    lww_element_set = LWWElementSet()
    lww_element_set.add('value1', 1)
    lww_element_set.remove('value1', 1)
    assert lww_element_set.contains('value1')

def test_remove_bias():
    lww_element_set = LWWElementSet(bias='remove')
    lww_element_set.add('value1', 1)
    lww_element_set.remove('value1', 1)
    assert not lww_element_set.contains('value1')

def test_merge_sets_with_add_in_second_set_after_remove_from_first():
    first = LWWElementSet()
    second = LWWElementSet()
    first.add('one', 1)
    first.remove('one', 2)
    second.add('one', 3)
    merged = first.merge(second)
    assert merged.contains('one')

def test_merge_sets_with_remove_in_second_set_after_add_in_first():
    first = LWWElementSet()
    second = LWWElementSet()
    first.add('one', 1)
    first.add('one', 2)
    second.remove('one', 3)
    merged = first.merge(second)
    assert not merged.contains('one')

