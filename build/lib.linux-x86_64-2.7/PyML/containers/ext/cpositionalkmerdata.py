# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info

if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp

        fp = None
        try:
            fp, pathname, description = imp.find_module('_cpositionalkmerdata', [dirname(__file__)])
        except ImportError:
            import _cpositionalkmerdata

            return _cpositionalkmerdata
        if fp is not None:
            try:
                _mod = imp.load_module('_cpositionalkmerdata', fp, pathname, description)
            finally:
                fp.close()
            return _mod

    _cpositionalkmerdata = swig_import_helper()
    del swig_import_helper
else:
    import _cpositionalkmerdata
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
    __swig_destroy__ = _cpositionalkmerdata.delete_SwigPyIterator
    __del__ = lambda self: None;

    def value(self): return _cpositionalkmerdata.SwigPyIterator_value(self)

    def incr(self, n=1): return _cpositionalkmerdata.SwigPyIterator_incr(self, n)

    def decr(self, n=1): return _cpositionalkmerdata.SwigPyIterator_decr(self, n)

    def distance(self, *args): return _cpositionalkmerdata.SwigPyIterator_distance(self, *args)

    def equal(self, *args): return _cpositionalkmerdata.SwigPyIterator_equal(self, *args)

    def copy(self): return _cpositionalkmerdata.SwigPyIterator_copy(self)

    def next(self): return _cpositionalkmerdata.SwigPyIterator_next(self)

    def __next__(self): return _cpositionalkmerdata.SwigPyIterator___next__(self)

    def previous(self): return _cpositionalkmerdata.SwigPyIterator_previous(self)

    def advance(self, *args): return _cpositionalkmerdata.SwigPyIterator_advance(self, *args)

    def __eq__(self, *args): return _cpositionalkmerdata.SwigPyIterator___eq__(self, *args)

    def __ne__(self, *args): return _cpositionalkmerdata.SwigPyIterator___ne__(self, *args)

    def __iadd__(self, *args): return _cpositionalkmerdata.SwigPyIterator___iadd__(self, *args)

    def __isub__(self, *args): return _cpositionalkmerdata.SwigPyIterator___isub__(self, *args)

    def __add__(self, *args): return _cpositionalkmerdata.SwigPyIterator___add__(self, *args)

    def __sub__(self, *args): return _cpositionalkmerdata.SwigPyIterator___sub__(self, *args)

    def __iter__(self): return self


SwigPyIterator_swigregister = _cpositionalkmerdata.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _cpositionalkmerdata.IntVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cpositionalkmerdata.IntVector___nonzero__(self)

    def __bool__(self):
        return _cpositionalkmerdata.IntVector___bool__(self)

    def __len__(self):
        return _cpositionalkmerdata.IntVector___len__(self)

    def pop(self):
        return _cpositionalkmerdata.IntVector_pop(self)

    def __getslice__(self, *args):
        return _cpositionalkmerdata.IntVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _cpositionalkmerdata.IntVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _cpositionalkmerdata.IntVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _cpositionalkmerdata.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cpositionalkmerdata.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cpositionalkmerdata.IntVector___setitem__(self, *args)

    def append(self, *args):
        return _cpositionalkmerdata.IntVector_append(self, *args)

    def empty(self):
        return _cpositionalkmerdata.IntVector_empty(self)

    def size(self):
        return _cpositionalkmerdata.IntVector_size(self)

    def clear(self):
        return _cpositionalkmerdata.IntVector_clear(self)

    def swap(self, *args):
        return _cpositionalkmerdata.IntVector_swap(self, *args)

    def get_allocator(self):
        return _cpositionalkmerdata.IntVector_get_allocator(self)

    def begin(self):
        return _cpositionalkmerdata.IntVector_begin(self)

    def end(self):
        return _cpositionalkmerdata.IntVector_end(self)

    def rbegin(self):
        return _cpositionalkmerdata.IntVector_rbegin(self)

    def rend(self):
        return _cpositionalkmerdata.IntVector_rend(self)

    def pop_back(self):
        return _cpositionalkmerdata.IntVector_pop_back(self)

    def erase(self, *args):
        return _cpositionalkmerdata.IntVector_erase(self, *args)

    def __init__(self, *args):
        this = _cpositionalkmerdata.new_IntVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _cpositionalkmerdata.IntVector_push_back(self, *args)

    def front(self):
        return _cpositionalkmerdata.IntVector_front(self)

    def back(self):
        return _cpositionalkmerdata.IntVector_back(self)

    def assign(self, *args):
        return _cpositionalkmerdata.IntVector_assign(self, *args)

    def resize(self, *args):
        return _cpositionalkmerdata.IntVector_resize(self, *args)

    def insert(self, *args):
        return _cpositionalkmerdata.IntVector_insert(self, *args)

    def reserve(self, *args):
        return _cpositionalkmerdata.IntVector_reserve(self, *args)

    def capacity(self):
        return _cpositionalkmerdata.IntVector_capacity(self)

    __swig_destroy__ = _cpositionalkmerdata.delete_IntVector
    __del__ = lambda self: None;


