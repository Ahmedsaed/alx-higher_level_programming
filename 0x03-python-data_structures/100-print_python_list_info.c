#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - print python list info
 *
 * @p: pointer to a python object
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, i;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
	}
}
