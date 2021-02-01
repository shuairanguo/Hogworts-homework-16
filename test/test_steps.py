import pytest
import yaml

def steps1():
    print("step1")
def steps2():
    print("steps2")

def step3():
    print("step3")

def steps(path):
    with open(path) as f:
        stepss = yaml.safe_load(f)
    for step in stepss:
        if "step1" in step:
            steps1()
        elif "step2" in step:
            steps2()
        elif "step3" in step:
            step3()


def test_func():
    steps('../step.yml')