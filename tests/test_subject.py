""" tests for Subject """

import unittest

import pydantic
import datetime

from aind_data_schema import Subject


class SubjectTests(unittest.TestCase):
    """tests for subject"""

    def test_constructors(self):
        """try building Subjects"""

        with self.assertRaises(pydantic.ValidationError):
            s = Subject()

        s = Subject(
            species="Mus musculus",
            specimen_id="1234",
            sex="Male",
            date_of_birth=datetime.datetime.now(),
            genotype="wt",
            light_cycle="reverse",
        )

        assert s is not None


if __name__ == "__main__":
    unittest.main()
