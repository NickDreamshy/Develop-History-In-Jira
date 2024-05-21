import unittest
from getting_info_from_txt import getting_date_deep


class TestGettingDateDeep(unittest.TestCase):

    def test_getting_date_deep(self):
        # Создаем временный файл для тестирования
        # with open('test_sources.txt', 'w') as file:
        #     file.write("VCS URL: https://github.com/example/example_repo\nCommit hash: abc123\n")

        # Проверяем, что функция возвращает правильный словарь для данного файла
        expected_result = {'ssh://git@example.com:/prj33-123.git': '123456789a1s3bb8814fffaaa18765d6d67fffa5'}
        self.assertEqual(expected_result.keys(),
                         getting_date_deep('sources.txt').keys())
        self.assertEqual(len(expected_result.keys()),
                         len(getting_date_deep('sources.txt').keys()))
        self.assertEqual(len(expected_result.values()),
                         len(getting_date_deep('sources.txt').values()))
        # self.assertEqual(1, len(getting_date_deep('sources.txt')))
        self.assertEqual(type(expected_result),
                         type(getting_date_deep('sources.txt')))
        self.assertEqual(list(expected_result.values()),
                         list(getting_date_deep('sources.txt').values()))
        self.assertEqual(type(expected_result.values()),
                         type(getting_date_deep('sources.txt').values()))
        self.assertEqual(list(expected_result.values())[0],
                         list(getting_date_deep('sources.txt').values())[0])
        self.assertEqual(type(list(expected_result.values())[0]),
                         type(list(getting_date_deep('sources.txt').values())[0]))

if __name__ == '__main__':
    unittest.main()
