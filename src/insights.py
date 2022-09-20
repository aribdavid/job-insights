from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_types = []
    for job in jobs_list:
        if job["job_type"] not in unique_types:
            unique_types.append(job["job_type"])
    return unique_types


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    jobs_list = read(path)
    unique_list = []

    for jobs in jobs_list:
        if jobs["industry"] not in unique_list and len(jobs["industry"]) != 0:
            unique_list.append(jobs["industry"])

    return unique_list


def filter_by_industry(jobs, industry):

    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):

    jobs_list = read(path)
    salaries_list = [
        int(job["max_salary"])
        for job in jobs_list
        if job["max_salary"].isnumeric()
    ]

    return max(salaries_list)


def get_min_salary(path):

    jobs_list = read(path)
    salaries_list = [
        int(job["min_salary"])
        for job in jobs_list
        if job["min_salary"].isnumeric()
    ]

    return min(salaries_list)


def matches_salary_range(job, salary):

    if (
        "min_salary" not in job
        or "max_salary" not in job
        or isinstance(job["min_salary"], int) is False
        or isinstance(job["max_salary"], int) is False
        or isinstance(salary, int) is False
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError
    if job["min_salary"] <= salary and job["max_salary"] >= salary:
        return True

    return False


def filter_by_salary_range(jobs, salary):
    filter_jobs = []
    fitted_jobs = []

    for job in jobs:
        if (
            "max_salary" in job
            and "min_salary" in job
            and type(job["min_salary"]) == int
            and type(job["max_salary"]) == int
            and type(salary) == int
            and job["min_salary"] < job["max_salary"]
        ):
            fitted_jobs.append(job)

    for job in fitted_jobs:
        if matches_salary_range(job, salary):
            filter_jobs.append(job)

    return filter_jobs
