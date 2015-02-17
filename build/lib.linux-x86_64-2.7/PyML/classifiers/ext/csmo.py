# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info

if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp

        fp = None
        try:
            fp, pathname, description = imp.find_module('_csmo', [dirname(__file__)])
        except ImportError:
            import _csmo

            return _csmo
        if fp is not None:
            try:
                _mod = imp.load_module('_csmo', fp, pathname, description)
            finally:
                fp.close()
            return _mod

    _csmo = swig_import_helper()
    del swig_import_helper
else:
    import _csmo
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method: return method(self, value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method: return method(self)
    raise AttributeError(name)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass

    _newclass = 0


class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")

    __repr__ = _swig_repr
    __swig_destroy__ = _csmo.delete_SwigPyIterator
    __del__ = lambda self: None;

    def value(self): return _csmo.SwigPyIterator_value(self)

    def incr(self, n=1): return _csmo.SwigPyIterator_incr(self, n)

    def decr(self, n=1): return _csmo.SwigPyIterator_decr(self, n)

    def distance(self, *args): return _csmo.SwigPyIterator_distance(self, *args)

    def equal(self, *args): return _csmo.SwigPyIterator_equal(self, *args)

    def copy(self): return _csmo.SwigPyIterator_copy(self)

    def next(self): return _csmo.SwigPyIterator_next(self)

    def __next__(self): return _csmo.SwigPyIterator___next__(self)

    def previous(self): return _csmo.SwigPyIterator_previous(self)

    def advance(self, *args): return _csmo.SwigPyIterator_advance(self, *args)

    def __eq__(self, *args): return _csmo.SwigPyIterator___eq__(self, *args)

    def __ne__(self, *args): return _csmo.SwigPyIterator___ne__(self, *args)

    def __iadd__(self, *args): return _csmo.SwigPyIterator___iadd__(self, *args)

    def __isub__(self, *args): return _csmo.SwigPyIterator___isub__(self, *args)

    def __add__(self, *args): return _csmo.SwigPyIterator___add__(self, *args)

    def __sub__(self, *args): return _csmo.SwigPyIterator___sub__(self, *args)

    def __iter__(self): return self


SwigPyIterator_swigregister = _csmo.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _csmo.IntVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _csmo.IntVector___nonzero__(self)

    def __bool__(self):
        return _csmo.IntVector___bool__(self)

    def __len__(self):
        return _csmo.IntVector___len__(self)

    def pop(self):
        return _csmo.IntVector_pop(self)

    def __getslice__(self, *args):
        return _csmo.IntVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _csmo.IntVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _csmo.IntVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _csmo.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _csmo.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _csmo.IntVector___setitem__(self, *args)

    def append(self, *args):
        return _csmo.IntVector_append(self, *args)

    def empty(self):
        return _csmo.IntVector_empty(self)

    def size(self):
        return _csmo.IntVector_size(self)

    def clear(self):
        return _csmo.IntVector_clear(self)

    def swap(self, *args):
        return _csmo.IntVector_swap(self, *args)

    def get_allocator(self):
        return _csmo.IntVector_get_allocator(self)

    def begin(self):
        return _csmo.IntVector_begin(self)

    def end(self):
        return _csmo.IntVector_end(self)

    def rbegin(self):
        return _csmo.IntVector_rbegin(self)

    def rend(self):
        return _csmo.IntVector_rend(self)

    def pop_back(self):
        return _csmo.IntVector_pop_back(self)

    def erase(self, *args):
        return _csmo.IntVector_erase(self, *args)

    def __init__(self, *args):
        this = _csmo.new_IntVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _csmo.IntVector_push_back(self, *args)

    def front(self):
        return _csmo.IntVector_front(self)

    def back(self):
        return _csmo.IntVector_back(self)

    def assign(self, *args):
        return _csmo.IntVector_assign(self, *args)

    def resize(self, *args):
        return _csmo.IntVector_resize(self, *args)

    def insert(self, *args):
        return _csmo.IntVector_insert(self, *args)

    def reserve(self, *args):
        return _csmo.IntVector_reserve(self, *args)

    def capacity(self):
        return _csmo.IntVector_capacity(self)

    __swig_destroy__ = _csmo.delete_IntVector
    __del__ = lambda self: None;


IntVector_swigregister = _csmo.IntVector_swigregister
IntVector_swigregister(IntVector)


class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _csmo.DoubleVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _csmo.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _csmo.DoubleVector___bool__(self)

    def __len__(self):
        return _csmo.DoubleVector___len__(self)

    def pop(self):
        return _csmo.DoubleVector_pop(self)

    def __getslice__(self, *args):
        return _csmo.DoubleVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _csmo.DoubleVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _csmo.DoubleVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _csmo.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _csmo.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _csmo.DoubleVector___setitem__(self, *args)

    def append(self, *args):
        return _csmo.DoubleVector_append(self, *args)

    def empty(self):
        return _csmo.DoubleVector_empty(self)

    def size(self):
        return _csmo.DoubleVector_size(self)

    def clear(self):
        return _csmo.DoubleVector_clear(self)

    def swap(self, *args):
        return _csmo.DoubleVector_swap(self, *args)

    def get_allocator(self):
        return _csmo.DoubleVector_get_allocator(self)

    def begin(self):
        return _csmo.DoubleVector_begin(self)

    def end(self):
        return _csmo.DoubleVector_end(self)

    def rbegin(self):
        return _csmo.DoubleVector_rbegin(self)

    def rend(self):
        return _csmo.DoubleVector_rend(self)

    def pop_back(self):
        return _csmo.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _csmo.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        this = _csmo.new_DoubleVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _csmo.DoubleVector_push_back(self, *args)

    def front(self):
        return _csmo.DoubleVector_front(self)

    def back(self):
        return _csmo.DoubleVector_back(self)

    def assign(self, *args):
        return _csmo.DoubleVector_assign(self, *args)

    def resize(self, *args):
        return _csmo.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _csmo.DoubleVector_insert(self, *args)

    def reserve(self, *args):
        return _csmo.DoubleVector_reserve(self, *args)

    def capacity(self):
        return _csmo.DoubleVector_capacity(self)

    __swig_destroy__ = _csmo.delete_DoubleVector
    __del__ = lambda self: None;


DoubleVector_swigregister = _csmo.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)


def runSMO(*args):
    return _csmo.runSMO(*args)


runSMO = _csmo.runSMO
# This file is compatible with both classic and new-style classes.


