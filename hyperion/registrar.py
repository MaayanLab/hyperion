"""Handles scheduling health checks.
"""


import sched
import time


health_checks = []


def register_health_check(checker):
    health_checks.append(checker)


def _check_all(sc):
    for hc in health_checks:
        hc.time_passed += 1
        if hc.time_passed == hc.interval_secs:
            hc.reset()
            if not hc.is_healthy():
                hc.on_fail()
    sc.enter(1, 1, _check_all, (sc,))


def start():
    s = sched.scheduler(time.time, time.sleep)
    s.enter(1, 1, _check_all, (s,))
    s.run()