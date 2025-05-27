"""
Core OOP Principles

Python implements four fundamental OOP concepts:

1. Encapsulation:

    Bundling data and methods within a class

    Controlling access via private/protected members (convention-based)

    Implementing getters/setters via properties

2. Abstraction:

    Hiding complex implementation details

    Exposing clear interfaces through methods

    Using abstract base classes (ABCs)

3. Inheritance:

    Creating hierarchical relationships

    Method resolution order (MRO) with C3 linearization

    Multiple inheritance support

4. Polymorphism:

    Duck typing principle

    Operator overloading via magic methods

    Interface implementation through ABCs

Python's OOP Implementation

1. Everything is an Object:

    Classes are objects (instances of type)

    Objects have identity, type, and value

    Methods are essentially functions with self

2. Special Methods:

    __init__: Constructor

    __new__: Instance creation

    __str__: String representation

    80+ special methods for operator overloading

3. Class vs Instance:

    Class attributes vs instance attributes

    Method binding (bound/unbound methods)

    Descriptor protocol for attribute access


    

Best Practices

    1. Follow the Single Responsibility Principle

    2. Use composition over inheritance when possible

    3. Prefer properties over direct attribute access

    4. Use abstract base classes for interface definition

    5. Implement __repr__ for debugging and __str__ for display

    6. Document public interfaces with docstrings

    7. Consider dataclasses for simple data containers (Python 3.7+)

Practical Exercises

1. Implement a library management system with:

    Book, Author, and Library classes

    Proper encapsulation and relationships

    Search and checkout functionality

2. Create a geometric calculator with:

    Abstract Shape class

    Concrete implementations (Circle, Rectangle, Triangle)

    Polymorphic area/perimeter calculations

3. Build a custom decorator system that:

    Logs method calls with arguments

    Measures execution time

    Handles exceptions gracefully

4. Develop a plugin architecture using:

    Abstract base classes for plugins

    Dynamic loading of plugin modules

    Version compatibility checking
    
"""