IntVector_swigregister = _cpositionalkmerdata.IntVector_swigregister
IntVector_swigregister(IntVector)


class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _cpositionalkmerdata.DoubleVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cpositionalkmerdata.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _cpositionalkmerdata.DoubleVector___bool__(self)

    def __len__(self):
        return _cpositionalkmerdata.DoubleVector___len__(self)

    def pop(self):
        return _cpositionalkmerdata.DoubleVector_pop(self)

    def __getslice__(self, *args):
        return _cpositionalkmerdata.DoubleVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _cpositionalkmerdata.DoubleVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _cpositionalkmerdata.DoubleVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _cpositionalkmerdata.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cpositionalkmerdata.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cpositionalkmerdata.DoubleVector___setitem__(self, *args)

    def append(self, *args):
        return _cpositionalkmerdata.DoubleVector_append(self, *args)

    def empty(self):
        return _cpositionalkmerdata.DoubleVector_empty(self)

    def size(self):
        return _cpositionalkmerdata.DoubleVector_size(self)

    def clear(self):
        return _cpositionalkmerdata.DoubleVector_clear(self)

    def swap(self, *args):
        return _cpositionalkmerdata.DoubleVector_swap(self, *args)

    def get_allocator(self):
        return _cpositionalkmerdata.DoubleVector_get_allocator(self)

    def begin(self):
        return _cpositionalkmerdata.DoubleVector_begin(self)

    def end(self):
        return _cpositionalkmerdata.DoubleVector_end(self)

    def rbegin(self):
        return _cpositionalkmerdata.DoubleVector_rbegin(self)

    def rend(self):
        return _cpositionalkmerdata.DoubleVector_rend(self)

    def pop_back(self):
        return _cpositionalkmerdata.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _cpositionalkmerdata.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        this = _cpositionalkmerdata.new_DoubleVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _cpositionalkmerdata.DoubleVector_push_back(self, *args)

    def front(self):
        return _cpositionalkmerdata.DoubleVector_front(self)

    def back(self):
        return _cpositionalkmerdata.DoubleVector_back(self)

    def assign(self, *args):
        return _cpositionalkmerdata.DoubleVector_assign(self, *args)

    def resize(self, *args):
        return _cpositionalkmerdata.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _cpositionalkmerdata.DoubleVector_insert(self, *args)

    def reserve(self, *args):
        return _cpositionalkmerdata.DoubleVector_reserve(self, *args)

    def capacity(self):
        return _cpositionalkmerdata.DoubleVector_capacity(self)

    __swig_destroy__ = _cpositionalkmerdata.delete_DoubleVector
    __del__ = lambda self: None;


DoubleVector_swigregister = _cpositionalkmerdata.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)


class StringVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StringVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StringVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _cpositionalkmerdata.StringVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cpositionalkmerdata.StringVector___nonzero__(self)

    def __bool__(self):
        return _cpositionalkmerdata.StringVector___bool__(self)

    def __len__(self):
        return _cpositionalkmerdata.StringVector___len__(self)

    def pop(self):
        return _cpositionalkmerdata.StringVector_pop(self)

    def __getslice__(self, *args):
        return _cpositionalkmerdata.StringVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _cpositionalkmerdata.StringVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _cpositionalkmerdata.StringVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _cpositionalkmerdata.StringVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cpositionalkmerdata.StringVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cpositionalkmerdata.StringVector___setitem__(self, *args)

    def append(self, *args):
        return _cpositionalkmerdata.StringVector_append(self, *args)

    def empty(self):
        return _cpositionalkmerdata.StringVector_empty(self)

    def size(self):
        return _cpositionalkmerdata.StringVector_size(self)

    def clear(self):
        return _cpositionalkmerdata.StringVector_clear(self)

    def swap(self, *args):
        return _cpositionalkmerdata.StringVector_swap(self, *args)

    def get_allocator(self):
        return _cpositionalkmerdata.StringVector_get_allocator(self)

    def begin(self):
        return _cpositionalkmerdata.StringVector_begin(self)

    def end(self):
        return _cpositionalkmerdata.StringVector_end(self)

    def rbegin(self):
        return _cpositionalkmerdata.StringVector_rbegin(self)

    def rend(self):
        return _cpositionalkmerdata.StringVector_rend(self)

    def pop_back(self):
        return _cpositionalkmerdata.StringVector_pop_back(self)

    def erase(self, *args):
        return _cpositionalkmerdata.StringVector_erase(self, *args)

    def __init__(self, *args):
        this = _cpositionalkmerdata.new_StringVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _cpositionalkmerdata.StringVector_push_back(self, *args)

    def front(self):
        return _cpositionalkmerdata.StringVector_front(self)

    def back(self):
        return _cpositionalkmerdata.StringVector_back(self)

    def assign(self, *args):
        return _cpositionalkmerdata.StringVector_assign(self, *args)

    def resize(self, *args):
        return _cpositionalkmerdata.StringVector_resize(self, *args)

    def insert(self, *args):
        return _cpositionalkmerdata.StringVector_insert(self, *args)

    def reserve(self, *args):
        return _cpositionalkmerdata.StringVector_reserve(self, *args)

    def capacity(self):
        return _cpositionalkmerdata.StringVector_capacity(self)

    __swig_destroy__ = _cpositionalkmerdata.delete_StringVector
    __del__ = lambda self: None;


StringVector_swigregister = _cpositionalkmerdata.StringVector_swigregister
StringVector_swigregister(StringVector)


class LongVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, LongVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, LongVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _cpositionalkmerdata.LongVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cpositionalkmerdata.LongVector___nonzero__(self)

    def __bool__(self):
        return _cpositionalkmerdata.LongVector___bool__(self)

    def __len__(self):
        return _cpositionalkmerdata.LongVector___len__(self)

    def pop(self):
        return _cpositionalkmerdata.LongVector_pop(self)

    def __getslice__(self, *args):
        return _cpositionalkmerdata.LongVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _cpositionalkmerdata.LongVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _cpositionalkmerdata.LongVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _cpositionalkmerdata.LongVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cpositionalkmerdata.LongVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cpositionalkmerdata.LongVector___setitem__(self, *args)

    def append(self, *args):
        return _cpositionalkmerdata.LongVector_append(self, *args)

    def empty(self):
        return _cpositionalkmerdata.LongVector_empty(self)

    def size(self):
        return _cpositionalkmerdata.LongVector_size(self)

    def clear(self):
        return _cpositionalkmerdata.LongVector_clear(self)

    def swap(self, *args):
        return _cpositionalkmerdata.LongVector_swap(self, *args)

    def get_allocator(self):
        return _cpositionalkmerdata.LongVector_get_allocator(self)

    def begin(self):
        return _cpositionalkmerdata.LongVector_begin(self)

    def end(self):
        return _cpositionalkmerdata.LongVector_end(self)

    def rbegin(self):
        return _cpositionalkmerdata.LongVector_rbegin(self)

    def rend(self):
        return _cpositionalkmerdata.LongVector_rend(self)

    def pop_back(self):
        return _cpositionalkmerdata.LongVector_pop_back(self)

    def erase(self, *args):
        return _cpositionalkmerdata.LongVector_erase(self, *args)

    def __init__(self, *args):
        this = _cpositionalkmerdata.new_LongVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _cpositionalkmerdata.LongVector_push_back(self, *args)

    def front(self):
        return _cpositionalkmerdata.LongVector_front(self)

    def back(self):
        return _cpositionalkmerdata.LongVector_back(self)

    def assign(self, *args):
        return _cpositionalkmerdata.LongVector_assign(self, *args)

    def resize(self, *args):
        return _cpositionalkmerdata.LongVector_resize(self, *args)

    def insert(self, *args):
        return _cpositionalkmerdata.LongVector_insert(self, *args)

    def reserve(self, *args):
        return _cpositionalkmerdata.LongVector_reserve(self, *args)

    def capacity(self):
        return _cpositionalkmerdata.LongVector_capacity(self)

    __swig_destroy__ = _cpositionalkmerdata.delete_LongVector
    __del__ = lambda self: None;


