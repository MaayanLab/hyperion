"""Handles scheduling health checks.
"""


import threading
import sched
import time


health_checks = {}
s = sched.scheduler(time.time, time.sleep)


def register_health_check(app_name, check):
    if not app_name in health_checks:
        health_checks[app_name] = []
    health_checks[app_name].append(check)


def get_status():
    results = []
    for app in health_checks:
        result = {
            'app': app,
            'tests': []
        }
        for hc in health_checks[app]:
            result['tests'].append({
                'name': hc.name,
                'status': 'passing' if hc.is_healthy() else 'failing',
                'url': hc.url,
                'email': hc.email,
                'interval': hc.interval_secs
            })
        results.append(result)
    return results


def _check_apps(sc):
    for app in health_checks:
        for hc in health_checks[app]:
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

    sc.enter(1, 1, _check_apps, (sc,))


def _start():
    print('Starting health checks.')
    s.enter(1, 1, _check_apps, (s,))
    s.run()


def start():
    t = threading.Thread(target=_start, daemon=True)
    t.start()