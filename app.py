# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Abstraction:
    def instantiate(self):
        raise NotImplementedError


class Implementation(Abstraction):
    def instantiate(self):
        self.foo()
        return 'Nafis Sadik'

    def foo(self):
        print('foo')


class Test(Abstraction):
    def bar(self):
        print('bar')

    def instantiate(self):
        self.bar()
        return 'Shaka laka boom boom'


class Consumption:
    def __init__(self, interface: Abstraction):
        self._interface = interface

    def execute(self):
        return self._interface.instantiate()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print(Consumption(Implementation()).execute())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
