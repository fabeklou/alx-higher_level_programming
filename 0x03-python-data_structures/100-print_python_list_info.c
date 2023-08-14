#include "python.h"

/**
 * print_python_list_info - prints some basic info about Python lists
 *
 * @p: pointer to PyOject
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	int i, len = 0;
	PyObject *item;
	PyListObject *clone = (PyListObject *)p;

	len = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", (int)clone->allocated);

	for (i = 0; i < len; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
	}
}
