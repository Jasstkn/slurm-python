branch = input()
tests_passed = int(input())
coverage = float(input())
approvals = int(input())

if branch.lower() not in ("development", "staging"):
    print(f"В ветке {branch} непроверенный код, пропускаем")
else:
    if tests_passed == 1 and coverage > 5:
        print(f"Внимание! Код из {branch} отправлен в релиз!")
    elif tests_passed == 1 and approvals >= 3:
        print(f"Внимание! Код из {branch} отправлен в релиз!")
    else:
        print(f"Код из {branch} с результатами тесты: {tests_passed}, coverage: {coverage}, approve: {approvals} в релиз не попадает.")
