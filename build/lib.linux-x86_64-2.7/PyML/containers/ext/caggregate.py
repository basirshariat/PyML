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
            fp, pathname, description = imp.find_module('_caggregate', [dirname(__file__)])
        except ImportError:
            import _caggregate

            return _caggregate
        if fp is not None:
            try:
                _mod = imp.load_module('_caggregate', fp, pathname, description)
            finally:
                fp.close()
            return _mod

    _caggregate = swig_import_helper()
    del swig_import_helper
else:
    import _caggregate
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
    __swig_destroy__ = _caggregate.delete_SwigPyIterator
    __del__ = lambda self: None;

    def value(self): return _caggregate.SwigPyIterator_value(self)

    def incr(self, n=1): return _caggregate.SwigPyIterator_incr(self, n)

    def decr(self, n=1): return _caggregate.SwigPyIterator_decr(self, n)

    def distance(self, *args): return _caggregate.SwigPyIterator_distance(self, *args)

    def equal(self, *args): return _caggregate.SwigPyIterator_equal(self, *args)

    def copy(self): return _caggregate.SwigPyIterator_copy(self)

    def next(self): return _caggregate.SwigPyIterator_next(self)

    def __next__(self): return _caggregate.SwigPyIterator___next__(self)

    def previous(self): return _caggregate.SwigPyIterator_previous(self)

    def advance(self, *args): return _caggregate.SwigPyIterator_advance(self, *args)

    def __eq__(self, *args): return _caggregate.SwigPyIterator___eq__(self, *args)

    def __ne__(self, *args): return _caggregate.SwigPyIterator___ne__(self, *args)

    def __iadd__(self, *args): return _caggregate.SwigPyIterator___iadd__(self, *args)

    def __isub__(self, *args): return _caggregate.SwigPyIterator___isub__(self, *args)

    def __add__(self, *args): return _caggregate.SwigPyIterator___add__(self, *args)

    def __sub__(self, *args): return _caggregate.SwigPyIterator___sub__(self, *args)

    def __iter__(self): return self


SwigPyIterator_swigregister = _caggregate.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)


class IntVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IntVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IntVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _caggregate.IntVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _caggregate.IntVector___nonzero__(self)

    def __bool__(self):
        return _caggregate.IntVector___bool__(self)

    def __len__(self):
        return _caggregate.IntVector___len__(self)

    def pop(self):
        return _caggregate.IntVector_pop(self)

    def __getslice__(self, *args):
        return _caggregate.IntVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _caggregate.IntVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _caggregate.IntVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _caggregate.IntVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _caggregate.IntVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _caggregate.IntVector___setitem__(self, *args)

    def append(self, *args):
        return _caggregate.IntVector_append(self, *args)

    def empty(self):
        return _caggregate.IntVector_empty(self)

    def size(self):
        return _caggregate.IntVector_size(self)

    def clear(self):
        return _caggregate.IntVector_clear(self)

    def swap(self, *args):
        return _caggregate.IntVector_swap(self, *args)

    def get_allocator(self):
        return _caggregate.IntVector_get_allocator(self)

    def begin(self):
        return _caggregate.IntVector_begin(self)

    def end(self):
        return _caggregate.IntVector_end(self)

    def rbegin(self):
        return _caggregate.IntVector_rbegin(self)

    def rend(self):
        return _caggregate.IntVector_rend(self)

    def pop_back(self):
        return _caggregate.IntVector_pop_back(self)

    def erase(self, *args):
        return _caggregate.IntVector_erase(self, *args)

    def __init__(self, *args):
        this = _caggregate.new_IntVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _caggregate.IntVector_push_back(self, *args)

    def front(self):
        return _caggregate.IntVector_front(self)

    def back(self):
        return _caggregate.IntVector_back(self)

    def assign(self, *args):
        return _caggregate.IntVector_assign(self, *args)

    def resize(self, *args):
        return _caggregate.IntVector_resize(self, *args)

    def insert(self, *args):
        return _caggregate.IntVector_insert(self, *args)

    def reserve(self, *args):
        return _caggregate.IntVector_reserve(self, *args)

    def capacity(self):
        return _caggregate.IntVector_capacity(self)

    __swig_destroy__ = _caggregate.delete_IntVector
    __del__ = lambda self: None;


IntVector_swigregister = _caggregate.IntVector_swigregister
IntVector_swigregister(IntVector)


class DoubleVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DoubleVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DoubleVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _caggregate.DoubleVector_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _caggregate.DoubleVector___nonzero__(self)

    def __bool__(self):
        return _caggregate.DoubleVector___bool__(self)

    def __len__(self):
        return _caggregate.DoubleVector___len__(self)

    def pop(self):
        return _caggregate.DoubleVector_pop(self)

    def __getslice__(self, *args):
        return _caggregate.DoubleVector___getslice__(self, *args)

    def __setslice__(self, *args):
        return _caggregate.DoubleVector___setslice__(self, *args)

    def __delslice__(self, *args):
        return _caggregate.DoubleVector___delslice__(self, *args)

    def __delitem__(self, *args):
        return _caggregate.DoubleVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _caggregate.DoubleVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _caggregate.DoubleVector___setitem__(self, *args)

    def append(self, *args):
        return _caggregate.DoubleVector_append(self, *args)

    def empty(self):
        return _caggregate.DoubleVector_empty(self)

    def size(self):
        return _caggregate.DoubleVector_size(self)

    def clear(self):
        return _caggregate.DoubleVector_clear(self)

    def swap(self, *args):
        return _caggregate.DoubleVector_swap(self, *args)

    def get_allocator(self):
        return _caggregate.DoubleVector_get_allocator(self)

    def begin(self):
        return _caggregate.DoubleVector_begin(self)

    def end(self):
        return _caggregate.DoubleVector_end(self)

    def rbegin(self):
        return _caggregate.DoubleVector_rbegin(self)

    def rend(self):
        return _caggregate.DoubleVector_rend(self)

    def pop_back(self):
        return _caggregate.DoubleVector_pop_back(self)

    def erase(self, *args):
        return _caggregate.DoubleVector_erase(self, *args)

    def __init__(self, *args):
        this = _caggregate.new_DoubleVector(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, *args):
        return _caggregate.DoubleVector_push_back(self, *args)

    def front(self):
        return _caggregate.DoubleVector_front(self)

    def back(self):
        return _caggregate.DoubleVector_back(self)

    def assign(self, *args):
        return _caggregate.DoubleVector_assign(self, *args)

    def resize(self, *args):
        return _caggregate.DoubleVector_resize(self, *args)

    def insert(self, *args):
        return _caggregate.DoubleVector_insert(self, *args)

    def reserve(self, *args):
        return _caggregate.DoubleVector_reserve(self, *args)

    def capacity(self):
        return _caggregate.DoubleVector_capacity(self)

    __swig_destroy__ = _caggregate.delete_DoubleVector
    __del__ = lambda self: None;


DoubleVector_swigregister = _caggregate.DoubleVector_swigregister
DoubleVector_swigregister(DoubleVector)


class DataSet(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, DataSet, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, DataSet, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")

    __repr__ = _swig_repr
    __swig_setmethods__["Y"] = _caggregate.DataSet_Y_set
    __swig_getmethods__["Y"] = _caggregate.DataSet_Y_get
    if _newclass: Y = _swig_property(_caggregate.DataSet_Y_get, _caggregate.DataSet_Y_set)
    __swig_setmethods__["norms"] = _caggregate.DataSet_norms_set
    __swig_getmethods__["norms"] = _caggregate.DataSet_norms_get
    if _newclass: norms = _swig_property(_caggregate.DataSet_norms_get, _caggregate.DataSet_norms_set)
    __swig_setmethods__["kernel"] = _caggregate.DataSet_kernel_set
    __swig_getmethods__["kernel"] = _caggregate.DataSet_kernel_get
    if _newclass: kernel = _swig_property(_caggregate.DataSet_kernel_get, _caggregate.DataSet_kernel_set)

    def setY(self, *args):
        return _caggregate.DataSet_setY(self, *args)

    def computeNorms(self):
        return _caggregate.DataSet_computeNorms(self)

    def setKernel(self, *args):
        return _caggregate.DataSet_setKernel(self, *args)

    def attachKernel(self, *args):
        return _caggregate.DataSet_attachKernel(self, *args)

    def getKernelMatrixAsVector(self):
        return _caggregate.DataSet_getKernelMatrixAsVector(self)

    def size(self):
        return _caggregate.DataSet_size(self)

    def dotProduct(self, *args):
        return _caggregate.DataSet_dotProduct(self, *args)

    def duplicate(self, *args):
        return _caggregate.DataSet_duplicate(self, *args)

    def castToBase(self):
        return _caggregate.DataSet_castToBase(self)

    def show(self):
        return _caggregate.DataSet_show(self)

    __swig_destroy__ = _caggregate.delete_DataSet
    __del__ = lambda self: None;


DataSet_swigregister = _caggregate.DataSet_swigregister
DataSet_swigregister(DataSet)


class Aggregate(DataSet):
    __swig_setmethods__ = {}
    for _s in [DataSet]: __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Aggregate, name, value)
    __swig_getmethods__ = {}
    for _s in [DataSet]: __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Aggregate, name)
    __repr__ = _swig_repr
    __swig_setmethods__["datas"] = _caggregate.Aggregate_datas_set
    __swig_getmethods__["datas"] = _caggregate.Aggregate_datas_get
    if _newclass: datas = _swig_property(_caggregate.Aggregate_datas_get, _caggregate.Aggregate_datas_set)
    __swig_setmethods__["weights"] = _caggregate.Aggregate_weights_set
    __swig_getmethods__["weights"] = _caggregate.Aggregate_weights_get
    if _newclass: weights = _swig_property(_caggregate.Aggregate_weights_get, _caggregate.Aggregate_weights_set)
    __swig_setmethods__["ownData"] = _caggregate.Aggregate_ownData_set
    __swig_getmethods__["ownData"] = _caggregate.Aggregate_ownData_get
    if _newclass: ownData = _swig_property(_caggregate.Aggregate_ownData_get, _caggregate.Aggregate_ownData_set)

    def size(self):
        return _caggregate.Aggregate_size(self)

    def dotProduct(self, *args):
        return _caggregate.Aggregate_dotProduct(self, *args)

    def show(self):
        return _caggregate.Aggregate_show(self)

    def castToBase(self):
        return _caggregate.Aggregate_castToBase(self)

    def duplicate(self, *args):
        return _caggregate.Aggregate_duplicate(self, *args)

    def addDataSet(self, *args):
        return _caggregate.Aggregate_addDataSet(self, *args)

    def __init__(self, *args):
        this = _caggregate.new_Aggregate(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    __swig_destroy__ = _caggregate.delete_Aggregate
    __del__ = lambda self: None;


Aggregate_swigregister = _caggregate.Aggregate_swigregister
Aggregate_swigregister(Aggregate)



