import runner
import unittest


#  Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest.
#  В классе пропишите следующие методы:

    # test_walk - метод, в котором создаётся объект класса Runner
        # с произвольным именем. Далее вызовите метод walk у этого объекта 10 раз.
        # После чего методом assertEqual сравните distance этого объекта со значением 50.
    # test_run - метод, в котором создаётся объект класса Runner с произвольным именем.
        # Далее вызовите метод run у этого объекта 10 раз.
        # После чего методом assertEqual сравните distance этого объекта со значением 100.
    # test_challenge - метод в котором создаются 2 объекта класса Runner с
        # произвольными именами. Далее 10 раз у объектов вызываются методы run и walk
        # соответственно. Т.к. дистанции должны быть разными,
        # используйте метод assertNotEqual, чтобы убедится в неравенстве результатов.
class RunnerTest(unittest.TestCase):
    def test_wolk(self):
        run_wolk = runner.Runner('Wolk')

        for _ in range(10):
            run_wolk.walk()
        self.assertEqual(run_wolk.distance, 50)

    def test_run(self):
        run_run = runner.Runner('Run')

        for _ in range(10):
            run_run.run()
        self.assertEqual(run_run.distance, 100)

    def test_challenge(self):
        run_wolk = runner.Runner('Wolk')
        run_run = runner.Runner('Run')

        for _ in range(10):
            run_wolk.walk()
            run_wolk.run()

        for _ in range(9):
            run_run.walk()
            run_run.run()
            
        self.assertNotEqual(run_wolk.distance, run_run.distance)


if __name__ == '__main__':
    unittest.main()