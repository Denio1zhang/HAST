# SPHERE

This repository accompanies the paper *SPHERE: Station-Level Encoding with Pair-History Enhanced Readout for Metro Origin–Destination Prediction*, currently under review at IEEE TKDE.

The full code will be released upon acceptance.

## Released now
- `predictions/hz/sphere_seed{0..4}.npz`: test-set predictions on HZMetro (5 seeds), each an array `pred` of shape (345, 80, 80).
- `evaluate.py`: computes wMAPE, nonzero wMAPE, MAE and RMSE .

## Reproducing Table II (Hangzhou)
```
python evaluate.py --gt hz_test_y.npz --pred predictions/hz/sphere_seed*.npz
```

| wMAPE (%) | wMAPE nonzero (%) | MAE | RMSE |
|---|---|---|---|
| 38.95 ± 0.02 | 34.81 ± 0.03 | 1.092 | 2.294 |
