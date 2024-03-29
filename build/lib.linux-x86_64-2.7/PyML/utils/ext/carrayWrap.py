# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import new

import _carrayWrap


new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method: return method(self, value)
    if (not static) or hasattr(self, name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method: return method(self)
    raise AttributeError, name


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


import types

try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object:
        pass

    _newclass = 0
del types


class PySwigIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PySwigIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PySwigIterator, name)

    def __init__(self): raise AttributeError, "No constructor defined"

    __repr__ = _swig_repr
    __swig_destroy__ = _carrayWrap.delete_PySwigIterator
    __del__ = lambda self: None;

    def value(*args): return _carrayWrap.PySwigIterator_value(*args)

    def incr(*args): return _carrayWrap.PySwigIterator_incr(*args)

    def decr(*args): return _carrayWrap.PySwigIterator_decr(*args)

    def distance(*args): return _carrayWrap.PySwigIterator_distance(*args)

    def equal(*args): return _carrayWrap.PySwigIterator_equal(*args)

    def copy(*args): return _carrayWrap.PySwigIterator_copy(*args)

    def next(*args): return _carrayWrap.PySwigIterator_next(*args)

    def previous(*args): return _carrayWrap.PySwigIterator_previous(*args)

    def advance(*args): return _carrayWrap.PySwigIterator_advance(*args)

    def __eq__(*args): return _carrayWrap.PySwigIterator___eq__(*args)

    def __ne__(*args): return _carrayWrap.PySwigIterator___ne__(*args)

    def __iadd__(*args): return _carrayWrap.PySwigIterator___iadd__(*args)

    def __isub__(*args): return _carrayWrap.PySwigIterator___isub__(*args)

    def __add__(*args): return _carrayWrap.PySwigIterator___add__(*args)

    def __sub__(*args): return _carrayWrap.PySwigIterator___sub__(*args)

    def __iter__(self): return self


PySwigIterator_swigregister = _carrayWrap.PySwigIterator_swigregister
PySwigIterator_swigregister(PySwigIterator)


class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr

    def iterator(*args):
        return _carrayWrap.IntVector_iterator(*args)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(*args):
        return _carrayWrap.IntVector___nonzero__(*args)

    def __len__(*args):
        return _carrayWrap.IntVector___len__(*args)

    def pop(*args):
        return _carrayWrap.IntVector_pop(*args)

    def __getslice__(*args):
        return _carrayWrap.IntVector___getslice__(*args)

    def __setslice__(*args):
        return _carrayWrap.IntVector___setslice__(*args)

    def __delslice__(*args):
        return _carrayWrap.IntVector___delslice__(*args)

    def __delitem__(*args):
        return _carrayWrap.IntVector___delitem__(*args)

    def __getitem__(*args):
        return _carrayWrap.IntVector___getitem__(*args)

    def __setitem__(*args):
        return _carrayWrap.IntVector___setitem__(*args)

    def append(*args):
        return _carrayWrap.IntVector_append(*args)

    def empty(*args):
        return _carrayWrap.IntVector_empty(*args)

    def size(*args):
        return _carrayWrap.IntVector_size(*args)

    def clear(*args):
        return _carrayWrap.IntVector_clear(*args)

    def swap(*args):
        return _carrayWrap.IntVector_swap(*args)

    def get_allocator(*args):
        return _carrayWrap.IntVector_get_allocator(*args)

    def begin(*args):
        return _carrayWrap.IntVector_begin(*args)

    def end(*args):
        return _carrayWrap.IntVector_end(*args)

    def rbegin(*args):
        return _carrayWrap.IntVector_rbegin(*args)

    def rend(*args):
        return _carrayWrap.IntVector_rend(*args)

    def pop_back(*args):
        return _carrayWrap.IntVector_pop_back(*args)

    def erase(*args):
        return _carrayWrap.IntVector_erase(*args)

    def __init__(self, *args):
        this = _carrayWrap.new_IntVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(*args):
        return _carrayWrap.IntVector_push_back(*args)

    def front(*args):
        return _carrayWrap.IntVector_front(*args)

    def back(*args):
        return _carrayWrap.IntVector_back(*args)

    def assign(*args):
        return _carrayWrap.IntVector_assign(*args)

    def resize(*args):
        return _carrayWrap.IntVector_resize(*args)

    def insert(*args):
        return _carrayWrap.IntVector_insert(*args)

    def reserve(*args):
        return _carrayWrap.IntVector_reserve(*args)

    def capacity(*args):
        return _carrayWrap.IntVector_capacity(*args)

    __swig_destroy__ = _carrayWrap.delete_IntVector
    __del__ = lambda self: None;


