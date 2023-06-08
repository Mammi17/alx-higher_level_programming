#include <Python.h>
#include <object.h>
#include <unicodeobject.h>


void print_python_string(PyObject *p)
{
    const char *tpe = NULL;
    Py_ssize_t l = 0;
    wchar_t *string = NULL;

    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        tpe = "compact ascii";
    else
        tpe = "compact unicode object";

    string = PyUnicode_AsWideCharString(p, &l);

    printf("  type: %s\n", tpe);
    printf("  length: %ld\n", l);
    printf("  value: %ls\n", string);
}
