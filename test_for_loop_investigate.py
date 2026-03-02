def test_output(capsys):
    import for_loop_investigate
    captured = capsys.readouterr()

    assert "I love corn.\n"*7 in captured.out, "I love corn needs to be printed 7 times"
    assert "\n".join(map(str, range(1, 21))) in captured.out, "Didn't print all numbers from 1 to 20"
    assert "\n".join(map(str, range(1, 101, 2))) in captured.out, "Didn't print all odd numbers from 1 to 100"
    assert "\n".join(map(str, range(20, 0, -1))) in captured.out, "Didn't print all numbers from 20 down to 1"
    assert all(str(i**3) in captured.out for i in range(1, 11)), "Didn't print all cubes from 1 to 10"
    assert "\n".join(map(str, range(0, 101, 10))) in captured.out, "Didn't print every 10th number from 0 to 100"