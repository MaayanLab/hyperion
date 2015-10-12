"""Handles scheduling health checks.
"""


import threading
import sched
import time


health_checks = []
s = sched.scheduler(time.time, time.sleep)
event = None


def register_health_check(checker):
    health_checks.append(checker)


def _check_all(sc):
    for hc in health_checks:
        hc.time_passed += 1
        if hc.time_passed != hc.interval_secs:
            continue

        print('Checking "%s"' % hc.name)
        hc.reset()
        if hc.is_healthy():
            hc.already_notified = False
            continue

        if hc.already_notified:
            continue

        hc.already_notified = True
        hc.on_fail()

    sc.enter(1, 1, _check_all, (sc,))


def get_status():
    results = []
    for hc in health_checks:
        results.append({
            'name': hc.name,
            'status': 'healthy' if hc.is_healthy() else 'broken'
        })
    return results


def start():
    s.enter(1, 1, _check_all, (s,))
    t = threading.Thread(target=s.run, daemon=True)
    t.start()