# SPHERE

This repository accompanies the paper *SPHERE: Station-Level Encoding with Pair-History Enhanced Readout for Metro Origin–Destination Prediction*, currently under review at IEEE TKDE.

The full code will be released upon acceptance.

## Released now

- `predictions/hz/sphere_seed{0..4}.npz`: SPHERE test-set predictions on Hangzhou (HZMetro), five random seeds. Each file holds one array `pred` of shape (345, 80, 80): 345 test slots (15 min, 21–25 Jan 2019), 80 × 80 OD pairs.
- `evaluate.py`: computes the metrics reported in the paper (wMAPE over all OD pairs, wMAPE over nonzero OD pairs, MAE, RMSE). Requires only NumPy.

## Reproducing the Hangzhou numbers in Table II

```
python evaluate.py --gt hz_test_y.npz --pred predictions/hz/sphere_seed*.npz
```

Expected output (mean ± std over five seeds):

| wMAPE (%) | wMAPE nonzero (%) | MAE | RMSE |
|---|---|---|---|
| 38.95 ± 0.02 | 34.81 ± 0.03 | 1.092 | 2.294 |

The ground truth is not included. `--gt` expects an `.npz` file with one array `y` holding the HZMetro test OD matrices, of the same shape as `pred`.
