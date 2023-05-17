#include <python.h>
/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject
 */

void print_python_list(PyObject *p)
{
	int taille, alloue, a;
	const char *tpe;
	PyListObject *l;
	PyVarObject *val;

	l = (PyListObject *)p;
	val = (PyVarObject *)p;
	taille = val->ob_size, alloue = l->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", taille);
	printf("[*] Allocated = %d\n", alloue);

	a = 0
	while (a < taille)
	{
		tpe = l->ob_item[a]->ob_type->tp_name;
		printf("Element %d: %s\n", a, tpe);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[a]);
		a++;
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char a, taille;
	PyBytesObject *bte;
	
	bte = (PyBytesObject *)p;
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bte->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		taille = 10;
	else
		taille = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", taille);
	a = 0;
	while (a < taille)
	{
		printf("%02hhx", bytes->ob_sval[a]);
		if (a == (taille - 1))
			printf("\n");
		else
			printf(" ");
	}
}
