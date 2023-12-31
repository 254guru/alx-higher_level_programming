#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <bytesobject.h>
#include <listobject.h>

/**
 * print_python_list - print basic information on python lists
 * @p: pyobject pointer
 *
 * return: void
 */
void print_python_list(PyObject *p)
{
	long int size_of_list = PyList_GET_SIZE(p), list_index;
	PyObject *temp;
	PyListObject *list_object = (PyListObject *) p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size_of_list);
	printf("[*] Allocated = %ld\n", list_object->allocated);

	for (list_index = 0; list_index < size_of_list; list_index++)
	{
		temp = PyList_GET_ITEM(p, list_index);
		printf("Element %ld: %s\n", list_index,
				temp->ob_type->tp_name);
		if (PyBytes_CheckExact(temp))
			print_python_bytes(temp);
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
	long int size_of_bytes, i;

	printf("[.] bytes object info\n");
	if (PyBytes_CheckExact(p))
	{
		size_of_bytes = PyBytes_Size(p);
		printf("  size: %ld\n", size_of_bytes);
		printf("  trying string: %s\n", PyBytes_AsString(p));
		if (size_of_bytes >= 10)
			size_of_bytes = 10;
		else
			size_of_bytes++;
		printf("  first %ld bytes:", size_of_bytes);
		for (i = 0; i < size_of_bytes; i++)
			printf(" %02x", (int) PyBytes_AsString(p)[i] & 0xff);
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

