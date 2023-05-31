#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: A PyObject
 */

void print_python_bytes(PyObject *p)
{
	size_t a, bte;
	char *str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
		return;
	}
	str = ((PyBytesObject *)(p))->ob_sval;
	bte = PyBytes_Size(p);
	printf("  size: %ld\n", bte);
	printf("  trying string: %s\n", str);
	if (bte >= 10)
		bte = 10;
	else
		bte++;
	printf("  first %ld bytes: ", bte);
	a = 0;
	while (a < bte - 1)
	{
		printf("%02hhx ", str[a]);
		a++;
	}
	printf("%02hhx", str[a]);
	printf("\n");
	fflush(stdout);
}

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject
 */
void print_python_list(PyObject *p)
{
	size_t a, al, l;
	const char *tpe;
	PyListObject *point;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
		return;
	}
	point = (PyListObject *)p;
	l = PyList_GET_SIZE(p);
	al = list->allocated;
	printf("[*] Size of the Python List = %ld\n", l);
	printf("[*] Allocated = %li\n", al);
	a = 0;
	while (a < l)
	{
		tpe = (point->ob_item[a])->ob_type->tp_name;
		printf("Element %li: %s\n", a, tpe);
		if (strcmp(tpe, "bytes") == 0)
			print_python_bytes(point->ob_item[a]);
		else if (strcmp(tpe, "float") == 0)
			print_python_float(point->ob_item[a]);
		a++;
	}
	fflush(stdout);
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