LongVector_swigregister = _cpositionalkmerdata.LongVector_swigregister
LongVector_swigregister(LongVector)


class DataSet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DataSet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DataSet, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")

    __repr__ = _swig_repr
    __swig_setmethods__["Y"] = _cpositionalkmerdata.DataSet_Y_set
    __swig_getmethods__["Y"] = _cpositionalkmerdata.DataSet_Y_get
    if _newclass: Y = _swig_property(_cpositionalkmerdata.DataSet_Y_get, _cpositionalkmerdata.DataSet_Y_set)
    __swig_setmethods__["norms"] = _cpositionalkmerdata.DataSet_norms_set
    __swig_getmethods__["norms"] = _cpositionalkmerdata.DataSet_norms_get
    if _newclass: norms = _swig_property(_cpositionalkmerdata.DataSet_norms_get, _cpositionalkmerdata.DataSet_norms_set)
    __swig_setmethods__["kernel"] = _cpositionalkmerdata.DataSet_kernel_set
    __swig_getmethods__["kernel"] = _cpositionalkmerdata.DataSet_kernel_get
    if _newclass: kernel = _swig_property(_cpositionalkmerdata.DataSet_kernel_get,
                                          _cpositionalkmerdata.DataSet_kernel_set)

    def setY(self, *args):
        return _cpositionalkmerdata.DataSet_setY(self, *args)

    def computeNorms(self):
        return _cpositionalkmerdata.DataSet_computeNorms(self)

    def setKernel(self, *args):
        return _cpositionalkmerdata.DataSet_setKernel(self, *args)

    def attachKernel(self, *args):
        return _cpositionalkmerdata.DataSet_attachKernel(self, *args)

    def getKernelMatrixAsVector(self):
        return _cpositionalkmerdata.DataSet_getKernelMatrixAsVector(self)

    def size(self):
        return _cpositionalkmerdata.DataSet_size(self)

    def dotProduct(self, *args):
        return _cpositionalkmerdata.DataSet_dotProduct(self, *args)

    def duplicate(self, *args):
        return _cpositionalkmerdata.DataSet_duplicate(self, *args)

    def castToBase(self):
        return _cpositionalkmerdata.DataSet_castToBase(self)

    def show(self):
        return _cpositionalkmerdata.DataSet_show(self)

    __swig_destroy__ = _cpositionalkmerdata.delete_DataSet
    __del__ = lambda self: None;


DataSet_swigregister = _cpositionalkmerdata.DataSet_swigregister
DataSet_swigregister(DataSet)


