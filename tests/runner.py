from base import results
import json
import os
import unittest
import xmlrunner

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover(os.getcwd())
    xmlrunner.XMLTestRunner().run(tests)
    print(json.dumps(results, default=lambda o: str(o), sort_keys=True, indent=4))
