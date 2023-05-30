#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: A PyObject
 */

void print_python_bytes(PyObject *p)
{
	Py_ssize_t l = 0, a = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	l = PyBytes_Size(p);
	printf("  size: %zd\n", l);
	str = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", str);
	printf("  first %zd bytes:", l < 10 ? l + 1 : 10);
	while (a < l + 1 && a < 10)
	{
		printf(" %02hhx", str[a]);
		a++;
	}
	printf("\n");
}

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t l, al, a;
	const char *point;
	PyListObject *current = (PyListObject *)p;
	PyVarObject *v = (PyVarObject *)p;

	l = v->ob_size;
	al = current->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", l);
	printf("[*] Allocated = %ld\n", al);

	for (a = 0; a < l; a++)
	{
		point = current->ob_item[a]->ob_type->tp_name;
		printf("Element %ld: %s\n", a, point);
		if (strcmp(point, "bytes") == 0)
			print_python_bytes(current->ob_item[a]);
		else if (strcmp(point, "float") == 0)
			print_python_float(current->ob_item[a]);
	}
}

/**
 * print_python_float - gives data of the PyFloatObject
 * @p: A PyObject
 */
void print_python_float(PyObject *p)
{
	double val = 0;
	char *str = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	val = ((PyFloatObject *)p)->ob_fval;
	str = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", str);
}
