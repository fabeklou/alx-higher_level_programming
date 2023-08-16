#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 *
 * @p: a pointer to the PyObject
 *
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	int list_len, allocation, i;
	const char *element_type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	list_len = var->ob_size;
	allocation = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", allocation);

	for (i = 0; i < list_len; i++)
	{
		element_type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, element_type);

		if (strcmp(element_type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 *
 * @p: a pointer to the PyObject
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, bytes;
	PyBytesObject *bytes_obj = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes_obj->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		bytes = 10;
	else
		bytes = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", bytes);
	for (i = 0; i < bytes; i++)
	{
		printf("%02hhx", bytes_obj->ob_sval[i]);

		if (i == (bytes - 1))
			printf("\n");
		else
			printf(" ");
	}
}
