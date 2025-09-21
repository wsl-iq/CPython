#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#ifdef _WIN32

int main(int argc, char *argv[])
{
    const char *script = (argc > 1) ? argv[1] : "CPython.py";
#ifdef _WIN32
    _putenv_s("PYTHONOPTIMIZE", "2");
    _putenv_s("PYTHONDONTWRITEBYTECODE", "1");
#else
    setenv("PYTHONOPTIMIZE", "2", 1);
    setenv("PYTHONDONTWRITEBYTECODE", "1", 1);
#endif
    Py_NoSiteFlag = 1;
    Py_IgnoreEnvironmentFlag = 1;
    Py_OptimizeFlag = 2;
    Py_InitializeEx(0);
    PyRun_SimpleString("import sys,os\nf=open(os.devnull,'w')\nsys.stdout=f\nsys.stderr=f\n");
    FILE *fp = fopen(script, "rb");
    if (fp) {
        PyRun_SimpleFile(fp, script);
    }
    Py_FinalizeEx();
    return 0;
}
#else
int main(int argc, char *argv[])
{
    fprintf(stderr, "This program is intended to be run on Windows.\n");
    return 1;
}
#endif
#else
int main(int argc, char *argv[])
{
    fprintf(stderr, "This program is intended to be compiled with a C compiler.\n");
    return 1;
}