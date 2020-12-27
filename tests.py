import os
import re
import unittest
from pathlib import Path

TEST_MODULE_PATH = Path(os.path.realpath(__file__)).parent / 'tests'
TEST_MODULE_IMPORT_PATH = 'tests'
SPLITTER = re.compile(r'(\d*)')
WHITELIST = []


class TestableModule:
    def __init__(self, module: str):
        self.prefix = None
        self.number = None
        self.module_path = module
        self.is_numbered = False
        try:
            m = SPLITTER.match(module)
            self.prefix = m.groups()[0]
            self.number = int(m.groups()[1])
            self.is_numbered = True
        except:
            pass

    def matches(self, other):
        if self.is_numbered and other.is_numbered:
            return self.prefix == other.prefix and self.number == other.number
        else:
            return self.module_path == other


class TestableModuleRange:
    def __init__(self, module: str):
        ranges = module.split(':')
        m = SPLITTER.match(ranges[0])
        self.prefix = m.groups()[0]
        self.range_start = int(m.groups()[1])
        m = SPLITTER.match(ranges[1])
        self.range_end = int(m.groups()[1])

    def matches(self, other: TestableModule):
        if other.is_numbered:
            return other.is_numbered \
                   and other.prefix == self.prefix \
                   and self.range_start <= other.number <= self.range_end


def load_all_tests():
    tests = []
    for module in TEST_MODULE_PATH.glob('**/*.py'):
        module = str(module).replace(str(TEST_MODULE_PATH) + '/', '')
        if '__' in module or module.startswith('base'):
            continue

        module = TestableModule(module)
        tests.append(module)
    return tests


def load_tests_to_run():
    all_tests = load_all_tests()
    tests_to_run = [test for test in all_tests]
    return sorted(tests_to_run, key=lambda item: item.module_path)


for test_module in load_tests_to_run():
    test_module = test_module.module_path.replace('.py', '')
    import_path = f'{TEST_MODULE_IMPORT_PATH}.{test_module}'
    import_path = import_path.replace('/', '.')
    exec(f'from {import_path} import *')

if __name__ == '__main__':
    unittest.main(failfast=False, verbosity=3)
