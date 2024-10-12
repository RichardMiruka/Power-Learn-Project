# Python source code is compiled into an intermediate form known as bytecode (.pyc files)
# This bytecode is then executed by the Python virtual machine (PVM) via the Python interpreter and is platform independent.
# The Python virtual machine is the runtime engine of the Python interpreter.
# The Python virtual machine is responsible for interpreting the bytecode and executing the program.
# The Python virtual machine is implemented in CPython as a stack-based virtual machine.
# The Python virtual machine has a stack, a block stack, and a frame stack.
# Bytecode is a low-level representation of the code, designed for efficient execution by the PVM.

# Example of bytecode
import dis
def hello():
    print("Hello World!")

dis.dis(hello)