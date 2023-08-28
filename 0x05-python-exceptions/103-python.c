#include <stdio.h>
#include <Python.h>
#include <floatObject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 *
 * @p: pointer to PyObject
 *
 * Rteurn: nothing
 */
void print_python_list(PyObject *p)
{
	int idx, list_size, alloc;
	const char *type_of_el;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	list_size = var->ob_size;
	alloc = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", alloc);

	for (idx = 0; idx < list_size; idx++)
	{
		type_of_el = list->ob_item[idx]->ob_type->tp_name;
		printf("Element %d: %s\n", idx, type_of_el);

		if (strcmp(type_of_el, "bytes") == 0)
			print_python_bytes(list->ob_item[idx]);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes objects
 *
 * @p: pointer to PyObject
 *
 * Return: nothing
 */
void print_python_bytes(PyObject *p)
{
	unsigned char idx, max_bytes;
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
		max_bytes = 10;
	else
		max_bytes = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %d bytes: ", max_bytes);

	for (idx = 0; idx < max_bytes; idx++)
	{
		printf("%02hhx", bytes_obj->ob_sval[idx]);

		if (idx == (max_bytes - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - prints some basic info about Python float objects
 *
 * @p: pointer to PyObject
 *
 * Return: nothing
 */
void print_python_float(PyObject *p)
{
	char *buffer;
	double value;
	PyFloatObject *float_obj = (PyFloatObject *)p;

	printf("[.] float object info\n");

	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = float_obj->ob_fval;
	buffer = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
}
