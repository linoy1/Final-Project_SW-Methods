# # import unittest
# import storekeeper
#
# class TestStorekeeper(unittest.TestCase):
#
# # def test_selectStorekeeperById(self):
#     from mock_db import MockDB
#     from mock import patch
#     import utils
#
#         class TestUtils(MockDB):
#
#             def test_db_write(self):
#                 with self.mock_db_config:
#                     self.assertEqual(utils.db_write("""INSERT INTO `test_table` (`id`, `text`, `int`) VALUES
#                                     ('3', 'test_text_3', 3)"""), True)
#                     self.assertEqual(utils.db_write("""INSERT INTO `test_table` (`id`, `text`, `int`) VALUES
#                                     ('1', 'test_text_3', 3)"""), False)
#                     self.assertEqual(utils.db_write("""DELETE FROM `test_table` WHERE id='1' """), True)
#                     self.assertEqual(utils.db_write("""DELETE FROM `test_table` WHERE id='4' """), True)