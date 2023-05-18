#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject list object.
 */

void print_python_list(PyObject *p)
{
	int taille, alloue, a;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	taille = var->ob_size;
	alloue = list->allocated;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", taille);
	printf("[*] Allocated = %d\n", alloue);
	for (a = 0; a < taille; a++)
	{
		type = list->ob_item[a]->ob_type->tp_name;
		printf("Element %d: %s\n", a, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[a]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	unsigned char a, taille;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		taille = 10;
	else
		taille = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %d bytes: ", taille);
	for (a = 0; a < taille; a++)
	{
		printf("%02hhx", bytes->ob_sval[a]);
		if (a == (taille - 1))
			printf("\n");
		else
			printf(" ");
	}
}
