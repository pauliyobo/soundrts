from __future__ import unicode_literals
from soundrts import res


# This test should only require the packages.py module.
# Since res.py doesn't use packages.py at the moment, this test fails.

# def test_packages_no_network():
#     def dummy_urlopen(url):
#         class Dummy:
#             def read(self):
#                 return "a\nb\n"
#         return Dummy()
#     def dummy_urlopen_no_network(url):
#         raise IOError
#     import urllib
#     original_urlopen = urllib.urlopen
#     try:
#         urllib.urlopen = dummy_urlopen
#         assert res.package_manager.get_packages_urls() == ["a", "b"]
#     finally:
#         urllib.urlopen = original_urlopen
#     try:
#         urllib.urlopen = dummy_urlopen_no_network
#         assert res.package_manager.get_packages_urls() == ["a", "b"]
#     finally:
#         urllib.urlopen = original_urlopen
