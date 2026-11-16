def contabilizador(tests):
    test_pass = 0
    test_fail = 0
    test_error = 0
    test_skipped = 0

    for test in tests:
        try:
            resultado = test()

            if resultado == "PASS":
                test_pass += 1

            elif resultado == "FAIL":
                test_fail += 1

            elif resultado == "ERROR":
                test_error += 1

            elif resultado == "SKIPPED":
                test_skipped += 1

            else:
                print(
                    f"Test {test.__name__} returned "
                    f"an unexpected result: {resultado}"
                )
                test_error += 1

        except Exception as e:
            print(f"Test {test.__name__} raised an exception: {e}")
            test_error += 1

    total_tests = len(tests)
    total_ejecutados = test_pass + test_fail + test_error

    porcentaje_exito = (
        (test_pass / total_ejecutados) * 100
        if total_ejecutados > 0 else 0
    )

    print(f"Total tests: {total_tests}")
    print(f"Passed: {test_pass}")
    print(f"Failed: {test_fail}")
    print(f"Errored: {test_error}")
    print(f"Skipped: {test_skipped}")
    print(f"Success rate: {porcentaje_exito:.2f}%")

    return test_pass, test_fail, test_error, test_skipped
