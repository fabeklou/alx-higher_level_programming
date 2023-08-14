#include "cpy.h"

/**
 * print_python_list_info - prints some basic info about Python lists
 *
 * @p: pointer to PyOject
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, list_len, list_allocated;
	PyObject *item;

	list_len = PyList_Size(p);
	list_allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %zd\n", list_len);
	printf("[*] Allocated = %zd\n", list_allocated);

	for (i = 0; i < list_len; i++)
	{
		printf("Element %zd: ", i);
		item = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
