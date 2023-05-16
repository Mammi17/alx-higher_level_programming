#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int taille = PyList_Size(p);
	int a;
	PyListObject *object;
		
	object = (PyListObject *)p;
	printf("[*] Size of the Python List = %li\n", taille);
	printf("[*] Allocated = %li\n", object->allocated);
	a = 0; 
	while (a < taille)
	{
		printf("Element %i: %s\n", a, Py_TYPE(object->ob_item[a])->tp_name);
		a++;
	}
}