class PositionalKmerData(DataSet):
    __swig_setmethods__ = {}
    for _s in [DataSet]: __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PositionalKmerData, name, value)
    __swig_getmethods__ = {}
    for _s in [DataSet]: __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PositionalKmerData, name)
    __repr__ = _swig_repr
    __swig_setmethods__["X"] = _cpositionalkmerdata.PositionalKmerData_X_set
    __swig_getmethods__["X"] = _cpositionalkmerdata.PositionalKmerData_X_get
    if _newclass: X = _swig_property(_cpositionalkmerdata.PositionalKmerData_X_get,
                                     _cpositionalkmerdata.PositionalKmerData_X_set)

    def __init__(self, *args):
        this = _cpositionalkmerdata.new_PositionalKmerData(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    __swig_destroy__ = _cpositionalkmerdata.delete_PositionalKmerData
    __del__ = lambda self: None;

    def addPattern(self, *args):
        return _cpositionalkmerdata.PositionalKmerData_addPattern(self, *args)

    def getSequence(self, *args):
        return _cpositionalkmerdata.PositionalKmerData_getSequence(self, *args)

    def size(self):
        return _cpositionalkmerdata.PositionalKmerData_size(self)

    def castToBase(self):
        return _cpositionalkmerdata.PositionalKmerData_castToBase(self)

    def show(self):
        return _cpositionalkmerdata.PositionalKmerData_show(self)

    def duplicate(self, *args):
        return _cpositionalkmerdata.PositionalKmerData_duplicate(self, *args)

    def dotProduct(self, *args):
        return _cpositionalkmerdata.PositionalKmerData_dotProduct(self, *args)

    __swig_setmethods__["mink"] = _cpositionalkmerdata.PositionalKmerData_mink_set
    __swig_getmethods__["mink"] = _cpositionalkmerdata.PositionalKmerData_mink_get
    if _newclass: mink = _swig_property(_cpositionalkmerdata.PositionalKmerData_mink_get,
                                        _cpositionalkmerdata.PositionalKmerData_mink_set)
    __swig_setmethods__["maxk"] = _cpositionalkmerdata.PositionalKmerData_maxk_set
    __swig_getmethods__["maxk"] = _cpositionalkmerdata.PositionalKmerData_maxk_get
    if _newclass: maxk = _swig_property(_cpositionalkmerdata.PositionalKmerData_maxk_get,
                                        _cpositionalkmerdata.PositionalKmerData_maxk_set)
    __swig_setmethods__["maxShift"] = _cpositionalkmerdata.PositionalKmerData_maxShift_set
    __swig_getmethods__["maxShift"] = _cpositionalkmerdata.PositionalKmerData_maxShift_get
    if _newclass: maxShift = _swig_property(_cpositionalkmerdata.PositionalKmerData_maxShift_get,
                                            _cpositionalkmerdata.PositionalKmerData_maxShift_set)
    __swig_setmethods__["noShiftStart"] = _cpositionalkmerdata.PositionalKmerData_noShiftStart_set
    __swig_getmethods__["noShiftStart"] = _cpositionalkmerdata.PositionalKmerData_noShiftStart_get
    if _newclass: noShiftStart = _swig_property(_cpositionalkmerdata.PositionalKmerData_noShiftStart_get,
                                                _cpositionalkmerdata.PositionalKmerData_noShiftStart_set)
    __swig_setmethods__["noShiftEnd"] = _cpositionalkmerdata.PositionalKmerData_noShiftEnd_set
    __swig_getmethods__["noShiftEnd"] = _cpositionalkmerdata.PositionalKmerData_noShiftEnd_get
    if _newclass: noShiftEnd = _swig_property(_cpositionalkmerdata.PositionalKmerData_noShiftEnd_get,
                                              _cpositionalkmerdata.PositionalKmerData_noShiftEnd_set)
    __swig_setmethods__["mismatches"] = _cpositionalkmerdata.PositionalKmerData_mismatches_set
    __swig_getmethods__["mismatches"] = _cpositionalkmerdata.PositionalKmerData_mismatches_get
    if _newclass: mismatches = _swig_property(_cpositionalkmerdata.PositionalKmerData_mismatches_get,
                                              _cpositionalkmerdata.PositionalKmerData_mismatches_set)
    __swig_setmethods__["mismatchProfile"] = _cpositionalkmerdata.PositionalKmerData_mismatchProfile_set
    __swig_getmethods__["mismatchProfile"] = _cpositionalkmerdata.PositionalKmerData_mismatchProfile_get
    if _newclass: mismatchProfile = _swig_property(_cpositionalkmerdata.PositionalKmerData_mismatchProfile_get,
                                                   _cpositionalkmerdata.PositionalKmerData_mismatchProfile_set)
    __swig_setmethods__["shiftWeight"] = _cpositionalkmerdata.PositionalKmerData_shiftWeight_set
    __swig_getmethods__["shiftWeight"] = _cpositionalkmerdata.PositionalKmerData_shiftWeight_get
    if _newclass: shiftWeight = _swig_property(_cpositionalkmerdata.PositionalKmerData_shiftWeight_get,
                                               _cpositionalkmerdata.PositionalKmerData_shiftWeight_set)

    def setMismatchProfile(self, *args):
        return _cpositionalkmerdata.PositionalKmerData_setMismatchProfile(self, *args)

    def setShiftWeight(self, *args):
        return _cpositionalkmerdata.PositionalKmerData_setShiftWeight(self, *args)

    def shiftSize(self, *args):
        return _cpositionalkmerdata.PositionalKmerData_shiftSize(self, *args)


PositionalKmerData_swigregister = _cpositionalkmerdata.PositionalKmerData_swigregister
PositionalKmerData_swigregister(PositionalKmerData)



