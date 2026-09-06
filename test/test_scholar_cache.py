"""Local cache integration tests. Never contacts Google Scholar."""
import importlib.util
from pathlib import Path
import tempfile
import os
import unittest
from unittest.mock import patch
import yaml

spec = importlib.util.spec_from_file_location('update', Path(__file__).resolve().parents[1] / 'bin/update_scholar_citations.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ScholarCacheTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.previous = Path.cwd()
        os.chdir(self.tmp.name)
        Path('_data').mkdir()
        Path('_data/socials.yml').write_text('scholar_userid: test\n')
        self.output = Path('_data/citations.yml')
        self.output.write_text('papers: {}\n')

    def tearDown(self):
        os.chdir(self.previous)
        self.tmp.cleanup()

    def run_fetch(self, author):
        with patch.object(module.scholarly, 'search_author_id', return_value={}), patch.object(module.scholarly, 'fill', return_value=author):
            module.get_scholar_citations()

    def test_author_total_is_not_sum_of_papers(self):
        self.output.unlink()
        self.run_fetch({'scholar_id': 'test', 'citedby': 12, 'publications': [{'author_pub_id': 'test:one', 'num_citations': 8, 'bib': {'title': 'Paper'}}]})
        data = yaml.safe_load(self.output.read_text())
        self.assertEqual(data['author']['total_citations'], 12)
        self.assertEqual(data['papers']['test:one']['citations'], 8)
        self.assertIn('last_updated', data['metadata'])

    def test_partial_response_preserves_cache(self):
        before = self.output.read_bytes()
        with self.assertRaises(ValueError):
            self.run_fetch({'scholar_id': 'test', 'citedby': 12, 'publications': [{'bib': {'title': 'Partial'}}]})
        self.assertEqual(before, self.output.read_bytes())

    def test_zero_is_valid(self):
        self.run_fetch({'scholar_id': 'test', 'citedby': 0, 'publications': []})
        self.assertEqual(yaml.safe_load(self.output.read_text())['author']['total_citations'], 0)

    def test_network_failure_preserves_cache(self):
        before = self.output.read_bytes()
        with patch.object(module.scholarly, 'search_author_id', side_effect=RuntimeError('blocked')):
            with self.assertRaises(RuntimeError):
                module.get_scholar_citations()
        self.assertEqual(before, self.output.read_bytes())


if __name__ == '__main__':
    unittest.main()
