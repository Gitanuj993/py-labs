# python script
from docx import Document

doc = Document()
doc.add_heading('Python Dunder Methods Cheat Sheet', 0)

sections = {
    "Object Lifecycle": [
        "__new__", "__init__", "__del__"
    ],
    "String Representation": [
        "__str__", "__repr__", "__format__"
    ],
    "Size & Truthiness": [
        "__len__", "__bool__"
    ],
    "Arithmetic Operators": [
        "__add__", "__sub__", "__mul__", "__truediv__", "__floordiv__", "__mod__", "__pow__",
        "__iadd__", "__isub__", "__imul__", "__itruediv__"
    ],
    "Comparison Operators": [
        "__eq__", "__ne__", "__lt__", "__le__", "__gt__", "__ge__"
    ],
    "Container Methods": [
        "__getitem__", "__setitem__", "__delitem__", "__contains__"
    ],
    "Iteration": [
        "__iter__", "__next__"
    ],
    "Callable Objects": [
        "__call__"
    ],
    "Attribute Access": [
        "__getattr__", "__getattribute__", "__setattr__", "__delattr__"
    ],
    "Context Managers": [
        "__enter__", "__exit__"
    ],
    "Class & Internals": [
        "__class__", "__init_subclass__", "__mro__"
    ],
    "Hashing": [
        "__hash__"
    ],
    "Copying": [
        "__copy__", "__deepcopy__"
    ],
    "Descriptor Protocol": [
        "__get__", "__set__", "__delete__"
    ],
    "Async (Advanced)": [
        "__await__", "__aiter__", "__anext__"
    ]
}

for section, methods in sections.items():
    doc.add_heading(section, level=1)
    for method in methods:
        doc.add_paragraph(method, style='List Bullet')

doc.save("python_dunder_methods.docx")

print("DOCX file created successfully!")