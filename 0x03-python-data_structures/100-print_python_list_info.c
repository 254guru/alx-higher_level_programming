#include <Python.h>
#include <listobject.h>
#include <object.h>
#define PY_SSIZE_T_CLEAN

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: PyObject pointer
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *object_list = (PyListObject *) p;
	long int list_size = Py_SIZE(p), list_index;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", object_list->allocated);

	for (list_index = 0; list_index < list_size; list_index++)
		printf("Element %ld: %s\n", list_index,
				Py_TYPE(PyList_GetItem(p, list_index))->tp_name);
}