IntVector_swigregister = _carrayWrap.IntVector_swigregister
IntVector_swigregister(IntVector)


class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr

    def iterator(*args):
        return _carrayWrap.DoubleVector_iterator(*args)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(*args):
        return _carrayWrap.DoubleVector___nonzero__(*args)

    def __len__(*args):
        return _carrayWrap.DoubleVector___len__(*args)

    def pop(*args):
        return _carrayWrap.DoubleVector_pop(*args)

    def __getslice__(*args):
        return _carrayWrap.DoubleVector___getslice__(*args)

    def __setslice__(*args):
        return _carrayWrap.DoubleVector___setslice__(*args)

    def __delslice__(*args):
        return _carrayWrap.DoubleVector___delslice__(*args)

    def __delitem__(*args):
        return _carrayWrap.DoubleVector___delitem__(*args)

    def __getitem__(*args):
        return _carrayWrap.DoubleVector___getitem__(*args)

    def __setitem__(*args):
        return _carrayWrap.DoubleVector___setitem__(*args)

    def append(*args):
        return _carrayWrap.DoubleVector_append(*args)

    def empty(*args):
        return _carrayWrap.DoubleVector_empty(*args)

    def size(*args):
        return _carrayWrap.DoubleVector_size(*args)

    def clear(*args):
        return _carrayWrap.DoubleVector_clear(*args)

    def swap(*args):
        return _carrayWrap.DoubleVector_swap(*args)

    def get_allocator(*args):
        return _carrayWrap.DoubleVector_get_allocator(*args)

    def begin(*args):
        return _carrayWrap.DoubleVector_begin(*args)

    def end(*args):
        return _carrayWrap.DoubleVector_end(*args)

    def rbegin(*args):
        return _carrayWrap.DoubleVector_rbegin(*args)

    def rend(*args):
        return _carrayWrap.DoubleVector_rend(*args)

    def pop_back(*args):
        return _carrayWrap.DoubleVector_pop_back(*args)

    def erase(*args):
        return _carrayWrap.DoubleVector_erase(*args)

    def __init__(self, *args):
        this = _carrayWrap.new_DoubleVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(*args):
        return _carrayWrap.DoubleVector_push_back(*args)

    def front(*args):
        return _carrayWrap.DoubleVector_front(*args)

    def back(*args):
        return _carrayWrap.DoubleVector_back(*args)

    def assign(*args):
        return _carrayWrap.DoubleVector_assign(*args)

    def resize(*args):
        return _carrayWrap.DoubleVector_resize(*args)

    def insert(*args):
        return _carrayWrap.DoubleVector_insert(*args)

    def reserve(*args):
        return _carrayWrap.DoubleVector_reserve(*args)

    def capacity(*args):
        return _carrayWrap.DoubleVector_capacity(*args)

    __swig_destroy__ = _carrayWrap.delete_DoubleVector
    __del__ = lambda self: None;


DoubleVector_swigregister = _carrayWrap.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)


class FloatVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, FloatVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, FloatVector, name)
    __repr__ = _swig_repr

    def iterator(*args):
        return _carrayWrap.FloatVector_iterator(*args)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(*args):
        return _carrayWrap.FloatVector___nonzero__(*args)

    def __len__(*args):
        return _carrayWrap.FloatVector___len__(*args)

    def pop(*args):
        return _carrayWrap.FloatVector_pop(*args)

    def __getslice__(*args):
        return _carrayWrap.FloatVector___getslice__(*args)

    def __setslice__(*args):
        return _carrayWrap.FloatVector___setslice__(*args)

    def __delslice__(*args):
        return _carrayWrap.FloatVector___delslice__(*args)

    def __delitem__(*args):
        return _carrayWrap.FloatVector___delitem__(*args)

    def __getitem__(*args):
        return _carrayWrap.FloatVector___getitem__(*args)

    def __setitem__(*args):
        return _carrayWrap.FloatVector___setitem__(*args)

    def append(*args):
        return _carrayWrap.FloatVector_append(*args)

    def empty(*args):
        return _carrayWrap.FloatVector_empty(*args)

    def size(*args):
        return _carrayWrap.FloatVector_size(*args)

    def clear(*args):
        return _carrayWrap.FloatVector_clear(*args)

    def swap(*args):
        return _carrayWrap.FloatVector_swap(*args)

    def get_allocator(*args):
        return _carrayWrap.FloatVector_get_allocator(*args)

    def begin(*args):
        return _carrayWrap.FloatVector_begin(*args)

    def end(*args):
        return _carrayWrap.FloatVector_end(*args)

    def rbegin(*args):
        return _carrayWrap.FloatVector_rbegin(*args)

    def rend(*args):
        return _carrayWrap.FloatVector_rend(*args)

    def pop_back(*args):
        return _carrayWrap.FloatVector_pop_back(*args)

    def erase(*args):
        return _carrayWrap.FloatVector_erase(*args)

    def __init__(self, *args):
        this = _carrayWrap.new_FloatVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(*args):
        return _carrayWrap.FloatVector_push_back(*args)

    def front(*args):
        return _carrayWrap.FloatVector_front(*args)

    def back(*args):
        return _carrayWrap.FloatVector_back(*args)

    def assign(*args):
        return _carrayWrap.FloatVector_assign(*args)

    def resize(*args):
        return _carrayWrap.FloatVector_resize(*args)

    def insert(*args):
        return _carrayWrap.FloatVector_insert(*args)

    def reserve(*args):
        return _carrayWrap.FloatVector_reserve(*args)

    def capacity(*args):
        return _carrayWrap.FloatVector_capacity(*args)

    __swig_destroy__ = _carrayWrap.delete_FloatVector
    __del__ = lambda self: None;


FloatVector_swigregister = _carrayWrap.FloatVector_swigregister
FloatVector_swigregister(FloatVector)


class StringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector, name)
    __repr__ = _swig_repr

    def iterator(*args):
        return _carrayWrap.StringVector_iterator(*args)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(*args):
        return _carrayWrap.StringVector___nonzero__(*args)

    def __len__(*args):
        return _carrayWrap.StringVector___len__(*args)

    def pop(*args):
        return _carrayWrap.StringVector_pop(*args)

    def __getslice__(*args):
        return _carrayWrap.StringVector___getslice__(*args)

    def __setslice__(*args):
        return _carrayWrap.StringVector___setslice__(*args)

    def __delslice__(*args):
        return _carrayWrap.StringVector___delslice__(*args)

    def __delitem__(*args):
        return _carrayWrap.StringVector___delitem__(*args)

    def __getitem__(*args):
        return _carrayWrap.StringVector___getitem__(*args)

    def __setitem__(*args):
        return _carrayWrap.StringVector___setitem__(*args)

    def append(*args):
        return _carrayWrap.StringVector_append(*args)

    def empty(*args):
        return _carrayWrap.StringVector_empty(*args)

    def size(*args):
        return _carrayWrap.StringVector_size(*args)

    def clear(*args):
        return _carrayWrap.StringVector_clear(*args)

    def swap(*args):
        return _carrayWrap.StringVector_swap(*args)

    def get_allocator(*args):
        return _carrayWrap.StringVector_get_allocator(*args)

    def begin(*args):
        return _carrayWrap.StringVector_begin(*args)

    def end(*args):
        return _carrayWrap.StringVector_end(*args)

    def rbegin(*args):
        return _carrayWrap.StringVector_rbegin(*args)

    def rend(*args):
        return _carrayWrap.StringVector_rend(*args)

    def pop_back(*args):
        return _carrayWrap.StringVector_pop_back(*args)

    def erase(*args):
        return _carrayWrap.StringVector_erase(*args)

    def __init__(self, *args):
        this = _carrayWrap.new_StringVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(*args):
        return _carrayWrap.StringVector_push_back(*args)

    def front(*args):
        return _carrayWrap.StringVector_front(*args)

    def back(*args):
        return _carrayWrap.StringVector_back(*args)

    def assign(*args):
        return _carrayWrap.StringVector_assign(*args)

    def resize(*args):
        return _carrayWrap.StringVector_resize(*args)

    def insert(*args):
        return _carrayWrap.StringVector_insert(*args)

    def reserve(*args):
        return _carrayWrap.StringVector_reserve(*args)

    def capacity(*args):
        return _carrayWrap.StringVector_capacity(*args)

    __swig_destroy__ = _carrayWrap.delete_StringVector
    __del__ = lambda self: None;


StringVector_swigregister = _carrayWrap.StringVector_swigregister
StringVector_swigregister(StringVector)


class LongVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LongVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LongVector, name)
    __repr__ = _swig_repr

    def iterator(*args):
        return _carrayWrap.LongVector_iterator(*args)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(*args):
        return _carrayWrap.LongVector___nonzero__(*args)

    def __len__(*args):
        return _carrayWrap.LongVector___len__(*args)

    def pop(*args):
        return _carrayWrap.LongVector_pop(*args)

    def __getslice__(*args):
        return _carrayWrap.LongVector___getslice__(*args)

    def __setslice__(*args):
        return _carrayWrap.LongVector___setslice__(*args)

    def __delslice__(*args):
        return _carrayWrap.LongVector___delslice__(*args)

    def __delitem__(*args):
        return _carrayWrap.LongVector___delitem__(*args)

    def __getitem__(*args):
        return _carrayWrap.LongVector___getitem__(*args)

    def __setitem__(*args):
        return _carrayWrap.LongVector___setitem__(*args)

    def append(*args):
        return _carrayWrap.LongVector_append(*args)

    def empty(*args):
        return _carrayWrap.LongVector_empty(*args)

    def size(*args):
        return _carrayWrap.LongVector_size(*args)

    def clear(*args):
        return _carrayWrap.LongVector_clear(*args)

    def swap(*args):
        return _carrayWrap.LongVector_swap(*args)

    def get_allocator(*args):
        return _carrayWrap.LongVector_get_allocator(*args)

    def begin(*args):
        return _carrayWrap.LongVector_begin(*args)

    def end(*args):
        return _carrayWrap.LongVector_end(*args)

    def rbegin(*args):
        return _carrayWrap.LongVector_rbegin(*args)

    def rend(*args):
        return _carrayWrap.LongVector_rend(*args)

    def pop_back(*args):
        return _carrayWrap.LongVector_pop_back(*args)

    def erase(*args):
        return _carrayWrap.LongVector_erase(*args)

    def __init__(self, *args):
        this = _carrayWrap.new_LongVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(*args):
        return _carrayWrap.LongVector_push_back(*args)

    def front(*args):
        return _carrayWrap.LongVector_front(*args)

    def back(*args):
        return _carrayWrap.LongVector_back(*args)

    def assign(*args):
        return _carrayWrap.LongVector_assign(*args)

    def resize(*args):
        return _carrayWrap.LongVector_resize(*args)

    def insert(*args):
        return _carrayWrap.LongVector_insert(*args)

    def reserve(*args):
        return _carrayWrap.LongVector_reserve(*args)

    def capacity(*args):
        return _carrayWrap.LongVector_capacity(*args)

    __swig_destroy__ = _carrayWrap.delete_LongVector
    __del__ = lambda self: None;


LongVector_swigregister = _carrayWrap.LongVector_swigregister
LongVector_swigregister(LongVector)


class intArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, intArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, intArray, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _carrayWrap.new_intArray(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    __swig_destroy__ = _carrayWrap.delete_intArray
    __del__ = lambda self: None;

    def __getitem__(*args):
        return _carrayWrap.intArray___getitem__(*args)

    def __setitem__(*args):
        return _carrayWrap.intArray___setitem__(*args)

    def cast(*args):
        return _carrayWrap.intArray_cast(*args)

    __swig_getmethods__["frompointer"] = lambda x: _carrayWrap.intArray_frompointer
    if _newclass: frompointer = staticmethod(_carrayWrap.intArray_frompointer)


intArray_swigregister = _carrayWrap.intArray_swigregister
intArray_swigregister(intArray)
intArray_frompointer = _carrayWrap.intArray_frompointer


class doubleArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, doubleArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, doubleArray, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _carrayWrap.new_doubleArray(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    __swig_destroy__ = _carrayWrap.delete_doubleArray
    __del__ = lambda self: None;

    def __getitem__(*args):
        return _carrayWrap.doubleArray___getitem__(*args)

    def __setitem__(*args):
        return _carrayWrap.doubleArray___setitem__(*args)

    def cast(*args):
        return _carrayWrap.doubleArray_cast(*args)

    __swig_getmethods__["frompointer"] = lambda x: _carrayWrap.doubleArray_frompointer
    if _newclass: frompointer = staticmethod(_carrayWrap.doubleArray_frompointer)


doubleArray_swigregister = _carrayWrap.doubleArray_swigregister
doubleArray_swigregister(doubleArray)
doubleArray_frompointer = _carrayWrap.doubleArray_frompointer



