from src.jobs import read
from src.sorting import sort_by

jobs = read("src/jobs.csv")


def test_sort_by_criteria():

    sort_by(jobs, "min_salary")
    assert jobs[0]["min_salary"] == "19857"
