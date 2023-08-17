#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - print basic information on python lists
 * @p: pyobject pointer
 *
 * return: void
 */
void print_python_list(PyObject *p)
{
	if (PyList_Check(p))
	{
	Py_ssize_t size = PyList_Size(p);
	PyObject *item;
	Py_ssize_t i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
	item = PyList_GetItem(p, i);
	printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
	}
	else
	{
	fprintf(stderr, "Invalid List Object\n");
	}
}
/**
 * print_python_bytes - print python bytes
 * @p: pyobject pointer
 *
 * return: void
 */
void print_python_bytes(PyObject *p)
{
	if (PyBytes_Check(p))
	{
	Py_ssize_t size = PyBytes_Size(p);
	const char *string = PyBytes_AsString(p);
	Py_ssize_t i;

	printf("[.] bytes object info\n");
	printf("	size: %ld\n", size);
	printf("	trying string: %s\n", string);

	if (size > 10)
	{
	size = 10;
	}
	printf("	first %ld bytes: ", size);
	for (i = 0; i < size; i++)
	{
	printf("%02x", (unsigned char)string[i]);
	if (i < size - 1)
		{
	printf(" ");
	}
	}
	printf("\n");
	}
	else
	{
	fprintf(stderr, "Invalid Bytes Object\n");
	}
}
