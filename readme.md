#Bug in AdaBoostRegressor

This bug is reported [here](https://github.com/scikit-learn/scikit-learn/issues/7408)

Without set random_state AdaBoostRegressor give better result mean absolute error(MAE).

#without random_state
```
python bug_adaboost_random_state_not_set.py
```
Output will be something like:

```
(0, 'MAE', 0.64210829927483515, 'PCC', 0.88549049415774561, 34.13120102882385, 'Tue Sep 13 12:22:09 2016', 'Train sahpe:', (1486, 300), 'eval sahpe:', (166, 300))
(1, 'MAE', 0.65935432018365303, 'PCC', 0.88932694114994282, 37.33173990249634, 'Tue Sep 13 12:22:46 2016', 'Train sahpe:', (1486, 300), 'eval sahpe:', (166, 300))
(2, 'MAE', 0.61181579023180888, 'PCC', 0.88994664334296159, 38.02985692024231, 'Tue Sep 13 12:23:24 2016', 'Train sahpe:', (1487, 300), 'eval sahpe:', (165, 300))
(3, 'MAE', 0.64010735593729262, 'PCC', 0.88253657676205011, 36.51884603500366, 'Tue Sep 13 12:24:01 2016', 'Train sahpe:', (1487, 300), 'eval sahpe:', (165, 300))

```
Mean of 30 rounds is 0.627+-

#with random_state
```
python bug_adaboost_random_state_set.py
```
Output will be something like:

```
(0, 'MAE', 0.74991429159056555, 'PCC', 0.84643854536529817, 36.02293395996094, 'Tue Sep 13 12:18:35 2016', 'Train sahpe:', (1486, 300), 'eval sahpe:', (166, 300))
(1, 'MAE', 0.69388782880642208, 'PCC', 0.87814379720996882, 40.33444595336914, 'Tue Sep 13 12:19:16 2016', 'Train sahpe:', (1486, 300), 'eval sahpe:', (166, 300))
(2, 'MAE', 0.71961884645498486, 'PCC', 0.85041432831081376, 41.19895100593567, 'Tue Sep 13 12:19:57 2016', 'Train sahpe:', (1487, 300), 'eval sahpe:', (165, 300))
(3, 'MAE', 0.75403383887973485, 'PCC', 0.83828696225622623, 35.856842041015625, 'Tue Sep 13 12:20:33 2016', 'Train sahpe:', (1487, 300), 'eval sahpe:', (165, 300))
```
