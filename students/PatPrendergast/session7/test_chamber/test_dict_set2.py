
import py.test
import dict_set2 as ds

def test_pref1():
    assert ds.preferences['name'] == 'Chris'

def test_setmaker():
    assert ds.setmaker(3, 20) == set([0,3,6,9,12,15,18])

def test_keys():
    assert ds.the_keys == [0, 1, 2, 3, 4, 5, 6, 7, 8, 
                            9, 10, 11, 12, 13, 14, 15]

def test_subset():
    s2 = ds.setmaker(2, 20)
    s3 = ds.setmaker(3, 20)
    assert ds.s3.issubset(s2) == False

